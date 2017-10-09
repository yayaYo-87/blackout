<template>
    <div class="project-item">
        <div class="project-item__wrapper">
            <div class="project-item__header">
                <div class="project-item__header_title">Проекты</div>
                <div class="project-item__header_name">Концерты</div>
                <div class="project-item__header_product">БИ-2 “THE BEST OF!” Минск-Арена</div>
                <div class="project-item__header_date">02.04.2017</div>
            </div>
            <div class="project-item__video">
                <youtube :video-id="videoId" player-height="700" player-width="100%"  ></youtube>
            </div>
            <div class="project-item__desc">
                В “Минске-Арене” выступила группа “БИ-2” с программой “THE BEST OF!”. Со сцены прозвучали более двадцати хитов группы. Музыканты исполнили главные композиции из всех выпущенных альбомов – от ранних пластинок до последнего на данный момент студийного издания «#16плюс». Некоторые из них не звучали со сцены до появления программы «THE BEST OF» более 10 лет!
                Помимо музыкальной составляющей концерта «THE BEST OF» зрители увидели новую сценографию и световое шоу, подготовленное специально для этой программы, а также неизменно мощный рок-н-ролльный «живой» звук, которым славятся все выступления БИ-2.
            </div>
            <div class="project-item__slider">
                <swiper :options="swiperOption">
                    <swiper-slide>
                        <div class="project-item__swiper">
                            <img class="project-item__img" src="/static/img/project1.jpg">
                        </div>
                    </swiper-slide>
                    <swiper-slide>
                        <div class="project-item__swiper">
                            <img class="project-item__img" src="/static/img/project1.jpg">
                        </div>
                    </swiper-slide>
                    <swiper-slide>
                        <div class="project-item__swiper">
                            <img class="project-item__img" src="/static/img/project1.jpg">
                        </div>
                    </swiper-slide>
                    <div class="project-item-prev" slot="button-prev"></div>
                    <div class="project-item-next" slot="button-next"></div>
                </swiper>
            </div>
            <div class="project-item__equipment">
                <!--<div class="project-item__equipment-title">Оборудование</div>-->
            </div>
        </div>
    </div>
</template>

<script>
  import Swiper from "../../../../node_modules/vue-awesome-swiper/src/swiper.vue";

  export default {
    data() {
      return{
        videoId: 'vt3eYidL_GY',
        swiperOption: {
          paginationClickable: true,
          nextButton: '.project-item-next',
          prevButton: '.project-item-prev',
          loop: true,
          pagination: '.swiper-pagination',
          grabCursor: true,
          slidesPerView: 'auto',
          effect: 'coverflow',
          autoplay: 5000,
          centeredSlides: true,
          speed: 1000,
          coverflow: {
            rotate: 50,
            stretch: 0,
            depth: 100,
            modifier: 1,
            slideShadows : true
          }

        }
      }
    },
    components: {
      Swiper
    }
  }
</script>