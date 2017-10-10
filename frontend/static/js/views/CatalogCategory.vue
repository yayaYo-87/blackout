<template>
    <div class="category">
        <div class="category__wrapper">
            <div class="category__header">
                <router-link :to="{ name: 'catalog' }" class="category__header_title">Оборудование</router-link>
                <div class="category__header_name">{{ result.name }}</div>
                <div class="category__header_link">
                    <div class="category__header_link-item" v-for="header in result.cat_subcategories">
                        <a href="#">{{ header.name }}</a>
                    </div>
                </div>
            </div>
            <div class="category__items"  :key="item.id" v-for="item in result.cat_subcategories">
                <div class="category__items_name">{{ item.name }}</div>
                <div class="category__items_wrapper" >
                    <router-link :to="{ name: 'catalogItem', params: { item: cart.id } }"  :key="cart.id" v-for="cart in item.device_subcategories" class="category__item">
                        <div class="category__item-tag" v-if="cart.tag">NEW</div>
                        <div class="category__item_cover" :style="`background-image: url('` + cart.cover + `')`"></div>
                        <div class="category__item_text">
                            <div class="category__item_text-desc">{{ cart.producer.name }}</div>
                            <div class="category__item_text-name">{{ cart.name }}</div>
                        </div>
                    </router-link>
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
        const id = this.$route.params.id

        axios.get('/api/devices_category/' + id + '/')
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