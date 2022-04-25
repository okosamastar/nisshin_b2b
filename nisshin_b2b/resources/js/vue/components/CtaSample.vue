<template>
  <a v-if="active" href="https://secure-link.jp/wf/?c=wf14875648" target="_blank" class="block w-full bg-green-50 p-3 md:p-4 mb-6 md:mb-0 hover:text-white no-hover-svg flex flex-wrap items-center hover:opacity-70">
    <div class="flex-1 w-full sm:w-auto flex justify-center md:justify-start items-center">
      <div class="flex-none w-8 h-8 md:w-10 md:h-10 bg-green-700 rounded-full flex justify-center items-center">
        <svg-vue icon="foodie" class="w-5 h-5 md:w-6 md:h-6 text-white"></svg-vue>
      </div>
      <p class="text-sm sm:text-base lg:text-lg md:text-base lg:text-lg leading-relaxed ml-2 text-black text-left">
        <span class="text-green-700 font-bold tracking-tight">この商品の無料サンプルをご用意！</span>
      </p>
    </div>
    <div class="flex-none w-full md:w-auto bg-white py-2 px-3 mt-2 md:mt-0 flex flex-col md:flex-row justify-between items-center">
      <div class="flex justify-center items-center">
        <span class="font-bold text-green-700">お申込みはこちら</span>
        <div class="w-8 h-8 ml-2 bg-green-700 flex justify-center items-center">
          <svg-vue icon="arrow" class="w-6 h-3 text-white"></svg-vue>
        </div>
      </div>
    </div>
  </a>
</template>

<script>

export default {

  props: {
    active: {
      type: Boolean,
      default: function() {
        return true
      }
    },
  },

  components: {

  }
}
</script>
