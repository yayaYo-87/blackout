<template>
    <div class="services-item">
        <div class="services-item__wrapper">
            <div class="services-item__text">
                <router-link tag="div" :to="{ name: 'services' }" class="services-item__title">Услуги</router-link>
                <div class="services-item__name">{{ result.name }}</div>
            </div>
            <div class="services-item__cover" :style="`background-image: url('` + result.cover + `')`"></div>
            <div class="services-item__desces" v-for="item in result.service_desces">
                <div class="services-item__desces-cover">
                    <img :src="item.cover" class="services-item__desces-img" alt="cover">
                    <div class="services-item__desces-name">{{ item.name }}</div>
                </div>
                <div class="services-item__desces-text">{{ item.description }}</div>
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
      getServicesItem(){
        let self = this;
        const id = self.$route.params.id;

        axios.get('/api/service/' + id + '/')
          .then(
            function (response) {
              self.result = response.data
              self.$store.dispatch('loader', { value: false })
            },
            function (error) {
              console.log(error)

            }
          )
      }
    },
    created(){
      this.getServicesItem()
    }
  }
</script>