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
            <div class="catalog__item" >
                <!--:to="{ name: 'catalogItem', params: { id: item.id } }"-->
                <router-link :to="{ name: 'catalogCategory' }"  >
                    <div class="catalog__item-img" style="background-image: url('/static/img/catalog1.jpg');"></div>
                    <div class="catalog__item_text">
                        <div class="catalog__item_text-title">LED Экраны</div>
                        <div class="catalog__item_text-desc">
                            <div class="catalog__item_text-desc_item">
                                <span>Для работы на открытом воздухе</span>
                            </div>
                            <div class="catalog__item_text-desc_item">
                                <span>Гибкий LED экран</span>
                            </div>
                            <div class="catalog__item_text-desc_item">
                                <span>Медиасервера</span>
                            </div>
                            <div class="catalog__item_text-desc_item">
                                <span>LED задник</span>
                            </div>
                            <div class="catalog__item_text-desc_item">
                                <span>Для работы в помещениях</span>
                            </div>
                            <div class="catalog__item_text-desc_item">
                                <span>Декоративные эффекты</span>
                            </div>
                            <div class="catalog__item_text-desc_item">
                                <span>LED полоски</span>
                            </div>
                        </div>
                    </div>
                </router-link>
            </div>
            <!--<div class="catalog__item" v-for="item in result" >-->
            <!--<router-link :to="{ name: 'catalogCategory', params: { id: item.id} }" >-->
            <!--<div class="catalog__item-img" :style="`background-image: url('`+ item.cover + `');`"></div>-->
            <!--<div class="catalog__item_text">-->
            <!--<div class="catalog__item_text-title">{{ item.name }}</div>-->
            <!--<div class="catalog__item_text-desc">-->
            <!--<div class="catalog__item_text-desc_item" v-for="cat in item.cat_subcategories">-->
            <!--<span>{{ cat.name }}</span>-->
            <!--</div>-->
            <!--</div>-->
            <!--</div>-->
            <!--</router-link>-->
            <!--</div>-->
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
            },
            function (error) {
              console.log(error)
            }
          )
      }
    },
    created() {
//      this.get()
    }
  }
</script>