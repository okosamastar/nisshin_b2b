<template>
  <div class="">
    <div class="tags max-w-2xl mx-auto mt-10 bg-gray-100 sm:flex justify-start">
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
    <div ref="cont" class="mt-8 md:mt-14">
      <slot></slot>
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
  },

  data() {
    return {
      currentIndex: 1,
    }
  },

  methods: {
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
    }
  },

  mounted() {
    this.switchContent(1)
  }
}
</script>

<style scoped>

</style>
