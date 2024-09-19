<template>
  <div class="news-detail q-pa-xl">
    <q-card-section class="absolute-right">
      <q-btn
        icon="close"
        flat
        round
        dense
        v-close-popup
      />
    </q-card-section>
    <div class="">
      <q-img
        :src="post.image"
        width="915px"
        height="340px"
        fit="contain"
        class="news-detail__img q-mb-lg"
      ></q-img>
      <p class="news-detail__title q-mb-sm">{{ post.title }}</p>
      <p class="news-detail__date">Дата: {{ post.publishDate }} г.</p>
    </div>
    <div class="news-detail__description">
      <q-separator class="event-detail__line q-my-md" />
      <p>{{ post.text }} </p>
    </div>
  </div>
</template>
<script setup lang="ts">
import plachold from "../assets/images/events-img.svg"
import { ref, defineProps, PropType } from 'vue'
import { Post } from "models";

const props = defineProps({
  post: {
    type: Object as PropType<Post>,
    required: true
  },
})
</script>