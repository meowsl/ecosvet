<template>
  <div class="news-detail q-pa-xl">
    <q-card-section class="absolute-right">
      <q-btn icon="close" flat round dense v-close-popup />
    </q-card-section>
    <div class="">
      <q-img :src="newsImage" width="915px" height="340px" class="news-detail__img q-mb-lg"></q-img>
      <p class="news-detail__title q-mb-sm">Абалдеть какое мероприятие прошло вчера на позавчерашней улице!</p>
      <p class="news-detail__date">Дата: 18.09.2024 г.</p>
    </div>
    <div class="news-detail__description">
      <q-separator class="event-detail__line q-my-md"/>
      <p>Данное мероприятие нацелено на крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое </p>
      <p>Данное мероприятие нацелено на крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое </p>
    </div>
  </div>
</template>
<script setup lang="ts">
import newsImage from "../assets/images/events-img.svg"
</script>