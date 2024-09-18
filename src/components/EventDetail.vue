<template>
  <div class="event-detail">
    <q-card-section class="absolute-right">
      <q-btn icon="close" flat round dense v-close-popup />
    </q-card-section>
    <div class="event-detail__card q-px-md">
      <div class="event-detail__container">
        <q-img
          class="event-detail__img q-my-md"
          :src="props.event.image"
          width="600px"
          height="340px"
          fit="contain"
        />
        <div class="column q-ml-lg">
          <p class="event-detail__title q-mt-xl">{{ props.event.name }}</p>
          <p class="event-detail__data q-mt-sm">Дата: {{ props.event.date }}</p>
          <p class="event-detail__data q-mt-sm">Автор: {{ props.event.author }}</p>

          <q-btn no-caps class="event-detail__btn q-mt-auto q-mb-md">Принять участие</q-btn>
        </div>
      </div>
      <div class="event-detail__section">
        <q-separator class="event-detail__line q-my-md"/>
        <div class="event-detail__description q-pt-none q-my-md">
          {{ props.event.description }}
        </div>
        <q-separator class="event-detail__line  q-my-md"/>
        <div class="event-detail__place">
          <p class="event-detail__section-head q-mb-md">Место проведения</p>
          <div class="event-detail__map"></div>
          <p class="event-detail__address q-my-sm">{{ props.event.address }} <br> {{ props.event.landmark }}</p>
        </div>
        <q-separator class="event-detail__line  q-my-md"/>
        <p v-if="!isAuth" class="event-detail__section-head q-mb-md">Принять участие</p>
        <div v-if="!isAuth" class="">
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
import { ref, defineProps, PropType } from 'vue'
import { useQuasar } from 'quasar'
import EventsImg from "../assets/images/events-img.svg"
import { EventDetail } from "src/models/event";
import { isAuthorizedFunc } from "src/services/isAuth"

const firstname = ref('')
const lastname = ref('')
const surname = ref('')
const email = ref('')
const $q = useQuasar()
const isAuth = isAuthorizedFunc()

const props = defineProps({
  event: {
    type: Object as PropType<EventDetail>,
    required: true
  }
})
const onSubmit = () => {
    // $q.notify({
    //   color: 'red-5',
    //   textColor: 'white',
    //   icon: 'warning',
    //   message: 'You need to accept the license and terms first'
    // })
}
</script>