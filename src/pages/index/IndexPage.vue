<template>
  <q-page class="index-page column justify-center items-center">
    <div class="column justify-center items-center">
      <!-- <q-img
          :src="Avatar"
          loading="lazy"
          fit="cover"
          height="132px"
          width="132px"
          class="q-my-xl"
      /> -->
      <h1 class="index-page__main-head">#ЭКОСВЕТ</h1>
      <h2 class="index-page__head q-mb-md">Первый экологический</h2>
      <q-btn class="index-page__btn row justify-center items-center">
        <p class="text-white">Мероприятия</p>
        <q-img
          class="q-ml-sm" 
          :src="Button"
          height="25px"
          width="25px"
        ></q-img>
      </q-btn>
    </div>
  </q-page>
</template>

<script setup lang="ts">
import AppExample from 'components/AppExample.vue'
import Avatar from "images/avatar.png"
import Button from "images/main_button.png"
</script>
