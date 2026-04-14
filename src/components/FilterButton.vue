<script setup lang="ts">
  import { ref } from 'vue'
  import { store } from '../store.js'

  // state
  const filtersOpen = ref(false)

</script>


<template>
  <div>
    <button @click="filtersOpen = true">Sort and filter</button>
    <div v-if="filtersOpen" class="modal-overlay">
      <div class="filter-modal">
        <div class="modal-header">
          <span>Sort</span>
        </div>
        <div class="sort-row">
          <select>
            <option>Newest &gt; oldest</option>
            <option>Oldest &gt; newest</option>
          </select>
          <select>
            <option>Impact factor</option>
          </select>
          <select>
            <option>Citation count</option>
          </select>
          <select>
            <option>Date range</option>
          </select>
        </div>
        <div class="modal-header">
          <span>Filter</span>
        </div>
        <div class="filter-row">
          <label><input type="checkbox" @change="store.setFilter({pubmed: $event.target.checked})"> PubMed</label>
          <label><input type="checkbox"> Preprints</label>
          <label><input type="checkbox" checked> Has images</label>
        </div>
        <div class="dropdown-grid">
          <select><option>All reactants</option></select>
          <select><option>All applications</option></select>
          <select><option>All research areas</option></select>
          <select><option>Reagent type</option></select>
          <select><option>Country</option></select>
          <select><option>Journal</option></select>
          <select><option>Institution</option></select>
          <select><option>Validation</option></select>
          <select><option>Instrument used</option></select>
          <select><option>Dilution</option></select>
        </div>
        <div class="modal-header">
          <span>Find</span>
        </div>
        <div class="find-row">
          <div class="find-input">
            <input type="text" placeholder="Product code">
            <span class="search-icon">🔍</span>
          </div>
          <div class="find-input">
            <input type="text" placeholder="Author name">
            <span class="search-icon">🔍</span>
          </div>
        </div>
        <div class="modal-actions">
          <button class="apply-btn">Apply</button>
          <button class="close-btn" @click="filtersOpen = false">Close</button>
        </div>
      </div>
    </div>
  </div>
</template>



<style scoped>
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0,0,0,0.18);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
  }
  .filter-modal {
    background: #f4f4f5;
    border-radius: 10px;
    padding: 28px 24px 20px 24px;
    min-width: 700px;
    box-shadow: 0 2px 16px rgba(0,0,0,0.13);
    border: 1px solid #bdbdbd;
  }
  .modal-header {
    font-weight: 600;
    margin-bottom: 10px;
    margin-top: 18px;
    color: #222;
  }
  .sort-row {
    display: flex;
    gap: 12px;
    margin-bottom: 18px;
  }
  .sort-row select {
    padding: 6px 18px 6px 10px;
    border-radius: 6px;
    border: 1px solid #d1d5db;
    background: #fff;
    font-size: 15px;
  }
  .filter-row {
    display: flex;
    gap: 18px;
    align-items: center;
    margin-bottom: 18px;
  }
  .filter-row label {
    font-size: 15px;
    display: flex;
    align-items: center;
    gap: 4px;
  }
  .filter-row .preprints input[type="checkbox"] {
    accent-color: #a78bfa;
  }
  .dropdown-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px 18px;
    margin-bottom: 18px;
  }
  .dropdown-grid select {
    padding: 6px 18px 6px 10px;
    border-radius: 6px;
    border: 1px solid #d1d5db;
    background: #fff;
    font-size: 15px;
  }
  .find-row {
    display: flex;
    gap: 18px;
    margin-bottom: 18px;
  }
  .find-input {
    position: relative;
    flex: 1;
  }
  .find-input input {
    width: 90%;
    padding: 7px 34px 7px 10px;
    border-radius: 6px;
    border: 1px solid #d1d5db;
    background: #fff;
    font-size: 15px;
  }
  .search-icon {
    position: absolute;
    right: 10px;
    top: 50%;
    transform: translateY(-50%);
    pointer-events: none;
    color: #888;
  }
  .modal-actions {
    display: flex;
    gap: 12px;
    justify-content: flex-start;
    margin-top: 8px;
  }
  .apply-btn {
    background: #111;
    color: #fff;
    border: none;
    border-radius: 6px;
    padding: 7px 22px;
    font-size: 15px;
    cursor: pointer;
    transition: background 0.2s;
  }
  .apply-btn:hover {
    background: #333;
  }
  .close-btn {
    background: #fff;
    color: #111;
    border: 1px solid #bdbdbd;
    border-radius: 6px;
    padding: 7px 22px;
    font-size: 15px;
    cursor: pointer;
    transition: background 0.2s;
  }
  .close-btn:hover {
    background: #f3f3f3;
  }
</style>