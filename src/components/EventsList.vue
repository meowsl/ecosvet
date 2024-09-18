<template>
  <div class="events row justify-center">
    <div class="events__container">
      <div class="text-h1 q-pt-xl row justify-end q-mr-lg"><span class="events__head">ЭКО</span>-приятия</div>
      <div class="q-pa-md row items-start q-gutter-lg">
        <q-card class="events__main-card" flat bordered>
          <q-card-section horizontal>
            <q-card-section class="events__main-card__section">
              <q-img
                class=""
                :src="EventsImg"
                width="219px"
                height="280px"
              />
            </q-card-section>
            <div class="">
              <q-card-section class="events__main-card__head">
                <p>Название мероприятия <br> Название мероприятия</p>
              </q-card-section>
              <q-separator class="events__card-line q-ml-md"/>
              <q-card-section>
                <p class="events__main-card__description">Это мероприятие очень крутое правда мы старались всей командой и может у нас и получилось но это не значит что получилось у всех точнее не у каждого</p>
              </q-card-section>
              <q-card-section class="row justify-end">
                <q-btn class="events__main-card__button" no-caps flat @click="popupVisible = !popupVisible">Подробнее</q-btn>
              </q-card-section>
            </div>
          </q-card-section>
        </q-card>
        <q-card class="events__card" flat bordered>
          <q-card-section class="events__card__section">
            <q-card-section class="events__card__section">
              <q-img
                class="events__card__img"
                :src="EventsImg"
                width="284px"
                height="250px"
              />
            </q-card-section>
            <div class="">
              <div class="events__card__head q-my-xs text-center">
                <p>Название мероприятия</p>
              </div>
              <q-separator class="events__card-line q-ml-md"/>
              <div class="q-pa-xs q-px-md">
                <p>Это мероприятие очень крутое правда мы старались всей командой и может у нас и не...</p>
              </div>
              <div class="events__card__btn row justify-center">
                <q-btn no-caps flat>Подробнее</q-btn>
              </div>
            </div>
          </q-card-section>
        </q-card>
        <q-card class="events__card" flat bordered>
          <q-card-section class="events__card__section">
            <q-card-section class="events__card__section">
              <q-img
                class="events__card__img"
                :src="EventsImg"
                width="284px"
                height="250px"
              />
            </q-card-section>
            <div class="">
              <div class="events__card__head q-my-xs text-center">
                <p>Название мероприятия</p>
              </div>
              <q-separator class="events__card-line q-ml-md"/>
              <div class="q-pa-xs q-px-md">
                <p>Это мероприятие очень крутое правда мы старались всей командой и может у нас и не...</p>
              </div>
              <div class="events__card__btn row justify-center">
                <q-btn no-caps flat>Подробнее</q-btn>
              </div>
            </div>
          </q-card-section>
        </q-card>
      </div>
      <div class="row justify-center q-my-lg">
        <q-btn no-caps class="events__btn text-white row justify-center items-center">
          <p class="text-white">Увидеть больше</p>
          <q-img
            class="q-ml-sm"
            :src="EarthIcon"
            height="25px"
            width="25px"
          ></q-img>
        </q-btn>
      </div>
      <div class="row justify-center q-ma-xl fixed-bottom-right">
        <q-btn flat rounded no-caps class="events__scroll-btn">
          <a href="#banner">
            <q-avatar size="50px">
              <img :src="ScrollIcon">
            </q-avatar>
          </a>
        </q-btn>
      </div>
    </div>
  </div>
  <q-dialog
    v-model="popupVisible"
    transition-show="slide-down"
    transition-hide="slide-down"
    transition-duration="500"
  >
    <EventDetail/>
  </q-dialog>

</template>

<script setup lang="ts">
import { ref } from 'vue';
import EventDetail from "./EventDetail.vue";
import EventsImg from "../assets/images/events-img.svg"
import EarthIcon from "../assets/images/earth-icon.svg"
import ScrollIcon from "../assets/images/scroll-btn.svg"
const popupVisible = ref<boolean>(false)
</script>