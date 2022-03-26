<template>
  <div class="w-full">
    <div class="md:flex flex-wrap justify-start items-start" :class="{'flex-row-reverse -mx-1' : layout==='row'}">
      <div class="flex-1 overflow-x-hidden md:px-1">
        <div class="relative border border-solid border-gray-300 aspect-h-1 aspect-y-1">
          <Splide ref="splide" :options="options">
            <SplideSlide v-for="(image, index) in images" v-bind:key="image.src">
              <div class="wrap-image">
                <img :src="image.src" :alt="image.title" class="mx-auto cursor-pointer" @click="magnify(index)">
              </div>
            </SplideSlide>
          </Splide>
          <div v-if="newmark" class="absolute left-0 top-0 mx-2 w-16 h-16">
            <img :src="imagePath + 'badge_new.png'" alt="NEW" class="no-effect">
          </div>
        </div>
      </div>
      <div :class="layout==='row'? 'hidden md:block flex-none w-[5.625rem] md:px-1' : 'flex flex-wrap mt-2 -mx-1 md:px-1'">
        <div
            v-for="(image, index) in images"
            :key="image.src"
            @click="showSlide(index)"
            class="flex justify-center items-center cursor-pointer mb-2"
            :class="{'w-1/4 px-1': layout==='col'}"
        >
          <div class="wrap-image border border-solid border-gray-300">
            <img :src="image.src" :alt="image.title">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  props: {
    images: {
      type: Array,
      default: []
    },
    layout: {
      type: String,
      default: 'row'
    },
    newmark: {
      type: Boolean,
      default: false
    },
    handleModal: {
      type: Function,
      required: true
    }
  },

  data() {
    return {
      imagePath: this.$imagePath,
      options: {
        type: 'loop',
        perPage: 1,
        arrows: true,
        pagination: false,
        breakpoints: {
          543: {

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
      },
    }
  },

  components: {
  },

  methods: {
    showSlide: function (index) {
      this.$refs.splide.go(index)
    },
    magnify: function (index) {
      const media = []
      for(let i=0; i < this.images.length; i++) {
        media[i] = {...this.images[i], type: 'image', caption: this.images[i].title };
      }
      this.handleModal(index, media)
    }
  },

  mounted() {
  },

  destroyed() {
  },

};
</script>

<style scoped>
.splide >>> .splide__arrow svg {
  width: 1rem;
  height: 1rem;
}
@media (min-width: 992px) {
  .splide >>> .splide__arrows {
    display: none;
  }
}
</style>
