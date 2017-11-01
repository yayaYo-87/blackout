<template>
    <div class="project-item">
        <div class="project-item__wrapper" v-if="result.length !== 0">
            <div class="project-item__header">
                <router-link tag="div" :to="{ name: 'project' }" class="project-item__header_title">Проекты</router-link>
                <router-link tag="div" :to="{ name: 'projectCategory', params: { id: $route.params.id } }" class="project-item__header_name">Концерты</router-link>
                <div class="project-item__header_product">{{ result.name }}</div>
                <div class="project-item__header_date">{{ result.date }}</div>
            </div>
            <div class="project-item__video" v-if="videoId">
                <youtube :video-id="videoId" player-height="700" player-width="100%"  ></youtube>
            </div>
            <div class="project-item__desc">{{ result.description }}</div>
            <div class="project-item__slider">
                <swiper :options="swiperOption">
                    <swiper-slide :key="index" v-for="(item, index) in result.project_images">
                        <div class="project-item__swiper">
                            <img class="project-item__img" :src="item.image">
                        </div>
                    </swiper-slide>
                    <div class="project-item-prev" slot="button-prev"></div>
                    <div class="project-item-next" slot="button-next"></div>
                </swiper>
            </div>
            <div class="project-item__equipment" v-if="devisec">
                <div class="project-item__equipment-title">Оборудование</div>
                <div class="project-item__equipment_item"
                     v-if="cart.device && cart.device.length !== 0"
                     :key="index" v-for="(cart, index) in result.project_devices">
                    <div class="project-item__equipment_item-name">{{ cart.category.name }}</div>
                    <div class="project-item__equipment_item-link">
                        <router-link tag="span"  :to="{ name: 'catalogItem', params: {id: cart.category.slug, item: dev.id} }"  :key="index.id" v-for="(dev, index) in cart.device">{{ dev.name }},</router-link>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
  import Swiper from "../../../../node_modules/vue-awesome-swiper/src/swiper.vue";
  import axios from 'axios'
  export default {
    data() {
      return{
        swiperOption: {
          paginationClickable: true,
          nextButton: '.project-item-next',
          prevButton: '.project-item-prev',
          loop: true,
          pagination: '.swiper-pagination',
          grabCursor: true,
          slidesPerView: 'auto',
//          autoplay: 5000,
          speed: 1000,
          coverflow: {
            rotate: 50,
            stretch: 0,
            depth: 100,
            modifier: 1,
            slideShadows : true
          }
        },
        result: []
      }
    },
    computed: {
      videoId() {
        return null
      },
      devisec(){
        return this.result.project_devices.length !== 0
      }
    },
    methods: {
      get() {
        let self = this;
        const id = this.$route.params.item;
        axios.get('/api/project/' + id + '/')
          .then(
            function (response) {
              self.result = response.data
              self.$store.dispatch('loader', { value: false })
            },
            function (error) {
              console.log(error)
              self.$store.dispatch('loader', { value: false })
            }
          )
      }
    },
    components: {
      Swiper
    },
    created() {
      this.get()
    }
  }
</script>