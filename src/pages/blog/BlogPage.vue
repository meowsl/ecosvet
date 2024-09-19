<template>
  <q-page class="blog-page">
    <q-img class="absolute-left" :src="foliageLeft" height="360px" width="540px"/>
    <q-img class="absolute-right" :src="foliageRight" height="360px" width="540px"/>
    <div class="blog-page__banner column justify-center items-center">
      <p class="blog-page__title">Блог <span class="blog-page__title-span">#ЭКОСВЕТа</span></p>
      <p class="blog-page__text">Авторские статьи, интервью, отчеты о <br> мероприятиях, обновления и много интересного!</p>
    </div>
  <div class="row justify-center q-mt-lg">
    <BlogList :post="postData"/>
  </div>
  </q-page>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import foliageLeft from "images/foliage-left.svg"
import foliageRight from "images/foliage-right.svg"
import BlogList from "src/components/BlogList.vue"
import { Post } from "src/models/post";
import { usePost } from 'src/composables/usePost'
const postData = ref<Post[]>([])

const { getPost } = usePost()
onMounted(async () => {
  postData.value = await getPost()
})
</script>