<template>
    <div class="main__header" v-if="result.length !== 0">
        <swiper :options="swiperOptionTop" class="main__header_swiperTop" ref="swiperTop">
            <swiper-slide :key="item.id"  v-for="item in result[0].top_sliders">
                <div class="main__header__swiper">
                    <img class="main__header__img" :src="item.cover">
                </div>
            </swiper-slide>
        </swiper>
        <div class="main__header-wrapper">
            <swiper :options="swiperOptionThumbs"  class="main__header_items" ref="swiperThumbs">
                <swiper-slide :key="cart.id" class="main__header_item" v-for="cart in result[0].top_sliders">
                    <div class="main__header_item-desc">{{ cart.description }}</div>
                    <div class="main__header_item-name">{{ cart.name }}</div>
                    <div class="main__header_item-icon" :style="`background-image: url('` + cart.ikon + `') `"></div>
                </swiper-slide>
            </swiper>
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
        swiperOptionTop: {
          notNextTick: true,
          autoplay: 4000,
          speed: 1000
        },
        swiperOptionThumbs: {
          notNextTick: true,
          centeredSlides: true,
          slidesPerView: 'auto',
          touchRatio: 0.2,
          slideToClickedSlide: true,
        },
        result: []
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
                const swiperTop = self.$refs.swiperTop.swiper;
                const swiperThumbs = self.$refs.swiperThumbs.swiper;
                swiperTop.params.control = swiperThumbs
                swiperThumbs.params.control = swiperTop
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