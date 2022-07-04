<template>
  <div class="overflow-visible">
    <details ref="detail" class="relative pb-16 overflow-visible" :class="{'md:pb-0': mobile_only}">
      <summary>
        <div class="absolute bottom-0 left-0 w-full cursor-pointer" :class="{'md:hidden': mobile_only}">
          <div class="flex justify-center items-center w-full py-2  border border-crimson bg-white rounded shadow-md">
            <span class="text-crimson font-bold">{{ isOpen ? close_text : open_text }}</span>
            <div class="bg-crimson p-1 ml-2 rounded-sm">
              <svg-vue icon="chevron_alt" class="w-2 h-2 text-white" :class="{'rotate-180': !isOpen}"></svg-vue>
            </div>
          </div>
        </div>
      </summary>
      <div class="">
        <slot></slot>
      </div>
    </details>
  </div>
</template>

<script>
import _ from "lodash";

export default {
  name: "Collapsable",

  props: {
    initial_open: {
      type: Boolean,
      default: true
    },
    open_text: {
      type: String,
      default: 'OPEN'
    },
    close_text: {
      type: String,
      default: 'CLOSE'
    },
    mobile_only: {
      type: Boolean,
      default: false
    },
  },

  data() {
    return {
      currentWidth: window.innerWidth,
      isOpen: this.initial_open,
    }
  },

  components: {},

  methods: {
    handleResize: function () {
      if (this.$isMobile() && this.currentWidth === window.innerWidth) {
        return;
      }
      if(this.mobile_only && window.innerWidth >= 992) {
        this.isOpen = true
      } else {
        this.isOpen = this.initial_open
      }

      this.setDetailsHeight();
    },
    setHeight: (detail, open = false) => {
      detail.open = open;
      const rect = detail.getBoundingClientRect();
      detail.dataset.width = rect.width;
      detail.style.setProperty(open ? `--expanded` : `--collapsed`, `${rect.height}px`);

    },
    setDetailsHeight: function () {
      const detail = this.$refs.detail
      detail.removeAttribute('style');
      this.setHeight(detail);
      this.setHeight(detail,true);
      detail.open = this.isOpen;
    }
  },

  mounted() {
    window.addEventListener("resize", _.throttle(this.handleResize, 250), {
      passive: false,
    });
    this.handleResize();

    this.$refs.detail.addEventListener("toggle", function() {
      this.isOpen = this.$refs.detail.open
    }.bind(this))

    this.$refs.detail.open = this.isOpen

  },

  destroyed() {
  },
}
</script>

<style scoped>

</style>
