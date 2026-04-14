<script setup lang="ts">
  import { store } from '../store.js'

</script>

<template>
  <div v-if="store.imagePopupOpen" class="modal-overlay">
    <div class="image-modal">
      <div class="image-modal-main">
        <div class="image-count">📷 1 of 100</div>
        <button class="nav-btn left"><span>&lt;</span></button>
        <div class="image-box">
          <span class="image-placeholder">
            <svg width="48" height="48" fill="none" stroke="#888" stroke-width="2" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 17l5-5a2 2 0 0 1 2.8 0l5.2 5.2M14 14l1-1a2 2 0 0 1 2.8 0l3.2 3.2"/></svg>
          </span>
        </div>
        <button class="nav-btn right"><span>&gt;</span></button>
        <button class="close-btn" @click="store.imagePopupOpen = false">✕ Close</button>
      </div>
      <div class="image-desc">
        Western blot analysis of extracts from HeLa cells transfected with 100 nM control siRNA #6201 (C-) or p44 MAPK (Erk1) siRNA (+), using p44/42 MAPK (Erk1/2) Antibody #9102 and GCK Antibody #3732. The Erk1/2 antibody confirms silencing of Erk1 expression, and GCK Antibody is used to control for loading and specificity of p44 MAPK (Erk1) siRNA.
      </div>
      <div class="thumb-row">
        <div class="thumb" v-for="n in 10" :key="n">
          <span class="thumb-placeholder">
            <svg width="28" height="28" fill="none" stroke="#888" stroke-width="2" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 17l5-5a2 2 0 0 1 2.8 0l5.2 5.2M14 14l1-1a2 2 0 0 1 2.8 0l3.2 3.2"/></svg>
          </span>
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
  z-index: 2000;
}
.image-modal {
  background: #f4f4f5;
  border-radius: 10px;
  padding: 28px 24px 20px 24px;
  min-width: 800px;
  box-shadow: 0 2px 16px rgba(0,0,0,0.13);
  border: 1px solid #bdbdbd;
  display: flex;
  flex-direction: column;
  gap: 18px;
}
.image-modal-main {
  position: relative;
  background: #fff;
  border-radius: 8px;
  border: 2px solid #3b82f6;
  min-height: 340px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 8px;
}
.image-count {
  position: absolute;
  top: 12px;
  left: 16px;
  background: #111;
  color: #fff;
  font-size: 15px;
  border-radius: 6px;
  padding: 3px 12px;
  z-index: 2;
}
.nav-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: #fff;
  border: 2px dashed #3b82f6;
  border-radius: 6px;
  width: 38px;
  height: 38px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  color: #3b82f6;
  cursor: pointer;
  z-index: 2;
}
.nav-btn.left {
  left: 12px;
}
.nav-btn.right {
  right: 12px;
}
.image-box {
  width: 340px;
  height: 260px;
  background: #f4f4f5;
  border: 2px dashed #bdbdbd;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 60px;
}
.image-placeholder {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 48px;
  height: 48px;
  color: #888;
}
.close-btn {
  position: absolute;
  left: 16px;
  bottom: 16px;
  background: #fff;
  color: #111;
  border: 1.5px solid #bdbdbd;
  border-radius: 6px;
  padding: 6px 18px;
  font-size: 15px;
  cursor: pointer;
  transition: background 0.2s;
  z-index: 2;
  display: flex;
  align-items: center;
  gap: 6px;
}
.close-btn:hover {
  background: #f3f3f3;
}
.image-desc {
  font-size: 13px;
  color: #222;
  background: none;
  margin-bottom: 0;
}
.thumb-row {
  display: flex;
  gap: 12px;
  justify-content: flex-start;
  margin-top: 0;
}
.thumb {
  background: #fff;
  border: 2px dashed #bdbdbd;
  border-radius: 6px;
  width: 38px;
  height: 38px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}
.thumb-placeholder {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  color: #888;
}
</style>