<template>
    <div class="main__client">
        <div class="main__client_wrapper">
            <div class="main__client_title">Наши клиенты</div>
            <swiper :options="swiperOption" class="main__client_items">
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c1.png" alt="tape">
                </swiper-slide>
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c2.png" alt="tape">
                </swiper-slide>
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c3.png" alt="tape">
                </swiper-slide>
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c4.png" alt="tape">
                </swiper-slide>
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c5.png" alt="tape">
                </swiper-slide>
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c6.png" alt="tape">
                </swiper-slide>
            </swiper>
        </div>
    </div>
</template>

<script>
  import Swiper from "../../../../node_modules/vue-awesome-swiper/src/swiper.vue";
  export default {
    data() {
      return {
        swiperOption: {
          spaceBetween: 40,
          slidesPerView: 8,
          paginationClickable: true,
          autoplay: 5000,
          speed: 1000,
        },
      }
    },
    components: {
      Swiper
    },
    methods: {

    },
    mounted() {
    }
  }
</script>