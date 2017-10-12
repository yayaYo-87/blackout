<template>
    <div class="item">
        <div class="item__wrapper">
            <div class="item__header">
                <router-link tag="div" :to="{ name: 'catalog' }" class="item__header_title">Оборудование</router-link>
                <router-link tag="div" :to="{ name: 'catalogCategory', params: {  id: $route.params.id } }" class="item__header_name">Световое оборудование</router-link>
                <div class="item__header_product " :class="{'item__header_product-new' : result.tag}">{{ result.name }}</div>
            </div>
            <div class="item__content">
                <div class="item__content_left">
                    <img :src="result.cover" alt="cover" class="item__content_img">
                    <div class="item__content_video">
                        <div class="item__content_video-text">Демо Видео:</div>
                        <a :href="result.you_tube_link" target="_blank">
                            <img src="/static/img/youtube.svg" alt="cover" class="item__content_video-img">
                        </a>
                    </div>
                    <div class="item__content_project">
                        <div class="item__content_project-title">Использован на мероприятиях:</div>
                        <div class="item__content_project-items">
                            <router-link tag="div" :to="{ name: 'projectItem', params: { id: item.category.slug, item: item.id } }" class="item__content_project-item" :key="index" v-for="(item, index) in result.projects">{{ item.name }}</router-link>
                        </div>
                    </div>
                </div>
                <div class="item__content_right" v-if=" result.producer && result.producer.length !== 0">
                    <div class="item__content_desc">{{ result.description }}</div>
                    <a :href="result.producer_link" target="_blank" class="item__content_link">Описание на сайте производителя</a>
                    <div class="item__content_producer">
                        <div class="item__content_producer_title">Производитель</div>
                        <div class="item__content_producer_item">
                            <img :src="result.producer.cover" alt="cover" class="item__content_producer_item-img">
                            <div class="item__content_producer_item-text">
                                <span>{{ result.producer.name }}</span>
                                <span>{{ result.producer.country }}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

  import axios from 'axios'

  export default {
    data() {
      return {
        result: []
      }
    },
    methods: {
      get() {
        let self = this;
        const id = this.$route.params.item

        axios.get('/api/device/' + id + '/')
          .then(
            function (response) {
              self.result = response.data
            },
            function (error) {
              console.log(error)
            }
          )
      }
    },
    created() {
      this.get()
    }

  }
</script>