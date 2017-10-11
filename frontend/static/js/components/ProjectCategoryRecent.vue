<template>
    <router-link tag="div" :to="{ name: 'projectItem', params: { item: item.slug}}" class="project-category__recent_item"
         :class="[itemHeight, itemRight]">

        <div class="project-category__recent_item-img" :style="`background-image: url('` + item.cover + `')`" ></div>
        <div class="project-category__recent_item-wrapper">
            <div class="project-category__recent_item-wrapper_title">{{ item.name }}</div>
            <div class="project-category__recent_item-wrapper-flex">
                <div class="project-category__recent_item-wrapper-date">{{ item.date }}</div>
                <div class="project-category__recent_item-wrapper-desc">{{ item.short_desc }}</div>
                <div class="project-category__recent_item-wrapper_link">
                    Подробнее
                </div>
            </div>
        </div>
    </router-link>
</template>

<script>
  export default {
    props: ['item', 'index'],
    data() {
      return {

      }
    },
    computed: {
      itemHeight(){
        return this.index === 2 ||
                this.index === 6  ||
                this.index === 10 ||
                this.index === 14 ||
                this.index === 18 ||
                this.index === 22 ||
                this.index === 26 ||
                this.index === 30 ||
                this.index === 34 ||
                this.index === 38 ||
                this.index === 42 ||
                this.index === 46 ||
                this.index === 50 ||
                this.index === 54 ||
                this.index === 58 ||
                this.index === 62 ||
                this.index === 66 ||
                this.index === 70  ? 'project-category__recent_item-height': ''
      },
      itemRight(){
        return this.index === 6 ||
                this.index === 14 ||
                this.index === 22 ||
                this.index === 30 ||
                this.index === 38 ||
                this.index === 46 ||
                this.index === 54 ||
                this.index === 62 ||
                this.index === 70 ? 'project-category__recent_item-right': ''
      }
    },
  }
</script>
