<template>
  <div class="overflow-visible">
    <details :id="'collapsable_' + id_number" ref="detail" class="relative pb-16 overflow-visible" :class="{'md:pb-0': mobile_only}">
      <summary class="outline-none focus:outline-none focus:border-transparent">
        <div class="absolute bottom-0 left-0 w-full cursor-pointer" :class="{'md:hidden': mobile_only}">
          <div class="flex justify-center items-center w-full py-2 border border-crimson bg-white rounded shadow-md">
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
    id_number: {
      type: Number,
      default: 1
    },
    mobile_only: {
      type: Boolean,
      default: false
    },
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
      if(this.$isMobile()){
        if(this.currentWidth === window.innerWidth){
          return;
        }
        this.isOpen = this.initial_open
      } else {
        if(this.mobile_only) {
          this.isOpen = true
        } else {
          this.isOpen = this.initial_open
        }
      }
      this.currentWidth = window.innerWidth
      this.setDetailsHeight();
    },
    setHeight: (detail, open = false) => {
      detail.open = open;
      const rect = detail.getBoundingClientRect();
      detail.dataset.width = rect.width;
      detail.style.setProperty(open ? `--expanded` : `--collapsed`, `${rect.height}px`);
      console.log('set height to ' + rect.height)
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

    this.$refs.detail.addEventListener("toggle", function() {
      this.isOpen = this.$refs.detail.open
      if(!this.isOpen) {
        this.$nextTick(function (){
          this.$scrollTo (
              '#' + 'collapsable_' + this.id_number,
              650,
              {
                offset: this.$isMobile ? -(48 + 127):-(64 + 140),//add global menu height
                onDone: undefined,
                onCancel: undefined,
              }
          )
        })
      }
    }.bind(this))

    window.addEventListener("resize", _.throttle(this.handleResize, 250), {
      passive: false,
    });
    this.handleResize();
  },

  destroyed() {
  },
}
</script>

<style scoped>

</style>
