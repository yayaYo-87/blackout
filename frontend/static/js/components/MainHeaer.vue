<template>
    <div class="main__header" v-if="result.length !== 0">
        <div  class="main__header_swiperTop">
            <video muted="muted" loop="loop" autoplay="autoplay" id="myVideo">
                <source src="/static/img/video.mp4" type='video/mp4'>
                <source src="/static/img/video.webm" type='video/webm'>
            </video>
        </div>
        <div class="main__header-wrapper">
            <div  class="main__header_items">
                <a :href="cart.link" :key="cart.id" class="main__header_item" v-for="cart in result[0].top_sliders">
                    <div class="main__header_item-desc">{{ cart.description }}</div>
                    <div class="main__header_item-name">{{ cart.name }}</div>
                    <div class="main__header_item-icon" :style="`background-image: url('` + cart.ikon + `') `"></div>
                </a>
            </div>
        </div>
    </div>
</template>

<script>
  import SwiperSlide from "../../../../node_modules/vue-awesome-swiper/src/slide.vue";
  import axios from 'axios'
  export default {
    components: {SwiperSlide},
    data() {
      return {
        result: [],
      }
    },
    methods: {
      get() {
        let self = this
        axios.get('/api/top_sliders/')
          .then(
            (response) => {
              self.result = response.data;
              setTimeout(function () {
                self.$store.dispatch('loader', { value: false })
              }, 1000)

            },
            function (error) {
              console.log(error)
              self.$store.dispatch('loader', { value: false })
            }
          )
      }
    },
    mounted() {
    },
    created() {
      this.get()
    }
  }
</script>