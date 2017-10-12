<template>
    <div class="main__project">
        <div class="main__project_items" v-if="result.length !== 0">
            <div class="main__project_item">
                <div class="main__project_item-title">Наши проекты</div>
                <router-link tag="div" :to="{ name: 'project' }" class="main__project_item-link">Показать все проекты</router-link>
            </div>
            <router-link v-if=" result[0] && result[0].length !== 0" tag="div" :to="{ name: 'projectItem', params: {  item: result[0].id , id: result[0].category.slug } }"
                         class="main__project_item main__project_item-hover">
                <div class="main__project_item-img" :style="`background-image: url('` + result[0].cover +`') ;`" ></div>
                <div class="main__project_item-wrapper">
                    <div class="main__project_item-wrapper_title">{{ result[0].name }}</div>
                    <div class="main__project_item-wrapper-flex">
                        <div class="main__project_item-wrapper-date">{{ result[0].date }}</div>
                        <div class="main__project_item-wrapper-desc">
                            {{ result[0].short_desc }}
                        </div>
                        <div class="main__project_item-wrapper_link">
                            Подробнее
                        </div>
                    </div>
                </div>
            </router-link>
            <router-link v-if="result[1] && result[1].length !== 0" tag="div" :to="{ name: 'projectItem', params: {  item: result[1].id , id: result[1].category.slug } }"
                         class="main__project_item main__project_item-hover main__project_item-height">
                <div class="main__project_item-img" :style="`background-image: url('` + result[1].cover +`') ;`" ></div>
                <div class="main__project_item-wrapper">
                    <div class="main__project_item-wrapper_title">{{ result[1].name }}</div>
                    <div class="main__project_item-wrapper-flex">
                        <div class="main__project_item-wrapper-date">{{ result[1].date }}</div>
                        <div class="main__project_item-wrapper-desc">
                            {{ result[1].short_desc }}
                        </div>
                        <div class="main__project_item-wrapper_link">
                            Подробнее
                        </div>
                    </div>
                </div>
            </router-link>
            <div class="main__project_item-two">
                <router-link  v-if="result[2] && result[2].length !== 0" tag="div" :to="{ name: 'projectItem', params: {  item: result[2].id , id: result[2].category.slug } }"
                             class="main__project_item main__project_item-hover">
                    <div class="main__project_item-img" :style="`background-image: url('` + result[2].cover +`') ;`" ></div>
                    <div class="main__project_item-wrapper">
                        <div class="main__project_item-wrapper_title">{{ result[2].name }}</div>
                        <div class="main__project_item-wrapper-flex">
                            <div class="main__project_item-wrapper-date">{{ result[2].date }}</div>
                            <div class="main__project_item-wrapper-desc">
                                {{ result[2].short_desc }}
                            </div>
                            <div class="main__project_item-wrapper_link">
                                Подробнее
                            </div>
                        </div>
                    </div>
                </router-link>
                <router-link v-if="result[3] && result[3].length !== 0" tag="div" :to="{ name: 'projectItem', params: {  item: result[3].id , id: result[3].category.slug } }"
                             class="main__project_item main__project_item-hover">
                    <div class="main__project_item-img" :style="`background-image: url('` + result[3].cover +`') ;`" ></div>
                    <div class="main__project_item-wrapper">
                        <div class="main__project_item-wrapper_title">{{ result[3].name }}</div>
                        <div class="main__project_item-wrapper-flex">
                            <div class="main__project_item-wrapper-date">{{ result[3].date }}</div>
                            <div class="main__project_item-wrapper-desc">
                                {{ result[3].short_desc }}
                            </div>
                            <div class="main__project_item-wrapper_link">
                                Подробнее
                            </div>
                        </div>
                    </div>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
  import axios from 'axios'

  export default {
    data() {
      return {
        result: []
      }
    },
    methods: {
      get() {
        let self = this;
        axios.get('/api/main_project/')
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
    created(){
      this.get()
    }
  }
</script>