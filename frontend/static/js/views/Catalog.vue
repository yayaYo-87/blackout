<template>
    <div class="catalog">
        <div class="catalog__wrapper">
            <div class="catalog__header">
                <div class="catalog__header_title">Оборудование</div>
                <div class="catalog__header_desc">Компания Blackout Studio предлагает различные
                    решения на рынке Беларуси с 2008 года. Основной профиль – оказание услуг по
                    проведению мероприятия самого высокого уровня. Аренда светового оборудования,
                    различных подвесных конструкций, а начиная с лета 2011 года звукового оборудования
                    и светодиодных экранов. Нашими постоянными заказчиками являются Первый и Второй
                    национальные каналы, Столичное телевиденье, “Атом интертеймент”, “All Stars”,
                    “Jet sounds promo” и другие. Практически каждое значимое событие в концерной,
                    фестивальной или ТВ продакшн сфере – это наша работа. Вторым направлением деятельности компании
                    является создание дизайна площадок, технические расчеты и сопровождающие проекты.</div>
            </div>
            <div class="catalog__item" v-for="item in result" >
                <router-link :to="{ name: 'catalogCategory', params: { id: item.slug} }" >
                    <div class="catalog__item-img" :style="`background-image: url('`+ item.cover + `');`"></div>
                    <div class="catalog__item_text">
                        <div class="catalog__item_text-title">{{ item.name }}</div>
                        <div class="catalog__item_text-desc">
                            <div class="catalog__item_text-desc_item" v-for="cat in item.cat_subcategories">
                                <router-link tag="span" :to="{ name: 'catalogCategory', params: { id: item.slug}, hash: `#w`+ cat.id }">
                                    {{ cat.name }}
                                </router-link>
                            </div>
                        </div>
                    </div>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
  import axios from 'axios'

  export default {
    data(){
      return {
        result: []
      }
    },
    methods: {
      get() {
        let self = this;
        axios.get('/api/devices_category/')
          .then(
            function (response) {
              self.result = response.data
              self.$store.dispatch('loader', { value: false })
            },
            function (error) {
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