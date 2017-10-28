<template>
    <div class="about">
        <div class="about__wrapper">
            <div class="about__header">
                <div class="about__header_title">О компании</div>
                <img class="about__header_img" src="/static/img/header/logo1.svg">
            </div>
        </div>
        <div class="about__text">
            <div class="about__text_title">История основания</div>
            <div class="about__text_desc">
                Blackout studio была основана в 2008 . Основная идея создания
                заключалось в предоставлении качественных комплексных технических решений для
                проведения  мероприятий, таких как музыкальные фестивали, концерты, туры исполнителей
                и телевизионные съемки. За прошедшие годы компания существенно выросла и предлагает
                решения почти во всех областях шоу-техники.</br>
                Постоянно обновляющийся парк приборов, высокий технический уровень персонала и
                индивидуальный подход к каждому проекту позволяют решить практически любую задачу
                в сфере концертоного и ТВ продакшена. В 2016 году компания Blackout открыла представительство в Москве .
            </div>
        </div>
        <div class="about__text">
            <div class="about__text_title">Миссия компании</div>
            <div class="about__text_desc">Нести свет людям!</div>
        </div>
        <div class="about__text">
            <div class="about__text_title">Команда</div>
            <div class="about__text_desc">
                BlackOut Studio- сплоченная команда профессионалов, способная выполнить любое желание
                заказчика. У нас есть опыт работы со многими техническими коллективами со всего мира,
                мы можем выполнить райдер любого артиста мировой величины .</br>
                Трудолюбивость нашего коллектива подтверждается богатым портфолио наших работ. Все
                наши специалисты влюблены в свое дело и делают его профессионально и эффектно.</br>
                Знакомьтесь – наша команда:
            </div>
        </div>
        <div class="about__item">
            <div class="about__item_title">Руководство</div>
            <div class="about__item_image">
                <div class="about__item_image-img" style="background-image: url('/static/img/about1.jpg')"></div>
                <div class="about__item_image-text">
                    <div class="about__item_image-text-title">Руководитель компании</div>
                    <div class="about__item_image-text-name">Илья Пиотровский</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
  export default {
    mounted() {
      this.$store.dispatch('loader', { value: false })
    }

  }
</script>