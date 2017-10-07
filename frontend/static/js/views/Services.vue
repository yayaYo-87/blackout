<template>
    <div class="services">
        <div class="services__wrapper">
            <div class="services__title">Услуги</div>
            <div class="services__item" v-for="item in resultServices">
                <div class="services__item-img" :style="`background-image: url('` + item.cover + `');`"></div>
                <div class="services__item_text">
                    <div class="services__item_text-title">{{ item.name }}</div>
                    <div class="services__item_text-desc">{{ item.short_description }}</div>
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
        resultServices: []
      }
    },
    methods: {
      getServices() {
        let self = this

        axios.get('/api/services/')
          .then(
            function (response) {
              self.resultServices = response.data
            },
            function (error) {
              console.log(error)
            }
          )
      }
    },
    created(){
      this.getServices()
    }
  }
</script>