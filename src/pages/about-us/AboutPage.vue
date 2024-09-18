<template>
    <q-page class="about-page column justify-center items-center">
      <q-img class="absolute-left" :src="foliageLeft" height="360px" width="540px"/>
      <q-img class="absolute-right" :src="foliageRight" height="360px" width="540px"/>
      <div class="about-page__banner column justify-center items-center ">
        <p class="about-page__title">Мы - команда <span class="about-page__title-span">template</span></p>
        <p class="about-page__under-title">Данная страница является ознакомительной и <br> не несет в себе функциональной нагрузки</p>
        <q-img :src="aboutMain" width="1000px" height="638"></q-img>
      </div>
    </q-page>
    <div class="column justify-center items-center">
      <AboutTargets />
      <AboutProblems />
      <AboutAdditionaly />
      <AboutFooter />
    </div>
  </template>

<script setup lang="ts">
import foliageLeft from "images/foliage-left.svg"
import foliageRight from "images/foliage-right.svg"
import aboutMain from "images/about-main.svg"
import AboutTargets from "src/components/AboutTargets.vue";
import AboutProblems from "src/components/AboutProblems.vue";
import AboutAdditionaly from "src/components/AboutAdditionaly.vue";
import AboutFooter from "src/components/AboutFooter.vue";
</script>