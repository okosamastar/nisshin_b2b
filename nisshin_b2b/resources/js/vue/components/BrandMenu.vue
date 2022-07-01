<template>
  <div class="md:relative z-100 w-1/2 md:w-full">
    <div id="brand-menu" ref="brand-menu" class="no-hover-svg" :class="{open: isOpen}">
      <div class="flex md:block justify-center items-center cursor-pointer" @click="toggleMenu">
        <div class="toggle-icon md:pt-1 px-3 md:mb-2">
          <span class="block w-6 h-[0.2rem] bg-white"></span>
          <span class="block w-6 h-[0.2rem] mt-[0.26rem] bg-white"></span>
          <span class="block w-6 h-[0.2rem] mt-[0.26rem] bg-white"></span>
        </div>
        <div class="menu-text">
          <img :src="static + 'images/brands/mama_the_pro/text-brand_menu.png'" alt="MENU">
        </div>
      </div>
      <slot></slot>
    </div>
  </div>
</template>

<script>

export default {
  props: {
    static: {
      type: String,
      default: ''
    },
  },

  data() {
    return {
      isOpen: false
    }
  },

  components: {

  },

  methods: {
    toggleMenu: function() {
      this.isOpen = !this.isOpen
    }
  },

  created() {
  },

  mounted() {

  },

  destroyed() {},

};
</script>

<style scoped>
</style>
