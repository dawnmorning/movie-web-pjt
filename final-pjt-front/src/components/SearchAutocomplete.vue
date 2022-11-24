<template>
   <div class="autocomplete">
    <input
      @input="onChange"
      @keydown.down="onArrowDown"
      @keydown.up="onArrowUp"
      @keydown.enter="onEnter"
      type="text"
      style="margin-right:5px; background-color: #f5f5f5';" placeholder='검색도 가능해요!'
    />
    <ul
      v-show="isOpen"
      class="autocomplete-results"
    >
      <li
          v-if="isLoading"
          class="loading"
        >
        Loading results...
      </li>
      <li
        v-else
        v-for="(result, i) in results"
        :key="i"
        @click="setResult(result)"
        class="autocomplete-result"
        :class="{ 'is-active': i === arrowCounter }"
      >
      {{ result }}
      </li>
    </ul>
    <button class="btn btn-outline-success"
    @click="selectMovie"
    style='width:60px; height:20px; position:relative; padding:0;'
    ><i style='' class="fa-solid fa-magnifying-glass"></i></button>
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

  .autocomplete-result {
    list-style: none;
    text-align: left;
    padding: 4px 2px;
    cursor: pointer;
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