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

                <router-link :to="{ name: 'partners' }" class="header__item">
                    Партнеры
                </router-link>
                <router-link :to="{ name: 'about' }" class="header__item">
                    О компании
                </router-link>
                <router-link :to="{ name: 'contacts' }" class="header__item">
                    Контакты
                </router-link>
            </div>
            <a href="tel:+74954097400" class="header__tel">
                +7 (495) 409 74 00
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
