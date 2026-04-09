<script setup lang="ts">
  import BarChart from './BarChart.vue'
</script>

<template>
  <div class="charts">
    <div class="chart-box chart-box-full">
      <span>Citation over time</span>
      <BarChart :data="[{Year: 2021, Value: 1}, {Year: 2022, Value: 2}, {Year: 2023, Value: 3}]" />
      <button class="enlarge-btn">Enlarge</button>
    </div>
    <div class="chart-box">
      <span>Disease states</span>
      <button class="enlarge-btn">Enlarge</button>
    </div>
    <div class="chart-box">
      <span>Research Area / Impact factor</span>
      <button class="enlarge-btn">Enlarge</button>
    </div>
  </div>
</template>

<style scoped>
  .charts {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }

  .chart-box {
    background: #fff;
    border: 1px solid #ccc;
    border-radius: 6px;
    height: 10rem;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 10px;
    margin-bottom: 8px;
    position: relative;

    span {
      position: absolute;
      left: 5px;
      top: 5px;
    }
  }
  .chart-box .enlarge-btn {
    position: absolute;
    bottom: 8px;
    left: 8px;
    background: #fff;
    border: 1px solid #ccc;
    border-radius: 6px;
    font-size: 13px;
    padding: 4px 12px;
    cursor: pointer;
  }

  .chart-box-full {
    grid-column-start: 1;
    grid-column-end: 3;
  }
</style>