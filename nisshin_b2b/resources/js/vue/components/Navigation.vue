<template>
  <div class="relative h-20 overflow-visible">
    <div id="site-nav" class="relative z-20 w-full bg-white md:flex justify-between items-center">
      <div class="relative z-10 w-full md:w-auto h-20 px-4 md:px-6 flex items-center bg-white">
        <a href="https://www.nisshin-seifun-welna.com/index/">
          <svg-vue icon="logo_welna" class="w-32 md:w-36 h-12"></svg-vue>
        </a>
      </div>
      <div v-if="isVisible" class="flex">
        <aside
          id="menus"
          class="absolute left-0 top-20 md:relative md:flex items-center w-full md:w-auto h-20 text-sm md:px-4 md:-mx-4 shadow-lg md:shadow-none"
          :class="{'is_active': isActive}"
        >
          <slot></slot>
        </aside>
        <div
          ref="humberger"
          class="md:hidden absolute right-0 top-0 z-30 md:relative md:w-22 h-20 md:h-full md:border-l border-crimson flex justify-center items-center cursor-pointer"
          @click="toggle"
        >
          <div class="flex flex-col justify-between items-end w-14 h-14 p-4">
            <span aria-hidden="true" class="w-full h-0.5 my-0.5 bg-black rounded transform transition duration-500 ease-in-out" :class="{'rotate-45 translate-y-[0.55rem]': isActive }"></span>
            <span aria-hidden="true" class="w-full h-0.5 my-0.5 bg-black rounded transform transition duration-500 ease-in-out" :class="{'-rotate-45': isActive }"></span>
            <span aria-hidden="true" class="w-1/2 h-0.5 my-0.5 bg-black rounded transform transition duration-500 ease-in-out" :class="{'opacity-0': isActive }"></span>
          </div>
        </div>
      </div>
    </div>
    <transition name="fade">
      <div v-show="isActive" class="overlay" ref="overlay" @click="toggle"></div>
    </transition>
  </div>
</template>

<script>

export default {

  props: {
  },

  components: {
  },

  data() {
    return {
      isActive: false,
      isVisible: false,
    }
  },

  methods: {
    toggle: function () {
      if(this.isActive) {
        this.unlock()
      } else {
        this.lock()
      }
      this.isActive = !this.isActive
    },
    lock: function (){
      document.querySelector("html").style.scrollBehavior = "unset"
      const scrollY = window.scrollY;
      const body = document.body;
      body.style.position = 'fixed';
      body.style.top = `-${scrollY}px`;
    },
    unlock: function () {
      const body = document.body;
      const scrollY = body.style.top;
      body.style.position = '';
      body.style.top = '';
      window.scrollTo(0, parseInt(scrollY || '0') * -1);
      document.querySelector("html").style.scrollBehavior = "smooth"
    },
  },

  mounted() {
    this.isVisible = true
  }
}
</script>

<style scoped>
div.overlay {
  position: fixed;
  left: 0;
  bottom: 0;
  background: rgba(11, 10, 12, 0.5);
  width: 100%;
  height: 100%;
  z-index: 10;
}
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
