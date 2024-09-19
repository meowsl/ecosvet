<template>
  <div class="news-list row justify-center q-pt-xl">
    <h3 class="news-list__marquee absolute-left text-center">Экологически чистые новости планеты</h3>
    <h3 class="news-list__marquee absolute-right text-center">Экологически чистые новости планеты</h3>
    <div class="news-list__container">
      <div class="row q-gutter-md">
        <template v-for="(newsItem, index) in props.news" :key="newsItem.id">
          <q-card v-if="index === 0" class="news-list__main-card cursor-pointer" clickable @click="popupVisible = !popupVisible">
              <q-img :src="newsItem.image" width="625px" height="350px" fit="contain"></q-img>
              <div class="news-list__main-card__text q-pa-md">{{newsItem.title}}</div>
          </q-card>
          <q-card v-else class="news-list__card cursor-pointer" clickable @click="popupVisible = !popupVisible">
            <q-card-section horizontal>
              <q-img :src="newsItem.image" width="295px" height="218px" fit="contain"></q-img>
              <div class="column q-ma-md">
                <div class="news-list__card__title q-mb-md">{{ newsItem.title }}</div>
                <div class="news-list__card__description">{{ newsItem.text }}</div>
              </div>
            </q-card-section>
          </q-card>  
        </template>
      </div>
    </div>
  </div>
  <q-dialog
    v-model="popupVisible"
    transition-show="slide-down"
    transition-hide="slide-down"
    transition-duration="500"
  >
    <NewsDetail/>
  </q-dialog>
</template>
<script setup lang="ts">
import { ref, PropType } from 'vue'
import newsImage from "images/news-image.svg"
import NewsDetail from "./NewsDetail.vue";
import { News } from "src/models/news";
import { useNews } from 'src/composables/useNews'
const popupVisible = ref<boolean>(false)

const props = defineProps({
  news:{  
    type: Array as PropType<News[]>,
    required: true
  }
})
</script>