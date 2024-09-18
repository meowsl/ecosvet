<template>
  <div class="profile-detail  column items-center">
    <div class="profile-detail__tabs column col-2">
      <div class="row q-gutter-x-md justify-center items-center q-mb-md">
        <p class="profile-detail__active-tab">Мои мероприятия</p>
        <p>Мои статьи</p>
        <p>Анализ активности</p>
      </div>
      <div class="row">
        <q-separator class="profile-detail__line"/>
      </div>
    </div>
    <div class="profile-detail__img col-8">
      <q-img :src="InDev" width="320px" height="360px"></q-img>
    </div>
  </div>
</template>
<script setup lang="ts">
import { ref } from 'vue'
import InDev from "images/in-dev.svg"
const tab = ref('events')
</script>