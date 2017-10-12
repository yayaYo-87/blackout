<template>
    <div class="services">
        <div class="services__wrapper">
            <div class="services__title">Услуги</div>
            <div class="services__item" v-for="item in resultServices">
                <router-link tag="div" :to="{ name: 'servicesItem', params: { id: item.id } }">
                    <div class="services__item-img" :style="`background-image: url('` + item.cover + `');`"></div>
                    <div class="services__item_text">
                        <div class="services__item_text-title">{{ item.name }}</div>
                        <div class="services__item_text-desc">{{ item.short_description }}</div>
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
        resultServices: []
      }
    },
    methods: {
      getServices() {
        let self = this

        axios.get('/api/service/')
          .then(
            function (response) {
              self.resultServices = response.data
              self.$store.dispatch('loader', { value: false })
            },
            function (error) {
              console.log(error)
              self.$store.dispatch('loader', { value: false })
            }
          )
      }
    },
    created(){
      this.getServices()
    }
  }
</script>