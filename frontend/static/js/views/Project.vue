<template>
    <div class="project">
        <div class="project__wrapper">
            <div class="project__header">
                <div class="project__header_title">Проекты</div>
            </div>
            <div class="project__recent">
                <div class="project__recent_title">Недавние</div>
                <div class="project__recent_items">
                    <router-link :to="{ name: 'projectItem', params: {  item: cart.id , id: cart.category.slug } }" class="project__recent_item" :key="cart.id" v-for=" cart in resent">
                        <div class="project__recent_item-img" :style="`background-image: url('` + cart.cover + `') ;`" ></div>
                        <div class="project__recent_item-wrapper">
                            <div class="project__recent_item-wrapper_title">{{ cart.name }}</div>
                            <div class="project__recent_item-wrapper-flex">
                                <div class="project__recent_item-wrapper-date">{{ cart.date }}</div>
                                <div class="project__recent_item-wrapper-desc">
                                    {{ cart.short_desc }}
                                </div>
                                <div class="project__recent_item-wrapper_link">
                                    Подробнее
                                </div>
                            </div>
                        </div>
                    </router-link>
                </div>
            </div>
            <div class="project__title">Все проекты</div>
            <div class="project__item" :key="item.id" v-for="item in result">
                <router-link tag="div" :to="{ name: 'projectCategory', params: { id: item.slug } }">
                    <div class="project__item-img" :style="`background-image: url('` + item.cover + `');`"></div>
                    <div class="project__item_text">
                        <div class="project__item_text-title">{{ item.name }}</div>
                        <!--<div class="project__item_text-desc">Телеканал Europa Plus TV открыл 2017 год жаркой вечеринкой на самой большой площадке страны! 20 февраля в Минска-Арене выступили известные исполнители со своими лучшими хитами:Мот, Willy William, Carla’s Dreams, Burak Yeter, Юлианна Караулова, MBAND, Monatik, Alekseev,  ПИЦЦА, Artik& Asti, Ofenbach, Mario Joy, Mahmut Orhan, Алина Артц, SWANKY TUNES, Eric Saade.</div>-->
                    </div>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
  import axios from 'axios'

  export default {
    data() {
      return {
        result: [],
        resent: []
      }
    },
    methods: {
      get() {
        let self = this;
        const id = this.$route.params.item

        axios.get('/api/project_category/')
          .then(
            function (response) {
              self.result = response.data
            },
            function (error) {
              console.log(error)
            }
          );
        axios.get('/api/resent_project/')
          .then(
            function (response) {
              self.resent = response.data
              self.$store.dispatch('loader', { value: false })
            },
            function (error) {
              console.log(error)
              self.$store.dispatch('loader', { value: false })
            }
          )
      }
    },
    created() {
      this.get()
    }

  }
</script>