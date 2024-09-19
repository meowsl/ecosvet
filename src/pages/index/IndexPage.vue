<template>
  <q-page class="index-page column justify-center items-center">
    <div
      v-if="isAuthorized"
      class="column justify-center items-center q-mb-xl"
    >
      <q-img
        :src="Avatar"
        loading="lazy"
        fit="cover"
        height="132px"
        width="132px"
        class=""
      >
        <q-img
          :src="Logout"
          height="30px"
          width="30px"
          class="absolute-bottom-right cursor-pointer clickable"
          style="background-color: transparent;"
          @click="logout"
        />
      </q-img>
      <p class="index-page__auth-data">{{ authStore.user?.lastName }} {{ authStore.user?.firstName?.charAt(0) }}. {{
        authStore.user?.surname?.charAt(0) }}.</p>
      <p class="index-page__auth-data">
        {{ (authStore.user?.lastName && authStore.user?.lastName?.length > 0) || (authStore.user?.firstName &&
          authStore.user.firstName.length > 0) ?
          `${authStore.user.lastName} ${authStore.user.firstName?.charAt(0)}.` : `${authStore.user?.username}` }}
      </p>
    </div>
    <div class="column justify-center items-center q-mb-xl">
      <h1 class="index-page__main-head">#ЭКОСВЕТ</h1>
      <h2 class="index-page__head q-mb-md">Первый экологический</h2>
      <q-btn
        no-caps
        class="index-page__btn row justify-center items-center q-py-lg"
        @click="scrollToEvents"
      >
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
    <EventsList :events="eventData" />
  </div>
</template>

<script setup lang="ts">
import Avatar from "images/avatar.svg"
import Button from "images/main_button.svg"
import Logout from "images/logout-icon.svg"
import EventsList from "src/components/EventsList.vue"
import { ref, onMounted } from 'vue'
import { useAuth } from 'src/composables/useAuth'
import { isAuthorizedFunc } from "src/services/isAuth"
import { useAuthStore } from 'src/stores/auth'
import { useEvent } from "src/composables/useEvent"
const { getUserInfo } = useAuth()

const authStore = useAuthStore()
const isAuthorized = isAuthorizedFunc()
const { getEvent } = useEvent()
const eventData = ref<Event[]>([])

const events = ref<HTMLElement | null>(null)

onMounted(async () => {
  if (authStore.user?.firstName === undefined) {
    authStore.user = await getUserInfo()
  }

  eventData.value = await getEvent()
})

const logout = async () => {
  const result = await authStore.userLogout();
  window.location.reload();
}

const scrollToEvents = () => {
  if (events.value) {
    events.value.scrollIntoView({ behavior: 'smooth' });
  }
}
</script>
