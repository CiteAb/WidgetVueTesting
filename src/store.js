import { reactive } from 'vue'

export const store = reactive({
  citations: [
  ],
  allImageUrls: [
  ],
  imagePopupOpen: false,
  carousel: {
    imageUrls: [],
    total: 100,
    nextUrl: 'aaa'
  },
  filters: {},
  setFilter(filter) {
    store.filters = {...store.filters, ...filter};
    console.log(store.filters);
    fetchData();
  }
});

const fetchData = async () => {
  const params = new URLSearchParams(store.filters);
  const res = await fetch(`http://127.0.0.1:5000/data?${params.toString() || ''}`);
  const data = await res.json();
  store.citations = data.citations;
  store.allImageUrls = data.allImageUrls;
}

fetchData();