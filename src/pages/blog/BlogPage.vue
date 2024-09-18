<template>
  <q-page class="blog-page">
    <q-img class="absolute-left" :src="foliageLeft" height="360px" width="540px"/>
    <q-img class="absolute-right" :src="foliageRight" height="360px" width="540px"/>
    <div class="blog-page__banner column justify-center items-center">
      <p class="blog-page__title">Блог <span class="blog-page__title-span">#ЭКОСВЕТа</span></p>
      <p class="blog-page__text">Авторские статьи, интервью, отчеты о <br> мероприятиях, обновления и много интересного!</p>
    </div>
  </q-page>
  <div class="row justify-center">
    <BlogList />
  </div>
</template>

<script setup lang="ts">
import foliageLeft from "images/foliage-left.svg"
import foliageRight from "images/foliage-right.svg"
import BlogList from "src/components/BlogList.vue"
</script>