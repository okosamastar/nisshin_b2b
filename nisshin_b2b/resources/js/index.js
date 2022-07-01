import Vue from 'vue'
import VueLazyLoad from 'vue-lazyload'
import VueYouTubeEmbed from 'vue-youtube-embed'
import AOS from 'aos'
import 'aos/dist/aos.css'
import SvgVue from 'svg-vue'
import CoolLightBox from 'vue-cool-lightbox'
import 'vue-cool-lightbox/dist/vue-cool-lightbox.min.css'
import VueSplide from '@splidejs/vue-splide';
import '@splidejs/splide/dist/css/splide.min.css';
import inView from "in-view";
import ScrollHint from 'scroll-hint';
import 'scroll-hint/css/scroll-hint.css';
import _ from "lodash";

const VueScrollTo = require('vue-scrollto');

// import Share from './vue/components/Share.vue'
import Navigation from "./vue/components/Navigation.vue";
import Hero from './vue/components/Hero.vue'
import DetailSlider from './vue/components/DetailSlider.vue'
import DetailInfo from './vue/components/DetailInfo.vue'
import CardSlider from './vue/components/CardSlider.vue'
import ImageSlider from './vue/components/ImageSlider.vue'
import VideoPlayer from "./vue/components/VideoPlayer.vue";
import CtaSample from "./vue/components/CtaSample.vue";
import BrandMenu from "./vue/components/BrandMenu.vue";

Vue.use(VueScrollTo);
Vue.use(VueYouTubeEmbed)
Vue.use( VueSplide );
Vue.use(SvgVue);
Vue.use(VueLazyLoad)

new Vue({
  el: '#app',
  props: {
    imagepath: {
      type: String,
      default: function() {
        return ''
      }
    },
  },
  components: {
    // Share,
    Navigation,
    Hero,
    DetailSlider,
    CardSlider,
    DetailInfo,
    ImageSlider,
    CoolLightBox,
    VideoPlayer,
    CtaSample,
    BrandMenu,
  },
  data() {
    return {
      isMobile: false,
      showModal: false,
      winHeight: null,
      imageUrl: null,
      showSideTab: false,
      media: [{}],
      mediaIndex: null,
      scrollY: 0,
      showModalOnLoad: true,
      showStickyMessage: false,
    }
  },
  methods: {
    getYear: function() {
      return new Date().getFullYear();
    },
    handleResize: function () {
      this.isMobile = window.innerWidth < 992
      inView.offset({ top: this.isMobile ? -800 : 0, bottom: this.isMobile ? -600 : 0 });
      const movie = this.$refs.b2bmovie
      if(movie){
        if(this.isMobile) {
          if(!movie.closest('#movie_sp_slot')){
            let dest = document.getElementById('movie_sp_slot')
            dest.appendChild(movie)
          }
        } else {
          if(!movie.closest('#movie_pc_slot')) {
            let dest = document.getElementById('movie_pc_slot')
            dest.appendChild(movie)
          }
        }
      }
    },
    handleKeydown: function (event) {
      if (event.keyCode === 27 && document.body.classList.contains('modal-active')) {
        this.imageUrl = null
        this.toggleModal()
      }
    },
    handleScroll: function (event) {
      const mainnav = this.$refs.mainnav;
      const footer  = document.getElementById("footer");
      const pagetop = document.getElementById("pagetop");
      const exhibition = document.getElementById('exhibition')

      const scrollElem = (function (doc) {
        if ("scrollingElement" in doc) {
          return doc.scrollingElement;
        }
        return doc.documentElement;
      })(document);

      const p = scrollElem.scrollTop;

      if(p < 150){
        mainnav.classList.remove("scrolled");
      } else if (p > this.scrollY) {
        mainnav.classList.add("scrolled")
      } else {
        if(!exhibition || inView.is(footer)){
          mainnav.classList.remove("scrolled")
        }
      }

      if (pagetop) {
        800 > p ? pagetop.classList.remove("show") : pagetop.classList.add("show");
      }

      this.scrollY = p;

      if(exhibition && this.isMobile){
        inView('#karaage').on('enter', (e)=>e.classList.add('in-view'))
        inView('#hayayude').on('enter', (e)=>e.classList.add('in-view')).on('exit', (e)=>e.classList.remove('in-view'))
        inView('#smilemeal').on('enter', (e)=>e.classList.add('in-view')).on('exit', (e)=>e.classList.remove('in-view'))
        inView('#iqf').on('enter', (e)=>e.classList.add('in-view')).on('exit', (e)=>e.classList.remove('in-view'))
        inView('#souzai').on('enter', (e)=>e.classList.add('in-view')).on('exit', (e)=>e.classList.remove('in-view'))
        inView('#tenpurako').on('enter', (e)=>e.classList.add('in-view')).on('exit', (e)=>e.classList.remove('in-view'))
      }
    },
    initModal: function () {
      // this.winHeight = window.innerHeight
      // this.$refs.modal.style.height = this.winHeight + "px"

      const openmodal = document.querySelectorAll('.modal-open')
      const self = this
      for (let i = 0; i < openmodal.length; i++) {
        openmodal[i].addEventListener('click', function(event){
          const img_url = event.target.closest('.modal-open').href
          self.imageUrl = img_url
          event.preventDefault()
          self.toggleModal()
        })
      }
      this.$refs.modalClose.addEventListener('click', () => {self.imageUrl = null; self.toggleModal()})
      this.$refs.modalContent.addEventListener('click', () => {self.imageUrl = null; self.toggleModal()})
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
    toggleModal: function () {
      const body = document.querySelector('body')
      this.showModal = !this.showModal
      body.classList.toggle('modal-active')
    },
    videoReady(event) {
      // console.log(event.target)
      this.player = event.target
    },
    videoEnd: function (event) {
      // console.log(event)
      this.handleClose()
    },
    heroVideoReady: function (event) {
      event.target.mute()
      event.target.playVideo()
    },
    heroVideoEnd: function (event) {
      event.target.playVideo()
    },
    playVideo: function (num, start, end) {
      const elm = this.$refs.modal
      const id = this['videoId' + num]
      elm.classList.add('is-active')
      this.player.clearVideo()
      this.player.loadVideoById({
        'videoId': id,
        'startSeconds': start,
        'endSeconds': end,
        'suggestedQuality': 'large'
      })
    },
    openLightBox: function (index, mediaArray) {
      console.log('called light box ', index)
      this.media = mediaArray
      this.mediaIndex = index
    },
    showVideoStream: function (url) {
      this.media = [
        {
          src: url,
          autoplay: true
        }
      ]
      this.mediaIndex = 0
    },
    showStickyNav: function (){
      this.$refs.exhibitnav.classList.add('scrolled')
    },
    hideStickyNav: function () {
      this.$refs.exhibitnav.classList.remove('scrolled')
    },
    hideIndicator: function (e) {
      e.currentTarget.classList.add('hidden');
    },
    hideModal: function(e) {
      this.showModalOnLoad = false
      this.showStickyMessage = true
    }
   },
  beforeCreate() {
    const mountEl = document.querySelector("#app");
    const dataSet = { ...mountEl.dataset }
    Vue.prototype.$imagePath = dataSet.imagepath
  },
  created () {
    AOS.init()
  },
  mounted() {
    window.addEventListener("resize", _.throttle(this.handleResize, 250), {
      passive: false,
    });
    window.addEventListener("scroll", _.throttle(this.handleScroll, 250), {
      passive: false,
    });
    window.addEventListener("keydown", _.throttle(this.handleKeydown, 250), {
      passive: false,
    });

    this.handleResize()
    this.handleScroll()

    inView('#products').on('enter', this.showStickyNav).on('exit', this.hideStickyNav)

    new ScrollHint('.js-scrollable', {
      i18n: {
        scrollable: 'スクロールできます'
      }
    });

  }
});
