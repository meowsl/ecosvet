<template>
  <div class="news-list row justify-center q-pt-xl">
    <h3 class="news-list__marquee absolute-left text-center">Экологически чистые новости планеты</h3>
    <h3 class="news-list__marquee absolute-right text-center">Экологически чистые новости планеты</h3>
    <div class="">
      <div class="row">
        <q-card class="news-list__main-card q-mr-xl cursor-pointer" clickable @click="popupVisible = !popupVisible">
            <q-img :src="newsImage"></q-img>
            <div class="news-list__main-card__text q-pa-md">Короткий заголовок</div>
        </q-card>
        <div class="q-gutter-lg">
          <q-card class="news-list__card cursor-pointer" clickable @click="popupVisible = !popupVisible">
            <q-card-section horizontal>
              <q-img :src="newsImage" width="295px" height="218px"></q-img>
              <div class="column q-ma-md">
                <div class="news-list__card__title q-mb-md">Короткий заголовок</div>
                <div class="news-list__card__description">И поехало описание все описывать что только можно туда сюда....</div>
              </div>
            </q-card-section>
          </q-card>
          <q-card class="news-list__card cursor-pointer" clickable @click="popupVisible = !popupVisible">
            <q-card-section horizontal>
              <q-img :src="newsImage" width="295px" height="218px"></q-img>
              <div class="column q-ma-md">
                <div class="news-list__card__title q-mb-md">Короткий заголовок</div>
                <div class="news-list__card__description">И поехало описание все описывать что только можно туда сюда....</div>
              </div>
            </q-card-section>
          </q-card>
        </div>
      </div>
    </div>
  </div>
  <q-dialog
    v-model="popupVisible"
    transition-show="slide-down"
    transition-hide="slide-down"
    transition-duration="500"
  >
    <NewDetail/>
  </q-dialog>
</template>
<script setup lang="ts">
import { ref } from 'vue'
import newsImage from "images/news-image.svg"
import NewDetail from "./NewDetail.vue";
const popupVisible = ref<boolean>(false)
</script>