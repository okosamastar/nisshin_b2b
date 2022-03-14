<template>
  <div class="flex flex-row justify-center items-center text-gray-700">
    <social-sharing
      :title="title"
      :description="description"
      :quote="description"
      hashtags=""
      twitter-user="GOOUTmagazine"
      inline-template
    >
      <div class="flex justify-center items-center">
        <network network="twitter">
          <div class="mx-2 md:mx-4 cursor-pointer leading-none"><icon-base width="22" height="22" icon-name="twitter" icon-color="#55acee"></icon-base></div>
        </network>
        <network network="facebook">
          <div class="mx-2 md:mx-4 cursor-pointer leading-none"><icon-base width="22" height="22" icon-name="facebook" icon-color="#3b5999"></icon-base></div>
        </network>
        <network network="line">
          <div class="mx-2 md:mx-4 cursor-pointer leading-none"><icon-base width="22" height="22" icon-name="line" icon-color="#00c300"></icon-base></div>
        </network>
      </div>
    </social-sharing>
  </div>
</template>

<script>
import SocialSharing from 'vue-social-sharing'

export default {

  props: {
    title: {
      type: String,
      default: function() {
        return ''
      }
    },
    description: {
      type: String,
      default: function() {
        return ''
      }
    },
  },

  components: {
    SocialSharing,
  }
}
</script>
