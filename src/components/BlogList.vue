<template>
  <div class="blog-list">
      <q-tabs
        v-model="tab"
        dense
        narrow-indicator
        align="left"
        no-caps
        class="blog-list__tabs"
      >
        <q-tab name="all" label="Все" />
        <q-tab name="articles" label="Статьи" />
        <q-tab name="interview" label="Интервью" />
        <q-tab name="research" label="Исследования" />
        <q-tab name="reports" label="Отчеты" />
        <q-tab name="updates" label="Обновление платформы" />
      </q-tabs>

      <q-tab-panels v-model="tab" animated>
        <q-tab-panel name="all">
          <div class="row justify-center">
            <div class="events__container">
              <div class="q-pa-md row items-start q-gutter-sm">
                <q-card class="events__main-card" flat bordered>
                  <q-card-section horizontal>
                    <q-card-section class="events__main-card__section">
                      <q-img
                        class=""
                        :src="EventsImg"
                        width="219px"
                        height="280px"
                      />
                    </q-card-section>
                    <div class="">
                      <q-card-section class="events__main-card__head">
                        <p>Название мероприятия <br> Название мероприятия</p>
                      </q-card-section>
                      <q-separator class="events__card-line q-ml-md"/>
                      <q-card-section>
                        <p class="events__main-card__description">Это мероприятие очень крутое правда мы старались всей командой и может у нас и получилось но это не значит что получилось у всех точнее не у каждого</p>
                      </q-card-section>
                      <q-card-section class="row justify-end">
                        <q-btn class="events__main-card__button" no-caps flat @click="popupVisible = !popupVisible">Подробнее</q-btn>
                      </q-card-section>
                    </div>
                  </q-card-section>
                </q-card>
                <q-card class="events__card" flat bordered>
                  <q-card-section class="events__card__section">
                    <q-card-section class="events__card__section">
                      <q-img
                        class="events__card__img"
                        :src="EventsImg"
                        width="284px"
                        height="250px"
                      />
                    </q-card-section>
                    <div class="">
                      <div class="events__card__head q-my-xs text-center">
                        <p>Название мероприятия</p>
                      </div>
                      <q-separator class="events__card-line q-ml-md"/>
                      <div class="q-pa-xs q-px-md">
                        <p>Это мероприятие очень крутое правда мы старались всей командой и может у нас и не...</p>
                      </div>
                      <div class="events__card__btn row justify-center">
                        <q-btn no-caps flat>Подробнее</q-btn>
                      </div>
                    </div>
                  </q-card-section>
                </q-card>
                <q-card class="events__card" flat bordered>
                  <q-card-section class="events__card__section">
                    <q-card-section class="events__card__section">
                      <q-img
                        class="events__card__img"
                        :src="EventsImg"
                        width="284px"
                        height="250px"
                      />
                    </q-card-section>
                    <div class="">
                      <div class="events__card__head q-my-xs text-center">
                        <p>Название мероприятия</p>
                      </div>
                      <q-separator class="events__card-line q-ml-md"/>
                      <div class="q-pa-xs q-px-md">
                        <p>Это мероприятие очень крутое правда мы старались всей командой и может у нас и не...</p>
                      </div>
                      <div class="events__card__btn row justify-center">
                        <q-btn no-caps flat>Подробнее</q-btn>
                      </div>
                    </div>
                  </q-card-section>
                </q-card>
              </div>
            </div>
          </div>
        </q-tab-panel>

        <q-tab-panel name="articles">
          <div class="text-h6">Статьи</div>
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
        </q-tab-panel>

        <q-tab-panel name="interview">
          <div class="text-h6">Интервью</div>
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
        </q-tab-panel>

        <q-tab-panel name="research">
          <div class="text-h6">Исследования</div>
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
        </q-tab-panel>

        <q-tab-panel name="reports">
          <div class="text-h6">Отчеты</div>
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
        </q-tab-panel>

        <q-tab-panel name="updates">
          <div class="text-h6">Обновление платформы</div>
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
        </q-tab-panel>
      </q-tab-panels>
  </div>
</template>
<script setup lang="ts">
import { ref } from 'vue'
const tab = ref('all')
</script>