<template>
  <div id="app" class="app"  >
    <header-block></header-block>
    <transition name="routerw">
      <div class="loader-wrapper" v-if="loaderw" >
        <div class="loader-wrapper_gif">
          <div class="cssload-thecube">
            <div class="cssload-cube cssload-c1"></div>
            <div class="cssload-cube cssload-c2"></div>
            <div class="cssload-cube cssload-c4"></div>
            <div class="cssload-cube cssload-c3"></div>
          </div>
        </div>
      </div>
    </transition>
    <transition name="router" mode="out-in">
      <router-view></router-view>
    </transition>

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
    computed: {
      loaderw() {
        return this.$store.state.loader.loader
      }
    },
    methods: {
      loaderTrue() {
        this.$store.dispatch('loader', { value: true })
      }
    },
    watch: {
      '$route': 'loaderTrue'
    }
  }
</script>
