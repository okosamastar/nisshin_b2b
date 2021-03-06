<template>
  <Splide ref="splide" :options="options" class="sm:px-8">
    <SplideSlide v-for="product in products" v-bind:key="product.url" class="wrap-image splide__slide" :class="product.class? product.class : ''">
      <div class="h-full">
        <a :href="product.link" class="h-full flex flex-col justify-between border border-solid border-gray-300 bg-white">
          <div class="relative aspect-w-4 aspect-h-3 border-b border-dashed border-gray-300">
            <div v-if="product.image" class="py-3 overflow-hidden bg-white">
              <img :src="product.image" :alt="product.title" class="w-auto h-full mx-auto">
            </div>
            <div v-else class="py-1 overflow-hidden bg-gray-100">
              <img :src="product.staticpath + 'default_thumbnail.png'" :alt="product.title" class="w-auto h-full mx-auto">
            </div>
            <div v-if="product.newmark" class="absolute left-0 top-0 w-12 h-12 mx-2">
              <img :src="imagePath + 'badge_new.png'" alt="New" class="no-effect">
            </div>
            <div v-if="product.preservation" class="absolute left-auto right-0 top-auto bottom-0 w-9 h-9 m-2">
              <img :src="imagePath + 'badge_' + product.preservation + '_mini.png'" alt="New" class="no-effect">
            </div>
          </div>
          <h4 class="flex-1 p-4 font-bold flex flex-col justify-start items-start">
            <span v-if="product.category" class="p-1 mb-2 text-xs border border-crimson text-crimson leading-none">{{ product.category }}</span>
            <span class="">{{ product.title }}</span>
          </h4>
          <dl class="pt-2 px-2 flex flex-wrap items-start bg-gray-100 text-black">
            <dt class="w-6/12 py-1 px-1 mb-1 text-xs font-bold bg-white">
              <span class="block border-l-4 border-solid border-crimson px-2">荷姿</span>
            </dt>
            <dd class="w-6/12 py-1 pl-3 mb-1 text-xs">{{ product.weight }}</dd>
            <dt class="w-6/12 py-1 px-1 mb-2 text-xs font-bold bg-white">
              <span class="block border-l-4 border-solid border-crimson px-2">マークコード</span>
            </dt>
            <dd class="w-6/12 pt-1 pl-3 text-xs">{{ product.code }}</dd>
          </dl>
        </a>
      </div>
    </SplideSlide>
  </Splide>
</template>

<script>

export default {
  props: {
    products: {
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
      if(!this.isMobile && this.products.length < 5) {
        splideList.classList.add('justify-center')
      } else {
        splideList.classList.remove('justify-center')
      }
    },
  },

  created() {
    if(!this.isMobile && this.products.length < 5) {
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
