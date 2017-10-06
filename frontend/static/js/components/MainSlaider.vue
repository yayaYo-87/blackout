<template>
    <div class="main__slider">
        <swiper :options="swiperOption">
            <swiper-slide>
                <div class="slider">
                    <img class="slider__img" src="/static/img/project1.jpg">
                    <div class="slider__text">
                        <div class="slider__text-title">Сергей Лазарев. Тур «The Best»</div>
                        <div class="slider__text-desc">Минск стал 99-м городом, а Москва — 100-м тура Сергея Лазарева «The Best»!</div>
                    </div>
                </div>
            </swiper-slide>
            <swiper-slide>
                <div class="slider">
                    <img class="slider__img" src="/static/img/project1.jpg">
                    <div class="slider__text">
                        <div class="slider__text-title">Сергей Лазарев. Тур «The Best»</div>
                        <div class="slider__text-desc">Минск стал 99-м городом, а Москва — 100-м тура Сергея Лазарева «The Best»!</div>
                    </div>
                </div>
            </swiper-slide>
            <swiper-slide>
                <div class="slider">
                    <img class="slider__img" src="/static/img/project1.jpg">
                    <div class="slider__text">
                        <div class="slider__text-title">Сергей Лазарев. Тур «The Best»</div>
                        <div class="slider__text-desc">Минск стал 99-м городом, а Москва — 100-м тура Сергея Лазарева «The Best»!</div>
                    </div>
                </div>
            </swiper-slide>
            <div class="main__slider-prev" slot="button-prev"></div>
            <div class="main__slider-next" slot="button-next"></div>
        </swiper>
    </div>
</template>

<script>
  import Swiper from "../../../../node_modules/vue-awesome-swiper/src/swiper.vue";

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
          autoplay: 5000
        }
      }
    },
    mounted() {

    }
  }</script>