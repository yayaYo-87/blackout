<template>
    <div class="header">
        <div class="header__wrapper">
            <div class="header__logo">
                <router-link :to="{ name: 'index' }" class="header__logo_img">
                    <img src="/static/img/header/logogor.svg" alt="logo">
                </router-link>
            </div>
            <div class="header__items">
                <router-link :to="{ name: 'services' }" class="header__item">
                    Услуги
                </router-link>
                <router-link :to="{ name: 'catalog' }" class="header__item">
                    Оборудование
                </router-link>
                <router-link :to="{ name: 'project' }" class="header__item">
                    Проекты
                </router-link>
                <div class="header__item">
                    Партнеры
                </div>
                <div class="header__item">
                    О компании
                </div>
                <div class="header__item">
                    Контакты
                </div>
            </div>
            <a href="tel:+375 (25) 632 28 29" class="header__tel">
                +375 (25) 632 28 29
            </a>
        </div>
    </div>
</template>

<script>
  export default {
    data(){
      return {

      }
    }
  }
</script>
