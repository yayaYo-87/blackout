<template>
    <div class="main__slider" v-if="result.length !== 0">
        <swiper :options="swiperOption">
            <swiper-slide  :key="item.id" v-for="item in result[0].bottom_sliders">
                <a :href="item.link" class="slider">
                    <img class="slider__img" :src="item.cover">
                    <div class="slider__text">
                        <div class="slider__text-title">{{item.name}}</div>
                        <div class="slider__text-desc">{{ item.description }}</div>
                    </div>
                </a>
            </swiper-slide>
            <div class="main__slider-prev" slot="button-prev"></div>
            <div class="main__slider-next" slot="button-next"></div>
        </swiper>
    </div>
</template>

<script>
  import Swiper from "../../../../node_modules/vue-awesome-swiper/src/swiper.vue";
  import axios from 'axios'
  export default {
    components: {
      Swiper
    },
    data () {
      return {
        swiperOption: {
          paginationClickable: true,
          nextButton: '.main__slider-next',
          prevButton: '.main__slider-prev',
          loop: true,
          autoplay: 5000,
          speed: 1000
        },
        result: []
      }
    },
    methods: {
      get() {
        let self = this
        axios.get('/api/bottom_sliders/')
          .then(
            (response) => {
              self.result = response.data;
            },
            function (error) {
              console.log(error)
            }
          )
      }

    },
    mounted() {
        this.get()
    }
  }</script>