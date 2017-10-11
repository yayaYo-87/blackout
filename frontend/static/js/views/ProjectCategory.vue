<template>
    <div class="project-category">
        <div class="project-category__wrapper">
            <div class="project-category__header">
                <router-link :to="{  name: 'project' }" class="project-category__header_title">Проекты</router-link>
                <div class="project-category__header_name">Концерты</div>
            </div>
            <div class="project-category__recent">
                <item-project
                        v-for="(item, index) in result.project_categories"
                        :key="index"
                        :item="item"
                        :index="index"
                ></item-project>
            </div>
        </div>
    </div>
</template>

<script>
  import axios from 'axios'
  import itemProject from '../components/ProjectCategoryRecent.vue'

  export default {
    data() {
      return {
        result: []
      }
    },
    components: {
      itemProject
    },
    methods: {
      get() {
        let self = this;
        const id = this.$route.params.id;

        axios.get('/api/project_category/' + id + '/')
          .then(
            function (response) {
              self.result = response.data
            },
            function (error) {
              console.log(error)
            }
          )
      }
    },
    created() {
      this.get()
    }

  }
</script>