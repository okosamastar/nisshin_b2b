<template>
  <div class="splide_images" ref="splide">
    <div class="splide__track">
      <ul class="splide__list">
        <li v-for="(image, index) in images" v-bind:key="index" class="splide__slide">
          <img :src="image" alt="日清製粉ウェルナ" class="w-full">
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import Splide from '@splidejs/splide';
import { AutoScroll } from '@splidejs/splide-extension-auto-scroll';


export default {
  props: {
    images: {
      type: Array,
      default: []
    },
  },

  data() {
    return {
      splide: null,
      options: {
        type: 'loop',
        drag   : 'free',
        focus  : 'center',
        perPage: 5,
        gap: '1rem',
        arrows: false,
        pagination: false,
        autoScroll: {
          speed: 2,
        },
        breakpoints: {
          543: {
            perPage: 1,
            padding: '3rem'
          },
          767: {
            perPage: 2,
            padding: '3rem'
          },
          991: {
            perPage: 3,
            padding: '3rem'
          },
        }
        // breakpoints: {
        //   800: {
        //     centerMode: false,
        //     itemsToShow: 3
        //   },
        //   1000: {
        //     itemsToShow: 6,
        //     pagination: 'fraction'
        //   }
        // }
      }
    }
  },

  components: {

  },

  methods: {
  },

  mounted() {
    this.splide = new Splide( '.splide_images', this.options ).mount({ AutoScroll });
  },

  destroyed() {},

};
</script>

<style scoped>
</style>
