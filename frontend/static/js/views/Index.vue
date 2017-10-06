<template>
    <div class="main">
        <main-header></main-header>
        <main-project></main-project>
        <main-slider></main-slider>
    </div>
</template>

<script>
  import mainHeader from '../components/MainHeaer.vue'
  import mainProject from '../components/MainProject.vue'
  import mainSlider from '../components/MainSlaider.vue'

  export default {
    data() {
      return {

      }
    },
    components:{
      mainHeader,
      mainProject,
      mainSlider
    }
  }
</script>