<template>
    <div class="contacts">
        <div class="contacts__wrapper">
            <div class="contacts__header">
                <div class="contacts__header_title">Контакты</div>
            </div>
        </div>
        <div class="contacts__items">
            <div class="contacts__item">
                <div class="contacts__item_title">Главный офис</div>
                <div class="contacts__item_desc">Наш офис находится в магазине “Свет и Звук”</div>
                <div class="contacts__item_text">г.Москва, Новодмитровская улица, 1с1</div>
                <div class="contacts__item_desc">Телефон:</div>
                <a href="tel:+74954097400" class="contacts__item_text">+7 (495) 409 74 00</a>
                <a href="mailto:office@blackout.moscow" class="contacts__item_email">office@blackout.moscow</a>
            </div>
            <div class="contacts__map">
                <div class="contacts__map-id" id="map1"></div>
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
    methods: {
      yandex(url) {
        if (Array.isArray(url)) {
          let self = this;
          let prom = [];
          url.forEach(function (item) {
            prom.push(self.script(item));
          });
          return Promise.all(prom);
        }

        return new Promise(function (resolve, reject) {
          let r = false;
          let t = document.getElementsByTagName('script')[0];
          let s = document.createElement('script');


          s.src = url;
          s.type = 'text/javascript';
          s.onload = s.onreadystatechange = function () {
            if (!r && (!this.readyState || this.readyState === 'complete')) {
              r = true;
              resolve(this);
            }
          };
          s.onerror = s.onabort = reject;
          t.parentNode.insertBefore(s, t);
        });
      },
      readyMap(){
        var myMap = new ymaps.Map('map1', {
            center: [55.806515, 37.584667],
            zoom: 16,
            controls: []
          }, {
            searchControlProvider: 'yandex#search'
          }),

          // Создаём макет содержимого.
          MyIconContentLayout = ymaps.templateLayoutFactory.createClass(
            '<div style="color: #FFFFFF; font-weight: bold;">$[properties.iconContent]</div>'
          ),

          myPlacemarkWithContent = new ymaps.Placemark([55.806515, 37.584667], {
            hintContent: 'г. Минск, улица Богдановича, дом 60',
            balloonContent: 'г. Минск, улица Богдановича, дом 60',
          }, {
            // Опции.
            // Необходимо указать данный тип макета.
            iconLayout: 'default#imageWithContent',
            // Своё изображение иконки метки.
            iconImageHref: '/static/img/Group.svg',
            // Размеры метки.
            iconImageSize: [37, 48],
            // Смещение левого верхнего угла иконки относительно
            // её "ножки" (точки привязки).
            iconImageOffset: [-15, -40],
            // Смещение слоя с содержимым относительно слоя с картинкой.
            iconContentOffset: [15, 15],
            // Макет содержимого.
            iconContentLayout: MyIconContentLayout
          });

        myMap.geoObjects
          .add(myPlacemarkWithContent);
      },
    },
    created() {
      this.yandex('//api-maps.yandex.ru/2.1/?lang=ru_RU').then(() => {
        let self = this;
        ymaps.ready(function () {
          self.readyMap()
        })
      });
    },
    mounted() {
      this.$store.dispatch('loader', { value: false })
    }

  }
</script>