<template>
    <div class="footer" :class="footerWhite">
        <div class="footer__wrapper">
            <div class="footer__logo">
                <img src="/static/img/logover.svg" alt="logo">
            </div>
            <div class="footer__cop">
                <div class="footer__cop_item footer__cop_item-phone">
                    <a href="tel:+74954097400">+7 (495) 409 74 00</a>
                </div>
                <div class="footer__cop_item footer__cop_item-mail">
                    <a target="_blank" href="mailto:office@blackout.moscow">office@blackout.moscow</a>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
  export default {
    data() {
      return {

      }
    },
    computed: {
      footerWhite(){
        return  this.$route.name === 'index' ? '' : 'footer-white'
      }
    }
  }
</script>