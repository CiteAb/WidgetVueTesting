<script setup>
  import { onMounted, ref, watch } from 'vue'
  import * as d3 from 'd3'

  const props = defineProps({
    data: {
      type: Array,
      required: true
    },
    width: {
      type: Number,
      default: 400
    },
    height: {
      type: Number,
      default: 200
    }
  })

  const svg = ref(null)

  const drawChart = () => {
    const svgEl = d3.select(svg.value)
    svgEl.selectAll('*').remove() // Clear previous renders

    const x = d3
      .scaleBand()
      .domain(props.data.map(d => d.Year))
      .range([0, props.width])
      .padding(0.1)

    svgEl.append("g")
      .attr("transform", "translate(0," + props.height + ")")
      .call(d3.axisBottom(x))
      .selectAll("text")
        .attr("transform", "translate(10,0)")
        .style("text-anchor", "end");

    const y = d3
      .scaleLinear()
      .domain([0, 10])
      .nice()
      .range([props.height, 0])

    svgEl
      .selectAll('rect')
      .data(props.data)
      .join('rect')
      .attr('x', d => x(d.Year))
      .attr('y', d => y(d.Value))
      .attr('width', x.bandwidth())
      .attr('height', d => props.height - y(d.Value))
      .attr('fill', 'steelblue')
  }

  onMounted(drawChart)
  watch(() => props.data, drawChart)
</script>

<template>
  <svg ref="svg" viewBox="0 0 420 220"></svg>
</template>

<style scoped>
svg {
  padding: 1rem;
  height: 8rem;
  width: 16rem;
}
</style>

