<template>
  <q-page class="profile-page row justify-center items-center">
    <div class="profile-page__section row justify-center">
      <q-card class="profile-page__data-card row">
        <div class="profile-page__data-card column items-center q-pt-lg">
          <div class="profile-page__img-section q-pb-lg">
            <q-img
            :src="Avatar"
            loading="lazy"
            fit="cover"
            height="200px"
            width="200px"
            class=""
          >
          </q-img>
          <q-img :src="Level" height="40px" width="60px" class="profile-page__level absolute-bottom" style="left: 50%; transform: translateX(-50%);"/>
          </div>
          <p class="profile-page__user-data q-mb-md">{{ authStore.user?.lastName }} {{ authStore.user?.firstName }} {{ authStore.user?.surname }}</p>
          <div class="">
            <p class="profile-page__label">Email</p>
            <div class="profile-page__input-section q-pl-md q-pt-xs">{{ authStore.user?.email }}</div>
            <p class="profile-page__label">Telegram</p>
            <div class="profile-page__input-section q-pl-md q-pt-xs"></div>
            <p class="profile-page__label">О себе</p>
            <div class="profile-page__input-about q-pl-md q-pt-xs"></div>
          </div>
          <p class="profile-page__achievement-title">Достижения</p>
          <q-separator class="profile-page__line q-my-sm"/>
          <div class="profile-page__achievement">
          </div>
        </div>
      </q-card>
      <q-card class="profile-page__event-card q-ml-sm q-pt-lg row justify-center">
        <ProfileDetails />
      </q-card>
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { onMounted } from "vue"
import Avatar from "images/avatar.svg"
import Level from "images/profile-lvl.svg"
import { useAuthStore } from 'src/stores/auth'
import { useAuth } from 'src/composables/useAuth'
import ProfileDetails from "src/components/ProfileDetails.vue"
const { getUserInfo } = useAuth()

const authStore = useAuthStore()

onMounted(async () => {
  if (authStore.user?.firstName === undefined) {
    authStore.user = await getUserInfo()
    console.log(authStore.user)
  }
})
</script>