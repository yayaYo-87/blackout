<template>
    <div class="partners">
        <div class="partners__wrapper">
            <div class="partners__header">
                <div class="partners__header_title">Партнеры</div>
            </div>
        </div>
        <div class="partners__item">
            <div class="partners__item_title">Производители оборудования</div>
            <div class="partners__item_icon">
                <img src="/static/img/LOGOS4.png" class="partners__item_icon-img" alt="">
                <img src="/static/img/pro2.png" class="partners__item_icon-img" alt="">
            </div>
            <div class="partners__item_desc">Мы поддерживаем постоянный контакт и регулярно обмениваемся информацией с производителями нашего оборудования. Это сотрудничество затрагивает многие аспекты работы и приносит пользу обеим сторонам. Помимо помощи в ремонте оборудования, технической поддержки и совместных пресс-релизов, производители совершенствуют свои приборы с учетом наших пожеланий.</div>
        </div>
    </div>
</template>

<script>
  export default {
    data() {
      return {

      }
    },
    mounted() {
      this.$store.dispatch('loader', { value: false })
    }
  }
</script>