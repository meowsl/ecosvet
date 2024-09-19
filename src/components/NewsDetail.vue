<template>
  <div class="news-detail q-pa-xl">
    <q-card-section class="absolute-right">
      <q-btn icon="close" flat round dense v-close-popup />
    </q-card-section>
    <div class="">
      <q-img :src="news.image" width="915px" height="340px" fit="contain" class="news-detail__img q-mb-lg"></q-img>
      <p class="news-detail__title q-mb-sm">{{ news.title }}</p>
      <p class="news-detail__date">Дата: {{news.publishDate}} г.</p>
    </div>
    <div class="news-detail__description">
      <q-separator class="event-detail__line q-my-md"/>
      <p>{{news.text}} </p>
    </div>
  </div>
</template>
<script setup lang="ts">
import newsImage from "../assets/images/events-img.svg"
import { ref, defineProps, PropType } from 'vue'
import { NewsDetail } from "src/models/news";
const props = defineProps({
  news: {
    type: Object as PropType<NewsDetail>,
    required: true
  },
})
</script>