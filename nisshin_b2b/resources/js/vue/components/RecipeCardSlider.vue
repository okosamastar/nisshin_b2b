<template>
  <Splide ref="splide" :options="options" class="w-full sm:px-8">
    <SplideSlide v-for="recipe in recipes" v-bind:key="recipe.url" class="wrap-image splide__slide" :class="recipe.class? recipe.class : ''">
      <a :href="recipe.link" class="block h-full flex flex-col justify-between border border-gray-200">
        <div v-if="recipe.image" class="wrap-image">
          <img :src="recipe.image" :alt="recipe.title" class="w-full">
        </div>
        <div v-else class="wrap-image">
          <img :src="recipe.staticpath + 'default_rectangle.png'" :alt="recipe.title" class="w-auto h-full mx-auto">
        </div>
        <div v-if="recipe.newmark" class="absolute left-0 top-0 w-12 h-12 mx-2">
          <img :src="imagePath + 'badge_new.png'" alt="New" class="no-effect">
        </div>
        <div class="p-4">
          <template v-if="recipe.dish_types.length > 0" class="">
            <span v-for="dish_type in recipe.dish_types" class="inline-block mb-2 py-1 px-2 text-xs border-2 border-crimson text-crimson leading-none">{{ dish_type }}</span>
          </template>
          <h5 class="font-bold">{{ recipe.title }}</h5>
        </div>
        <div v-if="recipe.events.length > 0" class="pt-2 px-4 border-t border-dashed border-gray-200 bg-gray-100">
          <span v-for="event in recipe.events" :key="event" class="inline-block mb-2 py-1.5 px-3 text-xs text-white text-center bg-crimson rounded-full leading-none">{{ event }}</span>
        </div>
      </a>
    </SplideSlide>
  </Splide>
</template>

<script>

export default {
  props: {
    recipes: {
      type: Array,
      default: []
    },
  },

  data() {
    return {
      imagePath: this.$imagePath,
      options: {
        type: 'slide',
        perPage: 4,
        perMove: 1,
        gap: '0.8rem',
        trimSpace: true,
        wheel: false,
        arrows: true,
        pagination: false,
        breakpoints: {
          543: {
            perPage: 1,
            perMove: 1,
            padding: '3.2rem',
            arrows: false,
          },
          767: {
            perPage: 2,
            perMove: 1,
            padding: '3.2rem',
            arrows: false,
          },
          991: {
            perPage: 3,
            padding: 0,
            arrows: true,
          },
          1024: {
            perPage: 3,
            padding: 0,
            arrows: true,
          },
        }
      },
      isMobile: false
    }
  },

  components: {
  },

  methods: {
    handleResize: function () {
      this.isMobile = window.innerWidth < 768
      const splideList = document.querySelector('#' + this.$refs.splide.$el.id + ' .splide__list')
      if(!this.isMobile && this.recipes.length < 5) {
        splideList.classList.add('justify-center')
      } else {
        splideList.classList.remove('justify-center')
      }
    },
  },

  created() {
    if(!this.isMobile && this.recipes.length < 5) {
      this.options = {...this.options,  arrows: false }
    }
  },

  mounted() {
    window.addEventListener('resize', this.handleResize, { passive: false })
    this.handleResize()
  },

  destroyed() {},

};
</script>

<style scoped>
.splide >>> .splide__arrow {
  background-color: transparent;
}
.splide >>> .splide__arrow svg {
  fill: #E82817;
}
.splide >>> .splide__arrow--prev {
  left: -.5rem;
}
.splide >>> .splide__arrow--prev:disabled {
  opacity: .2;
}
.splide >>> .splide__arrow--next {
  right: -.5rem;
}
.splide >>> .splide__arrow--next:disabled {
  opacity: .2;
}
@media screen and (max-width: 767px) {
  .splide >>> .splide__arrows {
    display: none;
  }
}
</style>
