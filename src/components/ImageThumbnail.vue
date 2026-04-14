<script setup lang="ts">
import { store } from '../store.js'

defineProps({
  url: String
})
</script>

<template>
  <div class="thumbnail" @click="store.imagePopupOpen = true">
    <img :src="url" />
  </div>
</template>

<style scoped>
  .thumbnail {
    width: 2rem;
    height: 2rem;

    border: 1px solid grey;
    border-radius: 5px;
    background-color: white;

    img {
      max-width: 2rem;
      max-height: 2rem;
    }
  }
</style>
