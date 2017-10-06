<template>
  <div id="app" class="app"  >
    <header-block

    ></header-block>
    <router-view></router-view>
  </div>
</template>

<script>
  import headerBlock from '../components/Header.vue'

  export default {
    name: 'app',
    data () {
      return {
        loader: true
      }
    },
    components: {
      headerBlock,
    },
    watch: {
      '$route' : 'mainFalse'
    },
    computed: {

    },
    methods:{

    }
  }
</script>
