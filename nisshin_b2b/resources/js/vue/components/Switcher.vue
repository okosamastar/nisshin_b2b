<template>
  <div :id="baseName + '-list'">
    <div class="tags w-full md:w-9/12 mx-auto mt-10 bg-gray-100 sm:flex justify-start">
      <h3 class="py-2 px-4 sm:p-0 flex justify-center items-center sm:border-r border-dashed border-gray-300">
        <span class="px-4 text-sm font-en text-crimson tracking-wider font-bold uppercase">filter</span>
      </h3>
      <ul class="flex-1 p-2 sm:p-4 flex flex-wrap justify-center sm:justify-start items-center -mx-1">
        <li
            v-for="(group, index) in groups"
            :id="'btn-' + baseName + (index + 1)"
            :key="'btn-' + (index + 1)"
            class="inline-block m-1 py-2 px-4 bg-crimson text-xs md:text-sm font-bold rounded-full flex items-center"
            :class="currentIndex === (index + 1) ? 'bg-yellow text-black cursor-default' : 'bg-crimson text-white cursor-pointer'"
            @click="switchContent(index + 1)"
        >
          <span>{{ group.name }}</span>
          <div
            class="w-4 h-4 ml-1 -mr-1 text-2xs rounded-full bg-white flex justify-center items-center leading-none tracking-[0]"
            :class="currentIndex === (index + 1) ? 'text-black' : 'text-crimson '"
          >
            {{ group.count }}
          </div>
        </li>
      </ul>
    </div>
    <div ref="cont" class="mt-8 md:mt-14 overflow-hidden transition-height">
      <slot></slot>
    </div>
    <div
        v-if="defaultHeight < originalHeight"
        class="relative -mt-12 md:-mt-28 pt-18 md:pt-32 text-center"
        :class="isOpen ? '' : 'bg-transparent-to-white'"
    >
      <div class="p-8 bg-crimson-50 text-center">
        <button class="w-64 button py-4 mx-auto" @click="handleClick">
          <span class="font-bold">{{ buttonText }}</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Switcher",

  props: {
    baseName:{
      type: String,
      default: 'switcher'
    },
    groups: {
      type: Array,
      default: []
    },
    defaultHeight: {
      type: Number,
      default: 640
    }
  },

  data() {
    return {
      currentWidth: window.innerWidth,
      originalHeight: 0,
      targetHeight: this.defaultHeight,
      currentIndex: 1,
      buttonText: 'VIEW MORE',
      isOpen: false
    }
  },

  methods: {
    handleResize: function () {
      if (this.$isMobile() && this.currentWidth === window.innerWidth) {
        return;
      }
      this.switchContent(this.currentIndex)
    },
    switchContent: function(num) {
      for (let i = 1; i < this.groups.length + 1; i++) {
        const elm = document.getElementById(this.baseName + i )
        if (elm && i === num) {
          elm.classList.remove('hidden')
          this.currentIndex = i
        } else {
          elm.classList.add('hidden')
        }
      }
      this.isOpen = true
      this.$nextTick(function (){
        this.$refs.cont.style.height = null;
        this.originalHeight = this.$refs.cont.offsetHeight
        this.setContainerHeight()
      })
    },
    handleClick: function () {
      if(this.buttonText === 'VIEW LESS') {
        this.$nextTick(function (){
          this.scrollTo('#' + this.baseName + '-list')
        })
      }
      this.setContainerHeight()
    },
    setContainerHeight: function () {
      if (this.originalHeight > this.defaultHeight) {
          this.isOpen = !this.isOpen
          this.buttonText = this.isOpen ? 'VIEW LESS' : 'VIEW MORE'
          this.targetHeight = this.isOpen ? this.originalHeight : this.defaultHeight
          this.$refs.cont.style.height = this.targetHeight + 'px'
      }
    },
    scrollTo: function (id) {
      const target = document.querySelector(id)
      const duration = 500
      const options = {
        offset: this.isMobile ? -(48 + 127):-(64 + 140),//add global menu height
        onDone: undefined,
        onCancel: undefined,
      }
      this.$scrollTo(target, duration, options)
    },
  },

  mounted() {
    window.addEventListener("resize", _.throttle(this.handleResize, 250), {
      passive: false,
    });
    this.switchContent(this.currentIndex)
  }
}
</script>

<style scoped>

</style>
