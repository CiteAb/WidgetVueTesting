<script setup lang="ts">
import Citationlist from './components/CitationList.vue'
import ChartSection from './components/ChartSection.vue'
import FilterButton from './components/FilterButton.vue'
</script>

<template>
  <header>
      <div class="logo">
        <span>Powered by</span>
        <h1>CiteAb</h1>
      </div>
      <button class="icon-btn" aria-label="Settings">
        <!-- Settings icon (placeholder) -->
        <span>⚙️</span>
      </button>
    </header>

    <section class="stats">
      <div class="stat-box">
        <div class="stat-number">1000</div>
        <div class="stat-label">(Citation count)</div>
      </div>
      <div class="stat-box">
        <div class="stat-number">1000</div>
        <div class="stat-label">(Image count)</div>
      </div>
      <div class="stat-box">
        <div class="stat-number">1000</div>
        <div class="stat-label">(Yearly citation count)</div>
      </div>
    </section>

    <section class="summary">
      <span class="icon">⚠️</span>
      <div>
        <strong>AI product summary:</strong><br>
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
      </div>
    </section>

    <section class="controls">
      <FilterButton />
      <input type="text" placeholder="" aria-label="Search">
      <button aria-label="Search">🔍</button>
    </section>

    <main class="main-content">
      <section class="left">
        <div class="section-title">Product Images</div>
        <div class="product-image-box">
          <span class="img-count">📷 1 of 100</span>
          <div class="img-nav">
            <button aria-label="Previous image">&#60;</button>
            <button aria-label="Next image">&#62;</button>
          </div>
          <button class="enlarge-btn">Enlarge</button>
        </div>
        <div class="product-image-desc">
          Western blot analysis of extracts from HeLa cells transfected with 100 nM control siRNA #621 (C-) or p44 MAPK (Erk1) siRNA (+), using p44/42 MAPK (Erk1/2) Antibody #9102 and GCK Antibody #3732. The Erk1/2 antibody confirms silencing of Erk1 expression, and GCK Antibody is used to control for loading and specificity of p44 MAPK (Erk1) siRNA.
        </div>
        <div class="product-image-thumbs">
          <button aria-label="Thumb 1">📷</button>
          <button aria-label="Thumb 2">📷</button>
          <button aria-label="Thumb 3">📷</button>
          <button aria-label="Thumb 4">📷</button>
          <button aria-label="Thumb 5">📷</button>
        </div>
      </section>
      <section class="right">
        <ChartSection />
      </section>
    </main>

    <section class="citations-section">
      <h2>Showing 5 of 1200 Citations</h2>
      <Citationlist />
    </section>
</template>

<style scoped>

</style>
