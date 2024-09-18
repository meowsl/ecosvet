<template>
  <div class="event-detail">
    <q-card-section class="absolute-right">
      <q-btn icon="close" flat round dense v-close-popup />
    </q-card-section>
    <div class="event-detail__card q-px-md">
      <div class="event-detail__container">
        <q-img
          class="event-detail__img q-my-md"
          :src="EventsImg"
          width="600px"
          height="340px"
        />
        <div class="column q-ml-lg">
          <p class="event-detail__title q-mt-xl">Название мероприятия можно длинное</p>
          <p class="event-detail__data q-mt-sm">Дата: 18.09.2024 г.</p>
          <p class="event-detail__data q-mt-sm">Автор: Фамилия Имя Отчество</p>

          <q-btn no-caps class="event-detail__btn q-mt-auto q-mb-md">Принять участие</q-btn>
        </div>
      </div>
      <div class="event-detail__section">
        <q-separator class="event-detail__line q-my-md"/>
        <div class="event-detail__description q-pt-none q-my-md">
          Данное мероприятие нацелено на крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое и вообще крутое
        </div>
        <q-separator class="event-detail__line  q-my-md"/>
        <div class="event-detail__place">
          <p class="event-detail__section-head q-mb-md">Место проведения</p>
          <div class="event-detail__map"></div>
          <p class="event-detail__address q-my-sm">г. Москва, ул. Рандомная, д. 666 <br> Ориентир: вход там где выход</p>
        </div>
        <q-separator class="event-detail__line  q-my-md"/>
        <p class="event-detail__section-head q-mb-md">Принять участие</p>
        <div class="">
          <q-form
            @submit="onSubmit"
            class="event-detail__form q-gutter-md row"
          >
            <q-input
              rounded
              outlined
              v-model="firstname"
              placeholder="Имя"
              class="event-detail__field"
            />
            <q-input
              rounded
              outlined
              v-model="lastname"
              placeholder="Фамилия"
              class="event-detail__field"
            />
            <q-input
              rounded
              outlined
              v-model="surname"
              placeholder="Отчество"
              class="event-detail__field"
            />
            <q-input
              rounded
              outlined
              v-model="email"
              placeholder="Email"
              class="event-detail__field"
            />
            <div class="q-ml-auto q-mr-md">
              <q-btn class="event-detail__form-btn" no-caps label="Подтвердить" type="submit"/>
            </div>
          </q-form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, defineProps } from 'vue'
import { useQuasar } from 'quasar'
import EventsImg from "../assets/images/events-img.svg"
const firstname = ref('')
const lastname = ref('')
const surname = ref('')
const email = ref('')
const $q = useQuasar()
const onSubmit = () => {
    $q.notify({
      color: 'red-5',
      textColor: 'white',
      icon: 'warning',
      message: 'You need to accept the license and terms first'
    })
}
</script>