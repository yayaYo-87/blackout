<template>
    <div class="project-category">
        <div class="project-category__wrapper">
            <div class="project-category__header">
                <div class="project-category__header_title">Проекты</div>
                <div class="project-category__header_name">Концерты</div>
            </div>
            <div class="project-category__recent">
                <item
                    v-for="(item, index) in result"
                    :key="index"
                    :item="item"
                    :index="index"
                ></item>
            </div>
        </div>
    </div>
</template>

<script>
  import item from '../components/ProjectCategoryRecent.vue'

  export default {
    components: {
      item
    },
    data() {
      return {
        result: [
          {
            cover: 'background-image: url(\'/static/img/project1.jpg\')',
            title: 'Международный фестиваль "рок за бобров"',
            date: '24.07.2017',
            desc: '22 июля на аэродроме «Боровая» под Минском состоялся десятый музыкальный фестиваль «Рок за Бобров».'
          },
          {
            cover: 'background-image: url(\'/static/img/project1.jpg\')',
            title: 'Международный фестиваль "рок за бобров"',
            date: '24.07.2017',
            desc: '22 июля на аэродроме «Боровая» под Минском состоялся десятый музыкальный фестиваль «Рок за Бобров».'
          },
          {
            cover: 'background-image: url(\'/static/img/project1.jpg\')',
            title: 'Международный фестиваль "рок за бобров"',
            date: '24.07.2017',
            desc: '22 июля на аэродроме «Боровая» под Минском состоялся десятый музыкальный фестиваль «Рок за Бобров».'
          },
          {
            cover: 'background-image: url(\'/static/img/project1.jpg\')',
            title: 'Международный фестиваль "рок за бобров"',
            date: '24.07.2017',
            desc: '22 июля на аэродроме «Боровая» под Минском состоялся десятый музыкальный фестиваль «Рок за Бобров».'
          },
          {
            cover: 'background-image: url(\'/static/img/project1.jpg\')',
            title: 'Международный фестиваль "рок за бобров"',
            date: '24.07.2017',
            desc: '22 июля на аэродроме «Боровая» под Минском состоялся десятый музыкальный фестиваль «Рок за Бобров».'
          },
          {
            cover: 'background-image: url(\'/static/img/project1.jpg\')',
            title: 'Международный фестиваль "рок за бобров"',
            date: '24.07.2017',
            desc: '22 июля на аэродроме «Боровая» под Минском состоялся десятый музыкальный фестиваль «Рок за Бобров».'
          },
          {
            cover: 'background-image: url(\'/static/img/project1.jpg\')',
            title: 'Международный фестиваль "рок за бобров"',
            date: '24.07.2017',
            desc: '22 июля на аэродроме «Боровая» под Минском состоялся десятый музыкальный фестиваль «Рок за Бобров».'
          },
          {
            cover: 'background-image: url(\'/static/img/project1.jpg\')',
            title: 'Международный фестиваль "рок за бобров"',
            date: '24.07.2017',
            desc: '22 июля на аэродроме «Боровая» под Минском состоялся десятый музыкальный фестиваль «Рок за Бобров».'
          },
          {
            cover: 'background-image: url(\'/static/img/project1.jpg\')',
            title: 'Международный фестиваль "рок за бобров"',
            date: '24.07.2017',
            desc: '22 июля на аэродроме «Боровая» под Минском состоялся десятый музыкальный фестиваль «Рок за Бобров».'
          },
          {
            cover: 'background-image: url(\'/static/img/project1.jpg\')',
            title: 'Международный фестиваль "рок за бобров"',
            date: '24.07.2017',
            desc: '22 июля на аэродроме «Боровая» под Минском состоялся десятый музыкальный фестиваль «Рок за Бобров».'
          },
        ]
      }
    }
  }
</script>