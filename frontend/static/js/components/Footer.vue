<template>
    <div class="footer" :class="footerWhite">
        <div class="footer__wrapper">
            <div class="footer__logo">
                <img src="/static/img/logover.svg" alt="logo">
            </div>
            <div class="footer__cop">
                <div class="footer__cop_item footer__cop_item-phone">
                    <a href="tel:+375 (25) 632 28 29">+375 (25) 632 28 29</a>
                </div>
                <div class="footer__cop_item footer__cop_item-mail">
                    <a target="_blank" href="mailto:info@blackout.by">info@blackout.by</a>
                </div>
                <div class="footer__cop_item footer__cop_item-fc">
                    <a href="#" target="_blank">blackoutstudioBY</a>
                </div>
                <div class="footer__cop_item footer__cop_item-sk">
                    <a href="skype:alainprostminsk" target="_blank">alainprostminsk</a>
                </div>
                <div class="footer__cop_item footer__cop_item-map">
                    Республика Беларусь, 220002 Минск, ул. Богдановича, 60
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
        return  this.$route.name === 'services' ? 'footer-white' : '' ||
        this.$route.name === 'servicesItem' ? 'footer-white' : '' ||
        this.$route.name === 'catalog' ? 'footer-white' : ''
      }
    }
  }
</script>