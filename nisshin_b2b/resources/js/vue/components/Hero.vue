<template>
  <div id="hero" class="block overflow-x-hidden">

    <div class="relative">
      <div class="image-filter"></div>
      <div class="white-filter"></div>
      <div class="sm:max-w-screen-sm md:max-w-screen-md lg:max-w-screen-lg mx-auto">
        <Splide ref="splide" :options="mainOptions">
          <SplideSlide v-for="slide in slides" :key="'main_' + slide.id">
            <img :src="slide.src" :alt="slide.title">
          </SplideSlide>
        </Splide>
      </div>
    </div>

    <div class="container mx-auto py-4">
      <Splide ref="thumbs" :options="thumbsOptions">
        <SplideSlide v-for="slide in slides" :key="'thmb_' + slide.id">
          <div class="bg-white">
            <img :src="slide.src" :alt="slide.title">
          </div>
        </SplideSlide>
      </Splide>
    </div>
  </div>
</template>

<script>
import { Splide, SplideSlide } from '@splidejs/vue-splide';
import '@splidejs/splide/dist/css/splide.min.css';

export default {
  props: {
    slides: {
      type: Array,
      default: []
    },
  },

  data() {
    return {
      imagePath: this.$imagePath,
      mainOptions: {
        type      : 'loop',
        perPage   : 1,
        perMove   : 1,
        gap       : '1.6rem',
        pagination: false,
        focus     : 'center',
        arrows    : true,
      },
      thumbsOptions: {
        type        : 'slide',
        rewind      : true,
        gap         : '.865rem',
        pagination  : false,
        perPage     : 4,
        perMove     : 1,
        isNavigation: true,
        updateOnMove: true,
        arrows      : true,
      },
    }
  },

  components: {
    Splide,
    SplideSlide,
  },

  methods: {

  },

  mounted() {
    const thumbsSplide = this.$refs.thumbs?.splide;
    if ( thumbsSplide ) {
      this.$refs.splide?.sync( thumbsSplide );
    }
  },

  destroyed() {
  },

};
</script>

<style scoped lang="scss">
::v-deep .splide {
  overflow-x: visible;
  .splide__track {
    overflow: visible;
  }
  .splide__arrow svg {
    width: 1rem;
    height: 1rem;
  }
}

::v-deep .splide--nav{
  .splide__track {
    .splide__list{
      .splide__slide {
        border-width: 1px;
        border-color: transparent;
        img {
          opacity: .5;
        }
        &.is-active {
          border-width: 1px;
          border-color: #E82817;
          img {
            opacity: 1;
          }
        }
      }
    }
  }
}

::v-deep #splide02 {
  @media (min-width: 992px) {
    .splide__arrows {
      .splide__arrow {
        background-color: transparent;
        &.splide__arrow--prev {
          left: -3rem;
        }
        &.splide__arrow--next {
          right: -3rem;
        }
      }
    }
  }
}

</style>
