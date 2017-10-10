<template>
    <div class="project">
        <div class="project__wrapper">
            <div class="project__header">
                <div class="project__header_title">Проекты</div>
            </div>
            <div class="project__recent">
                <div class="project__recent_title">Недавние</div>
                <div class="project__recent_items">
                    <div class="project__recent_item">
                        <div class="project__recent_item-img" style="background-image: url('/static/img/project1.jpg') ;" ></div>
                        <div class="project__recent_item-wrapper">
                            <div class="project__recent_item-wrapper_title">Международный фестиваль "рок за бобров"</div>
                            <div class="project__recent_item-wrapper-flex">
                                <div class="project__recent_item-wrapper-date">24.07.2017</div>
                                <div class="project__recent_item-wrapper-desc">
                                    22 июля на аэродроме «Боровая» под Минском состоялся десятый музыкальный фестиваль «Рок за Бобров».
                                </div>
                                <div class="project__recent_item-wrapper_link">
                                    Подробнее
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="project__recent_item">
                        <div class="project__recent_item-img" style="background-image: url('/static/img/project1.jpg') ;" ></div>
                        <div class="project__recent_item-wrapper">
                            <div class="project__recent_item-wrapper_title">Международный фестиваль "рок за бобров"</div>
                            <div class="project__recent_item-wrapper-flex">
                                <div class="project__recent_item-wrapper-date">24.07.2017</div>
                                <div class="project__recent_item-wrapper-desc">
                                    22 июля на аэродроме «Боровая» под Минском состоялся десятый музыкальный фестиваль «Рок за Бобров».
                                </div>
                                <div class="project__recent_item-wrapper_link">
                                    Подробнее
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="project__title">Все проекты</div>
            <div class="project__item" >
                <router-link tag="div" :to="{ name: 'projectCategory' }">
                    <div class="project__item-img" style="background-image: url('/static/img/project123.jpg');"></div>
                    <div class="project__item_text">
                        <div class="project__item_text-title">HOT & TOP. EUROPA PLUS TV!</div>
                        <div class="project__item_text-desc">Телеканал Europa Plus TV открыл 2017 год жаркой вечеринкой на самой большой площадке страны! 20 февраля в Минска-Арене выступили известные исполнители со своими лучшими хитами:Мот, Willy William, Carla’s Dreams, Burak Yeter, Юлианна Караулова, MBAND, Monatik, Alekseev,  ПИЦЦА, Artik& Asti, Ofenbach, Mario Joy, Mahmut Orhan, Алина Артц, SWANKY TUNES, Eric Saade.</div>
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
//      this.get()
    }

  }
</script>