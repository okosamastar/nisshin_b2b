<template>
  <div class="md:relative z-100 w-1/2 h-12 md:w-full md:h-16 border-t border-green md:border-none">
    <div id="brand-menu" ref="brandMenu" class="no-hover-svg" :class="{open: isOpen}">
      <div class="menu-title" @click="(event) => handleClick(event)">
        <div class="toggle-icon">
          <span class="block w-6 h-[0.2rem] bg-white"></span>
          <span class="block w-6 h-[0.2rem] mt-[0.26rem] bg-white"></span>
          <span class="block w-6 h-[0.2rem] mt-[0.26rem] bg-white"></span>
        </div>
        <div class="menu-text">
          <img :src="static + 'brands/text-page_menu.png'" alt="MENU">
        </div>
      </div>
      <div ref="menuList" class="menu-list mt-6">
        <slot></slot>
      </div>
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
      menuList: null,
      isOpen: false,
      listHeight: 0,
    }
  },

  components: {

  },

  methods: {
    handleClick: function(event) {
      event.stopPropagation();
      this.toggleMenu()
    },
    handleResize: function() {
      if(window.innerWidth < 992) {
        if(this.isOpen) {
          this.$refs.brandMenu.style.transform = "translate(0, -" + (this.listHeight + 90) + "px)"
        } else {
          this.$refs.brandMenu.style.transform = null
        }
      }else {
        this.$refs.brandMenu.style.transform = null
      }
    },
    toggleMenu: function() {
      this.isOpen = !this.isOpen
      this.handleResize()
    }
  },

  created() {
  },

  mounted() {
    window.addEventListener("resize", _.throttle(this.handleResize, 250), {
      passive: false,
    });
    window.addEventListener("click", () => {
      if(this.isOpen) this.toggleMenu()
    });
    this.$refs.menuList.querySelector('ul').classList.remove('hidden')
    this.listHeight = this.$refs.menuList.offsetHeight
  },

  destroyed() {},

};
</script>

<style scoped>
</style>
