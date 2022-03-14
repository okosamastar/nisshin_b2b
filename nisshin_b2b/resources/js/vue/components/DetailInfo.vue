<template>
  <div class="relative">
    <details ref="detail">
      <summary class="py-7 shadow-inner cursor-pointer text-center outline-none">
        <div class="absolute inset-x-0 sm:right-0 top-0 z-20 w-full flex justify-center sm:justify-end">
          <div class="w-8/12 sm:w-4/12 md:w-3/12 p-4 flex justify-center items-center bg-white shadow hover:shadow-lg" @click="isOpened=!isOpened">
            <span class="text-xl text-crimson font-bold">詳細情報を見る</span>
            <div class="flex-none w-7 h-7 ml-2 rounded-full bg-crimson flex justify-center items-center">
              <svg-vue icon="chevron_alt" class="w-3 h-3 transform text-white transition ease-in duration-150" :class="isOpened? '':'rotate-180 -mb-0.5'"/>
            </div>
          </div>
        </div>
        <div class="absolute bottom-0 left-0 z-10 w-full -mb-3 px-0.5 bg-gray-to-white">
          <div class="w-full h-full py-3 bg-white flex flex-col items-center">
            <span class="block mb-1.5 w-10 h-0.5 bg-gray-200 opacity-75"></span>
            <span class="block mb-1 w-10 h-0.5 bg-gray-200 opacity-75"></span>
          </div>
        </div>
      </summary>
      <div class="px-4 pt-0 pb-12 sm:px-10 sm:pb-16 mt-6">
        <div class="bg-white shadow p-4 sm:p-8">
          <div class="sm:flex sm:-mx-2">
            <div class="w-full sm:w-3/12 sm:px-2">
              <div class="h-full p-4 bg-gray-100">
                <h4 class="w-full text-crimson font-bold">調理設備</h4>
                <div class="flex flex-wrap -mx-1">
                  <div v-for="facility in facilities" :key="facility" class="w-full md:w-1/2 px-1 mt-3">
                    <div class="flex flex-col items-center bg-white text-center">
                      <svg-vue :icon="facility" class="w-16 h-16 pt-3 text-crimson mx-auto"></svg-vue>
                      <span class="block pt-2 pb-4 text-sm font-bold text-crimson">{{ trans[facility] }}</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="w-full sm:w-9/12 sm:px-2">
              <div class="h-full p-4 bg-gray-100 mt-3 sm:mt-0">
                <h4 class="w-full text-crimson font-bold">調理条件</h4>
                <div class="sm:flex flex-wrap sm:-mx-1">
                  <div v-for="condition in conditions" :key="condition.title" class="w-full sm:w-1/2 md:w-1/3 sm:px-1 mt-3">
                    <div class="flex justify-between items-center bg-white">
                      <div class="w-20 flex flex-col items-center bg-crimson text-center">
                        <svg-vue :icon="condition.title" class="w-16 h-16 pt-4 text-white mx-auto"></svg-vue>
                        <span class="block pt-2 pb-4 text-sm font-bold text-white">{{ trans[condition.title] }}</span>
                      </div>
                      <div class="flex-1 text-sm text-center text-crimson font-bold" v-html="condition.value"></div>
                    </div>
                  </div>
                  <div v-if="extra_a" class="sm:w-2/3 sm:px-1 mt-3">
                    <div class="sm:h-full flex">
                      <div class="">
                        <div class="w-20 h-full flex justify-center items-center bg-crimson text-center">
                          <span class="block text-sm font-bold text-white">ご参考</span>
                        </div>
                      </div>
                      <div class="flex justify-center items-center">
                        <svg-vue icon="triangle" class="w-3 h-4 text-crimson"></svg-vue>
                      </div>
                      <div class="flex-1 flex items-center">
                        <div class="py-4 pl-4 text-xs" v-html="extra_a.text"></div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div v-if="extra_c" class="w-full mt-4">
            <div class="flex items-center">
              <a :href="extra_c.url" class="text-xs text-crimson font-bold underline hover:no-underline"
                 v-html="extra_c.text"></a>
              <a :href="extra_c.url">
                <svg-vue icon="chevron" class="w-3 h-3 ml-2 text-crimson"></svg-vue>
              </a>
            </div>
          </div>
          <div class="w-full mt-4">
            <div class="bg-gray-100 p-4 pb-3">
              <h4 class="w-full mb-3 text-crimson font-bold">商品規格</h4>
              <div class="sm:flex flex-wrap sm:-mx-4">
                <div class="w-full sm:w-1/2 md:w-1/3 sm:px-4">
                  <dl class="flex flex-wrap items-start">
                    <template v-for="spec in specs_a">
                      <dt class="w-5/12 py-1 px-1 mb-1 text-xs font-bold bg-white" :key="spec.title">
                        <span class="block border-l-4 border-solid border-crimson px-2">{{ spec.title }}</span>
                      </dt>
                      <dd class="w-7/12 py-1 pl-3 mb-1 text-xs" v-html="spec.value"></dd>
                    </template>
                  </dl>
                </div>
                <div class="w-full sm:w-1/2 md:w-1/3 sm:px-4 md:border-l border-dashed border-gray-300">
                  <dl class="flex flex-wrap items-start">
                    <template v-for="spec in specs_b">
                      <dt class="w-5/12 py-1 px-1 mb-1 text-xs font-bold bg-white" :key="spec.title">
                        <span class="block border-l-4 border-solid border-crimson px-2">{{ spec.title }}</span>
                      </dt>
                      <dd class="w-7/12 py-1 pl-3 mb-1 text-xs" v-html="spec.value"></dd>
                    </template>
                  </dl>
                </div>
                <div class="w-full sm:w-1/2 md:w-1/3 sm:px-4 md:border-l border-dashed border-gray-300">
                  <dl class="flex flex-wrap justify-start items-start">
                    <template v-for="spec in specs_c">
                      <dt class="w-5/12 py-1 px-1 mb-1 text-xs font-bold bg-white" :key="spec.title">
                        <span class="block border-l-4 border-solid border-crimson px-2">{{ spec.title }}</span>
                      </dt>
                      <dd class="w-7/12 py-1 pl-3 mb-1 text-xs" v-html="spec.value"></dd>
                    </template>
                  </dl>
                </div>
              </div>
            </div>

            <div v-if="extra_b" class="extra_block flex-1 mt-4 px-4 border-l-3 border-solid border-crimson">
              <h5>
                <span class="text-crimson font-bold text-sm">{{ extra_b.title }}</span>
                <span class="ml-2 text-xs font-normal">{{ extra_b.subtitle }}</span>
              </h5>
              <div class="pt-2 text-xs" v-html="extra_b.text"></div>
            </div>

          </div>
        </div>
      </div>
    </details>
  </div>
</template>

<script>
import _ from "lodash";

export default {
  props: {
    facilities: {
      type: Array,
      default: []
    },
    conditions: {
      type: Array,
      default: []
    },
    specs_a: {
      type: Array,
      default: []
    },
    specs_b: {
      type: Array,
      default: []
    },
    specs_c: {
      type: Array,
      default: []
    },
    extra_a: {
      type: Object,
      default: null
    },
    extra_b: {
      type: Object,
      default: null
    },
    extra_c: {
      type: Object,
      default: null
    }
  },

  data() {
    return {
      isOpened: false,
      trans: {
        'boil': 'ボイル',
        'steam': 'スチーム',
        'bake': 'ベイク',
        'fry': 'フライ',
        'microwave': 'レンジ',
        'water': '加水',
        'time': '時間',
        'temp': '温度',
      }
    }
  },

  components: {},

  methods: {
    handleResize: function () {
      // console.log('yay! resized')
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
      this.setHeight(detail, true);
      detail.open = false;

      // const RO = new ResizeObserver(entries => {
      //   return entries.forEach(entry => {
      //     const detail = entry.target;
      //     const width = parseInt(detail.dataset.width, 10);
      //     if (width !== entry.contentRect.width) {
      //       detail.removeAttribute('style');
      //       this.setHeight(detail);
      //       this.setHeight(detail, true);
      //       detail.open = false;
      //     }
      //   })
      // });
      // RO.observe(detail);
    }
  },

  mounted() {
    window.addEventListener("resize", _.throttle(this.handleResize, 250), {
      passive: false,
    });
    this.handleResize();
  },

  destroyed() {
  },

};
</script>
