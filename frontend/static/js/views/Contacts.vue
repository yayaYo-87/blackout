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
                <div class="contacts__item_text">г. Минск,  улица Богдановича,  дом 60</div>
                <div class="contacts__item_desc">Телефон/факс:</div>
                <a href="tel:+375 (17) 283 88 83" class="contacts__item_text">+375 (17) 283 88 83</a>
                <div class="contacts__item_desc">По вопросам аренды оборудования обращайтесь по телефонам:</div>
                <a href="tel:+375 (25) 632 28 29" class="contacts__item_text">+375 (25) 632 28 29 — Игорь</a>
                <a href="tel:+375 (29) 119 80 25" class="contacts__item_text">+375 (29) 119 80 25 — Илья</a>
                <div class="contacts__item_email">info@blackout.by </br>office@blackout.by</div>
            </div>
            <div class="contacts__map">
                <div class="contacts__map-id" id="map1"></div>
            </div>
        </div>
        <div class="contacts__items">
            <div class="contacts__item">
                <div class="contacts__item_title">Склад</div>
                <div class="contacts__item_desc">Наш склад находится в районе военного аэродрома Липки</div>
                <div class="contacts__item_text">г. Минск, ул.  Липковская 9/2, 1200 м от МКАД</div>
                <div class="contacts__item_desc">Телефон склада:</div>
                <a href="tel:+375 (29) 656 34 56" class="contacts__item_text">+375 (29) 656 34 56 — Андрей</a>
            </div>
            <div class="contacts__map">
                <div class="contacts__map-id" id="map2"></div>
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
      readyMap2(){
        var myMap = new ymaps.Map('map2', {
            center: [53.919728, 27.703819],
            zoom: 16,
            controls: []
          }, {
            searchControlProvider: 'yandex#search'
          }),

          // Создаём макет содержимого.
          MyIconContentLayout = ymaps.templateLayoutFactory.createClass(
            '<div style="color: #FFFFFF; font-weight: bold;">$[properties.iconContent]</div>'
          ),

          myPlacemarkWithContent = new ymaps.Placemark([53.919728, 27.703819], {
            hintContent: 'г. Минск, ул. Липковская 9/2, 1200 м от МКАД',
            balloonContent: 'г. Минск, ул. Липковская 9/2, 1200 м от МКАД',
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
      readyMap(){
        var myMap = new ymaps.Map('map1', {
            center: [53.920439, 27.567688],
            zoom: 16,
            controls: []
          }, {
            searchControlProvider: 'yandex#search'
          }),

          // Создаём макет содержимого.
          MyIconContentLayout = ymaps.templateLayoutFactory.createClass(
            '<div style="color: #FFFFFF; font-weight: bold;">$[properties.iconContent]</div>'
          ),

          myPlacemarkWithContent = new ymaps.Placemark([53.920439, 27.567688], {
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
          self.readyMap2()
        })
      });
    },

  }
</script>