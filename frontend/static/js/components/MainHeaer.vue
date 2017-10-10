<template>
    <div class="main__header" >
        <swiper :options="swiperOptionTop" class="main__header_swiperTop" ref="swiperTop">
            <swiper-slide>
                <div class="main__header__swiper">
                    <img class="main__header__img" src="/static/img/header123.jpg">
                </div>
            </swiper-slide>
            <swiper-slide>
                <div class="main__header__swiper">
                    <img class="main__header__img" src="/static/img/header123.jpg">
                </div>
            </swiper-slide>
            <swiper-slide>
                <div class="main__header__swiper">
                    <img class="main__header__img" src="/static/img/header123.jpg">
                </div>
            </swiper-slide>
            <swiper-slide>
                <div class="main__header__swiper">
                    <img class="main__header__img" src="/static/img/header123.jpg">
                </div>
            </swiper-slide>
        </swiper>
        <div class="main__header-wrapper">
            <swiper :options="swiperOptionThumbs"  class="main__header_items" ref="swiperThumbs">
                <swiper-slide class="main__header_item">
                    <div class="main__header_item-desc">Световое оборудование</div>
                    <div class="main__header_item-name">Безграничная яркость</div>
                    <div class="main__header_item-icon" style="background: url('/static/img/icon123.svg') no-repeat"></div>
                </swiper-slide>
                <swiper-slide class="main__header_item">
                    <div class="main__header_item-desc">Световое оборудование</div>
                    <div class="main__header_item-name">Безграничная яркость</div>
                    <div class="main__header_item-icon"  style="background: url('/static/img/icon123.svg') no-repeat"></div>
                </swiper-slide>
                <swiper-slide class="main__header_item">
                    <div class="main__header_item-desc">Световое оборудование</div>
                    <div class="main__header_item-name">Безграничная яркость</div>
                    <div class="main__header_item-icon"  style="background: url('/static/img/icon123.svg') no-repeat"></div>
                </swiper-slide>
                <swiper-slide class="main__header_item">
                    <div class="main__header_item-desc">Световое оборудование</div>
                    <div class="main__header_item-name">Безграничная яркость</div>
                    <div class="main__header_item-icon"  style="background: url('/static/img/icon123.svg') no-repeat"></div>
                </swiper-slide>
            </swiper>
        </div>
    </div>
</template>

<script>
  import SwiperSlide from "../../../../node_modules/vue-awesome-swiper/src/slide.vue";

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

        }

      }
    },
    mounted() {
      const swiperTop = this.$refs.swiperTop.swiper
      const swiperThumbs = this.$refs.swiperThumbs.swiper
      swiperTop.params.control = swiperThumbs
      swiperThumbs.params.control = swiperTop
    }
  }
</script>