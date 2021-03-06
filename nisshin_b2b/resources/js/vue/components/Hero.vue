<template>
  <section id="hero" class="block overflow-x-hidden">

    <div class="relative">
      <div class="image-filter"></div>
      <div class="white-filter"></div>
      <div class="sm:max-w-screen-sm md:max-w-screen-md lg:max-w-screen-lg mx-auto">
        <Splide ref="splide" :options="mainOptions">
          <SplideSlide v-for="slide in slides" :key="'main_' + slide.id">
            <a :href="slide.link" :target="slide.target">
              <img :src="slide.src_sp" :alt="slide.title" class="md:hidden">
              <img :src="slide.src_pc" :alt="slide.title" class="hidden md:block">
            </a>
          </SplideSlide>
        </Splide>
      </div>
    </div>

    <div class="hidden md:block relative sm:max-w-screen-sm md:max-w-screen-md lg:max-w-screen-lg mx-auto py-5">
      <Splide ref="thumbs" :options="thumbsOptions" class="relative z-10 text-center">
        <SplideSlide v-for="slide in slides" :key="'thmb_' + slide.id" class="w-full">
          <div class="bg-white">
            <img :src="slide.src_pc" :alt="slide.title" class="w-full h-auto">
          </div>
        </SplideSlide>
      </Splide>
      <div class="absolute left-0 bottom-0 w-full h-full flex justify-between items-center">
        <button ref="prev" class="-ml-10" @click="prevSlide">
          <svg-vue  icon="chevron_alt" class="w-4 h-4 -rotate-90"></svg-vue>
        </button>
        <button ref="next" class="-mr-10" @click="nextSlide">
          <svg-vue  icon="chevron_alt" class="w-4 rotate-90"></svg-vue>
        </button>
      </div>
    </div>
  </section>
</template>

<script>

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
        arrows    : false,
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
        arrows      : false,
        drag        : false,
      },
    }
  },

  components: {
  },

  methods: {
    prevSlide: function () {
      console.log('prev')
      this.$refs.splide.go( '<' );
    },
    nextSlide: function () {
      console.log('next')
      this.$refs.splide.go( '>' );
    }
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
  .splide__track{
    display: flex;
    justify-content: center;
  }
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
