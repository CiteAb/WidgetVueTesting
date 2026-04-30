<script setup lang="js">
  import Graph from 'graphology';
  import Sigma from 'sigma';
  import forceAtlas2 from 'graphology-layout-forceatlas2';
  import FA2Layout from 'graphology-layout-forceatlas2/worker';
  import circlepack from 'graphology-layout/circlepack';  
  import { onMounted } from 'vue';
  import { store } from '../store.js'
  import { animateNodes } from "sigma/utils";

  onMounted(() => {
    const graph = new Graph();

    store.graphData.nodes.forEach(node => {
      graph.addNode(node.id, { label: node.name, forceLabel: false, x: Math.random(), y: Math.random(), size: 10, color: "blue" });
    });

    store.graphData.links.forEach(link => {
      graph.addEdge(link.source, link.target, { size: link.value / 1000, color: "grey" });
    });

    // let settings = forceAtlas2.inferSettings(graph);
    // const fa2Layout = new FA2Layout(graph, {
    //   settings: settings,
    // });

    const renderer = new Sigma(graph, document.getElementById("container"));

    renderer.setSettings({
      enableCameraZooming: false,
      enableCameraPanning: false,
      enableCameraRotation: false,
      labelRenderedSizeThreshold: 1000
    });

    let state = {};
    function setHoveredNode(node) {
      if (node) {
        state.hoveredNode = node;
        state.hoveredNeighbors = new Set(graph.neighbors(node));
      }

      if (!node) {
        state.hoveredNode = undefined;
        state.hoveredNeighbors = undefined;
      }

      // Refresh rendering
      renderer.refresh({
        // We don't touch the graph data so we can skip its reindexation
        skipIndexation: true,
      });
    }

     renderer.on("enterNode", ({ node }) => {
      setHoveredNode(node);
    });
    renderer.on("leaveNode", () => {
      setHoveredNode(undefined);
    });


    renderer.setSetting("nodeReducer", (node, data) => {
      const res = { ...data };

      if (state.hoveredNeighbors && !state.hoveredNeighbors.has(node) && state.hoveredNode !== node) {
        res.label = "";
        res.color = "#f6f6f6";
      }

      if (state.selectedNode === node) {
        res.highlighted = true;
      } else if (state.suggestions) {
        if (state.suggestions.has(node)) {
          res.forceLabel = true;
        } else {
          res.label = "";
          res.color = "#f6f6f6";
        }
      }

      return res;
    });

    renderer.setSetting("edgeReducer", (edge, data) => {
      const res = { ...data };

      if (
        state.hoveredNode &&
        !graph.extremities(edge).every((n) => n === state.hoveredNode || graph.areNeighbors(n, state.hoveredNode))
      ) {
        res.hidden = true;
      }

      if (
        state.suggestions &&
        (!state.suggestions.has(graph.source(edge)) || !state.suggestions.has(graph.target(edge)))
      ) {
        res.hidden = true;
      }

      return res;
    });

    
    //forceAtlas2(graph, {iterations: 50000});

    // fa2Layout.start();
    const positions = forceAtlas2(graph, {iterations: 1000});
    //forceAtlas2.assign(graph, {iterations: 1000});
    animateNodes(graph, positions, { duration: 2000 }, () => {
      renderer.setSetting("labelRenderedSizeThreshold", 0);
    });

  });
</script>

<template>
  <div id="container" style="background: white; height: 100%"></div>
  
</template>