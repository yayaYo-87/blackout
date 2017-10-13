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
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c7.png" alt="tape">
                </swiper-slide>
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c8.png" alt="tape">
                </swiper-slide>
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c9.png" alt="tape">
                </swiper-slide>
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c10.png" alt="tape">
                </swiper-slide>
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c12.png" alt="tape">
                </swiper-slide>
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c13.png" alt="tape">
                </swiper-slide>
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c14.png" alt="tape">
                </swiper-slide>
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c15.png" alt="tape">
                </swiper-slide>
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c16.png" alt="tape">
                </swiper-slide>
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c17.png" alt="tape">
                </swiper-slide>
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c18.png" alt="tape">
                </swiper-slide>
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c19.png" alt="tape">
                </swiper-slide>
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c20.png" alt="tape">
                </swiper-slide>
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c21.png" alt="tape">
                </swiper-slide>
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c22.png" alt="tape">
                </swiper-slide>
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c23.png" alt="tape">
                </swiper-slide>
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c24.png" alt="tape">
                </swiper-slide>
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c25.png" alt="tape">
                </swiper-slide>
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c26.png" alt="tape">
                </swiper-slide>
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c27.png" alt="tape">
                </swiper-slide>
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c28.png" alt="tape">
                </swiper-slide>
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c29.png" alt="tape">
                </swiper-slide>
                <swiper-slide class="main__client_item">
                    <img src="/static/img/client/c30.png" alt="tape">
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
          loop: true,
          autoplay: 1000,
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