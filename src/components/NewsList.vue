<template>
  <div class="news-list row justify-center q-pt-xl q-pb-xl">
    <h3 class="news-list__marquee absolute-left text-center">Экологически чистые новости планеты</h3>
    <h3 class="news-list__marquee absolute-right text-center">Экологически чистые новости планеты</h3>
    <div class="news-list__container column align-center">
      <div class="row q-gutter-lg q-mb-md">
        <div
          class="news-list__main-card cursor-pointer"
          @click="openPopup(props.news[0]?.id)"
        >
          <q-img
            :src="props.news[0]?.image"
            width="625px"
            height="350px"
            fit="cover"
            style="border-radius: 25px !important;"
          ></q-img>
          <div class="news-list__main-card__text q-pa-md">{{ props.news[0]?.title }}</div>
        </div>
        <div class="column">
          <div
            class="q-mb-md"
            v-for="newsItem in props.news.slice(1, 3)"
            :key="newsItem.id"
          >
            <q-card
              class="news-list__card cursor-pointer q-mb-md"
              clickable
              @click="openPopup(newsItem.id)"
            >
              <q-card-section horizontal>
                <div>
                  <q-img
                    :src="newsItem.image"
                    width="295px"
                    height="218px"
                    fit="cover"
                    style="border-radius: 25px !important;"
                  ></q-img>
                </div>
                <div class="column q-ma-md">
                  <div class="news-list__card__title q-mb-md">{{ newsItem.title }}</div>
                  <div class="news-list__card__description">{{ newsItem.text }}</div>
                </div>
              </q-card-section>
            </q-card>
          </div>
        </div>
      </div>
      <div class="row q-gutter-md">
        <div
          v-for="newsItem in props.news.slice(3)"
          :key="newsItem.id"
        >
          <q-card
            class="news-list__card cursor-pointer"
            clickable
            @click="openPopup(newsItem.id)"
          >
            <q-card-section horizontal>
              <div style="border-radius: 25px !important;">
                <q-img
                  :src="newsItem.image"
                  width="295px"
                  height="218px"
                  fit="cover"
                  style="border-radius: 25px !important;"
                />
              </div>
              <div class="column q-ma-md">
                <div class="news-list__card__title q-mb-md">{{ newsItem.title }}</div>
                <div class="news-list__card__description">{{ newsItem.text }}</div>
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
    <NewsDetail :news="newsDetailData" />
  </q-dialog>
</template>
<script setup lang="ts">
import { ref, PropType } from 'vue'
import newsImage from "images/news-image.svg"
import NewsDetail from "./NewsDetail.vue";
import { News } from "src/models/news";
import { useNews } from 'src/composables/useNews'
const popupVisible = ref<boolean>(false)
const selectedNewsId = ref<number | null>(null);
const { getNewsDetail } = useNews()
const newsDetailData = ref<News | null>(null);

const props = defineProps({
  news: {
    type: Array as PropType<News[]>,
    required: true
  }
})

const openPopup = async (newsId: number) => {
  if (newsId !== undefined) {
    selectedNewsId.value = newsId;
    const newsDetail = await getNewsDetail(newsId)
    newsDetailData.value = newsDetail
    popupVisible.value = true;
  }
}
</script>