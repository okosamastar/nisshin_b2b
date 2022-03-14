<template>
  <video muted loop autoPlay controls preload="auto" data-setup='{}' ref="videoPlayer" class="video-js"></video>
</template>

<script>
import videojs from 'video.js';
import "video.js/dist/video-js.css"

export default {
  props: {
    options: {
      type: Object,
      default: {
        'muted': true,
        'controls': false,
        'autoplay': true,
        'preload': 'auto',
      }
    }
  },
  data() {
    return {
      player: null
    }
  },
  mounted() {
    this.player = videojs(this.$refs.videoPlayer, this.options, function onPlayerReady() {
      console.log('onPlayerReady', this)
    })
  },
  beforeDestroy() {
    if (this.player) {
      this.player.dispose()
    }
  }
}
</script>

<style scoped>
.video-js >>> .vjs-big-play-button {
  line-height: 2em;
  height: 2em;
  width: 2em;
  top: 50%;
  left: 50%;
  border-radius: 50%;
  margin-left: -1em;
  margin-top: -1em;
  border: none;
}
</style >
