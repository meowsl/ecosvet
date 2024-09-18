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
      <q-btn no-caps class="index-page__btn row justify-center items-center q-py-lg" @click="scrollToEvents">
        <p class="text-white">Мероприятия</p>
        <q-img
          class="q-ml-sm"
          :src="Button"
          height="30px"
          width="25px"
        ></q-img>
      </q-btn>
    </div>
  </q-page>
  <div ref="events">
    <EventsList />
  </div>
</template>

<script setup lang="ts">
import Avatar from "images/avatar.svg"
import Button from "images/main_button.svg"
import EventsList from "src/components/EventsList.vue"
import { ref } from 'vue'

const events = ref<HTMLElement | null>(null)

const scrollToEvents = () => {
  if (events.value) {
    events.value.scrollIntoView({ behavior: 'smooth' });
  }
}
</script>
