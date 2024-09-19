<template>
  <div class="events row justify-center">
    <div class="events__container">
      <div class="events__head q-pt-xl row justify-end q-mr-lg">ЭКО<span class="text-black">-приятия</span></div>
      <div class="q-pa-md row items-start q-gutter-lg">
        <template v-for="(event, index) in props.events" :key="event.id">
        <q-card v-if="index === 0" class="events__main-card" flat bordered>
          <q-card-section horizontal>
            <q-card-section class="events__main-card__section">
              <q-img
                class="events__main-card__img"
                :src="event.image"
                width="219px"
                height="280px"
                fit="contain"
              />
            </q-card-section>
            <div class="">
              <q-card-section class="events__main-card__head">
                <p>{{ event.name }}</p>
              </q-card-section>
              <q-separator class="events__card-line q-ml-md"/>
              <q-card-section>
                <p class="events__main-card__description">{{ event.description }}</p>
              </q-card-section>
              <q-card-section class="row justify-end">
                <q-btn class="events__main-card__button absolute-bottom-right q-mr-md q-mb-sm" no-caps flat @click="openPopup(event.id)">Подробнее</q-btn>
              </q-card-section>
            </div>
          </q-card-section>
        </q-card>
        <q-card v-else class="events__card" flat bordered>
          <q-card-section class="events__card__section">
            <q-card-section class="events__card__section">
              <q-img
                class="events__card__img"
                :src="event.image"
                width="284px"
                height="250px"
                fit="contain"
              />
            </q-card-section>
            <div class="">
              <div class="events__card__head q-my-xs text-center">
                <p>{{ event.name }}</p>
              </div>
              <q-separator class="events__card-line q-ml-md"/>
              <div class="q-pa-xs q-px-md">
                <p class="events__card__description">{{ event.description }}</p>
              </div>
              <div class="events__card__btn row justify-center">
                <q-btn no-caps flat @click="openPopup(event.id)">Подробнее</q-btn>
              </div>
            </div>
          </q-card-section>
        </q-card>
      </template>
      </div>
      <div class="row justify-center q-my-lg">
        <q-btn no-caps class="events__btn text-white row justify-center items-center">
          <p class="text-white">Увидеть больше</p>
          <q-img
            class="q-ml-sm"
            :src="EarthIcon"
            height="30px"
            width="30px"
          ></q-img>
        </q-btn>
      </div>
      <div class="row justify-center q-ma-xl absolute-bottom-right">
        <q-btn flat rounded no-caps class="events__scroll-btn" @click="scrollToBanner">
            <q-avatar size="50px">
              <img :src="ScrollIcon">
            </q-avatar>
        </q-btn>
      </div>
    </div>
  </div>
  <q-dialog
    v-model="popupVisible"
    transition-show="slide-down"
    transition-hide="slide-down"
    transition-duration="500"
  >
    <EventDetail :event="eventDetailData" :userEvent="userEvent"/>
  </q-dialog>

</template>

<script setup lang="ts">
import { ref, PropType, onMounted } from 'vue';
import EventDetail from "./EventDetail.vue";
import { Event } from "src/models/event";
import { UserEvent } from "src/models/auth";
import EventsImg from "../assets/images/events-img.svg"
import EarthIcon from "../assets/images/earth-icon.svg"
import ScrollIcon from "../assets/images/scroll-btn.svg"
import { useEvent } from 'src/composables/useEvent'

const popupVisible = ref<boolean>(false)
const selectedEventId = ref<number | null>(null);
const { getEventDetail, getUserEvent } = useEvent()
const eventDetailData = ref<Event | null>(null);
const userEvent = ref<UserEvent |null>(null);

const props = defineProps({
  events:{
    type: Array as PropType<Event[]>,
    required: true
  }
})

const scrollToBanner = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
}

const openPopup = async (eventId: number) => {
  if (eventId !== undefined) {
    selectedEventId.value = eventId;
    const eventDetail = await getEventDetail(eventId)
    userEvent.value = await getUserEvent()
    eventDetailData.value = eventDetail
    popupVisible.value = true;
  }
}
</script>