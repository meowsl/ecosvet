<template>
  <q-page class="news-page row justify-center items-center">
    <q-img class="absolute-left" :src="foliageLeft" height="360px" width="540px"/>
    <q-img class="absolute-right" :src="foliageRight" height="360px" width="540px"/>
    <div class="news-page__banner col-9 q-mb-xl">
      <div class="">Последние новости <br> <span class="news-page__head">экологического</span> <br> сообщества</div>
      <q-btn no-caps class="news-page__btn" @click="scrollToNews">
        <p>Перейти</p>
        <q-img class="q-ml-md" :src="newsIcon" width="35px" height="35px"></q-img>
      </q-btn>
    </div>
  </q-page>
  <div ref="news">
    <NewsList :news="newsData"/>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import foliageLeft from "images/foliage-left.svg"
import foliageRight from "images/foliage-right.svg"
import newsIcon from "images/news-icon.svg"
import NewsList from "src/components/NewsList.vue"
import { News } from "src/models/news";
import { useNews } from 'src/composables/useNews'
const news = ref<HTMLElement | null>(null)
const newsData = ref<News[]>([])

const { getNews } = useNews()

const scrollToNews = () => {
  if (news.value) {
    news.value.scrollIntoView({ behavior: 'smooth' });
  }
}

const events = ref<HTMLElement | null>(null)

onMounted(async () => {
  newsData.value = await getNews()
})
</script>