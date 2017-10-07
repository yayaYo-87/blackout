<template>
  <div id="app" class="app"  >
    <header-block></header-block>

    <router-view></router-view>

    <footer-block></footer-block>
  </div>
</template>

<script>
  import headerBlock from '../components/Header.vue'
  import footerBlock from '../components/Footer.vue'

  export default {
    name: 'app',
    data () {
      return {
        loader: true
      }
    },
    components: {
      headerBlock,
      footerBlock
    },
    watch: {

    },
    computed: {

    },
    methods:{

    }
  }
</script>
