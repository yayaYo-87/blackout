<template>
    <div class="main">
        <main-header></main-header>
        <main-project></main-project>
        <main-slider></main-slider>
        <main-client></main-client>
    </div>
</template>

<script>
  import mainHeader from '../components/MainHeaer.vue'
  import mainProject from '../components/MainProject.vue'
  import mainSlider from '../components/MainSlaider.vue'
  import mainClient from '../components/MainClient.vue'

  export default {
    data() {
      return {

      }
    },
    components:{
      mainHeader,
      mainProject,
      mainSlider,
      mainClient
    }
  }
</script>