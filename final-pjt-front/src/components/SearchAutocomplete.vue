<template>
   <div class="autocomplete">
    <input
      @input="onChange"
      @keydown.down="onArrowDown"
      @keydown.up="onArrowUp"
      @keydown.enter="onEnter"
      type="text"
      style="margin-top:8px; margin-right:5px; background-color: #f5f5f5; border-radius:0.1cm" placeholder='영화 검색' :value=" search"
    />
    <button class="btn btn-outline-dark"
    @click="selectMovie"
    style='width:60px; height:30px; position:relative; padding:0;'
    ><i style='' class="fa-solid fa-magnifying-glass"></i></button>
    <ul
      v-show="isOpen"
      class="autocomplete-results1"
    >
      <li
          v-if="isLoading"
          class="loading"
          style='width:160px;'
        >
        Loading results...
      </li>
      <li
        v-else
        v-for="(result, i) in results"
        :key="i"
        @click="setResult(result)"
        class="autocomplete-result1"
        :class="{ 'is-active': i === arrowCounter }"
      >
      {{ result }}
      </li>
    </ul>
    
  </div>
</template>

<script>
export default {
  name: 'SearchAutocomplete',
  props: {
    items: {
      type: Array,
      required: false,
      default: () => [],
    },
    isAsync: {
      type: Boolean,
      required: false,
      default: false,
    },
  },
  watch: {
    items: function (value) {
      if (this.isAsync) {
        this.results = value;
        this.isOpen = true;
        this.isLoading = false;
      }
    }
  },
  data() {
    return {
      search: '',
      results: [],
      isOpen: false,
      arrowCounter: -1,
      isLoading: false,
    };
  },
  methods: {
    setResult(result) {
      this.search = result;
      this.isOpen = false;
    },
    selectMovie() {
      this.$emit('selected-movie', this.search)
      this.search = ''
    },
    filterResults() {
      this.results = this.items.filter(item => item.toLowerCase().indexOf(this.search.toLowerCase()) > -1);
    },
    onChange(event) {
      this.search= event.target.value      
      this.$emit('input', this.search);

      if (this.isAsync) {
        this.isLoading = true;
      } else {
      this.filterResults();
      this.isOpen = true;
      }
    },
    handleClickOutside(event) {
      if (!this.$el.contains(event.target)) {
        this.arrowCounter = -1;
        this.isOpen = false;
      }
    },
    onArrowDown() {
      if (this.arrowCounter < this.results.length) {
        this.arrowCounter = this.arrowCounter + 1;
      }
    },
    onArrowUp() {
      if (this.arrowCounter > 0) {
        this.arrowCounter = this.arrowCounter - 1;
      }
    },
    onEnter() {
      this.search = this.results[this.arrowCounter];
      this.arrowCounter = -1;
      this.isOpen = false;
    }
  },
  mounted() {
    document.addEventListener('click', this.handleClickOutside);
  },
  unmounted() {
    document.removeEventListener('click', this.handleClickOutside);
  },
  
}
</script>

<style>
.autocomplete {
    position: relative;
    width: 600px;
    height: 40px;
    margin: 20px auto;
    border: 1px solid #bdc1c6;
    border-radius: 20px;
  }

  .autocomplete-results {
    padding: 0;
    margin: 0;
    /* border: 1px solid #eeeeee; */
    height: 120px;
    min-height: 1em;
    max-height: 400px;    
    overflow: auto;
    width: 100%;
  }

  .autocomplete-result1 {
    width:66%;
    list-style: none;
    text-align: left;
    padding: 4px 2px;
    cursor: pointer;
    background-color: white;
    position: relative;
    right: 5px;
  }

  .autocomplete-result.is-active,
  .autocomplete-result:hover {
    background-color: #4AAE9B;
    color: white;
  }

  input::placeholder{
    opacity: 0.7;
    font-size: 12px;
  }
</style>