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
      <q-tab
        name="all"
        label="Все"
      />
      <q-tab
        v-for="type in contentTypes"
        :key="type"
        :name="type"
        :label="contentTypeLabels[type]"
      />
    </q-tabs>

    <q-tab-panels
      v-model="tab"
      animated
    >
      <q-tab-panel name="all">
        <div class="row justify-center">
          <div class="events__container">
            <div class="q-pa-md row items-start q-gutter-sm">
              <template
                v-for="(post, index) in post"
                :key="post.id"
              >
                <q-card
                  v-if="index === 0"
                  class="events__main-card"
                  flat
                  bordered
                >
                  <q-card-section horizontal>
                    <q-card-section class="events__main-card__section">
                      <q-img
                        class=""
                        :src="post.image"
                        width="219px"
                        height="280px"
                      />
                    </q-card-section>
                    <div class="">
                      <q-card-section class="events__main-card__head">
                        <p>{{ post.title }}</p>
                      </q-card-section>
                      <q-separator class="events__card-line q-ml-md" />
                      <q-card-section>
                        <p class="events__main-card__description">{{ post.text }}</p>
                      </q-card-section>
                      <q-btn
                        class="events__main-card__button absolute-bottom-right q-mr-md q-mb-sm"
                        no-caps
                        flat
                        @click="openDetail(post)"
                      >Подробнее</q-btn>
                    </div>
                  </q-card-section>
                </q-card>
                <q-card
                  v-else-if="index <= 2"
                  class="events__card"
                  flat
                  bordered
                >
                  <q-card-section class="events__card__section">
                    <q-card-section class="events__card__section">
                      <q-img
                        class="events__card__img"
                        :src="post.image"
                        width="284px"
                        height="250px"
                      />
                    </q-card-section>
                    <div class="">
                      <div class="events__card__head q-my-xs text-center">
                        <p>{{ post.title }}</p>
                      </div>
                      <q-separator class="events__card-line q-ml-md" />
                      <div class="q-pa-xs q-px-md">
                        <p>{{ post.text }}</p>
                      </div>
                      <div class="events__card__btn row justify-center absolute-left q-mr-md">
                        <q-btn
                          no-caps
                          flat
                          @click="openDetail(post)"
                        >Подробнее</q-btn>
                      </div>
                    </div>
                  </q-card-section>
                </q-card>
                <q-card
                  v-else
                  class="events__card"
                  flat
                  bordered
                >
                  <q-card-section class="events__card__section">
                    <q-card-section class="events__card__section">
                      <q-img
                        class="events__card__img"
                        :src="post.image"
                        width="284px"
                        height="250px"
                      />
                    </q-card-section>
                    <div class="">
                      <div class="events__card__head q-my-xs text-center">
                        <p>{{ post.title }}</p>
                      </div>
                      <q-separator class="events__card-line q-ml-md" />
                      <div class="events-card__description q-pa-xs q-px-md">
                        <p>{{ post.text }}</p>
                      </div>
                      <div class="events__card__btn row justify-center absolute-bottom q-mr-md q-mb-sm">
                        <q-btn
                          no-caps
                          flat
                          @click="openDetail(post)"
                        >Подробнее</q-btn>
                      </div>
                    </div>
                  </q-card-section>
                </q-card>
              </template>
            </div>
          </div>
        </div>
      </q-tab-panel>
      <q-tab-panel
        v-for="type in contentTypes"
        :key="type"
        :name="type"
      >
        <div class="row justify-center">
          <div class="events__container">
            <div class="q-pa-md row items-start q-gutter-sm">
              <template
                v-for="(post, index) in postByType[type]"
                :key="post.id"
              >
                <q-card
                  v-if="index === 0"
                  class="events__main-card"
                  flat
                  bordered
                >
                  <q-card-section horizontal>
                    <q-card-section class="events__main-card__section">
                      <q-img
                        class=""
                        :src="post.image"
                        width="219px"
                        height="280px"
                      />
                    </q-card-section>
                    <div class="">
                      <q-card-section class="events__main-card__head">
                        <p>{{ post.title }}</p>
                      </q-card-section>
                      <q-separator class="events__card-line q-ml-md" />
                      <q-card-section>
                        <p class="events__main-card__description">{{ post.text }}</p>
                      </q-card-section>
                      <q-card-section class="row justify-end">
                        <q-btn
                          class="events__main-card__button"
                          no-caps
                          flat
                          @click="openDetail(post)"
                        >Подробнее</q-btn>
                      </q-card-section>
                    </div>
                  </q-card-section>
                </q-card>
                <q-card
                  v-else-if="index <= 2"
                  class="events__card"
                  flat
                  bordered
                >
                  <q-card-section class="events__card__section">
                    <q-card-section class="events__card__section">
                      <q-img
                        class="events__card__img"
                        :src="post.image"
                        width="284px"
                        height="250px"
                      />
                    </q-card-section>
                    <div class="">
                      <div class="events__card__head q-my-xs text-center">
                        <p>{{ post.title }}</p>
                      </div>
                      <q-separator class="events__card-line q-ml-md" />
                      <div class="q-pa-xs q-px-md">
                        <p>{{ post.text }}</p>
                      </div>
                      <div class="events__card__btn row justify-center">
                        <q-btn
                          no-caps
                          flat
                          @click="openDetail(post)"
                        >Подробнее</q-btn>
                      </div>
                    </div>
                  </q-card-section>
                </q-card>
                <q-card
                  v-else
                  class="events__card"
                  flat
                  bordered
                >
                  <q-card-section class="events__card__section">
                    <q-card-section class="events__card__section">
                      <q-img
                        class="events__card__img"
                        :src="post.image"
                        width="284px"
                        height="250px"
                      />
                    </q-card-section>
                    <div class="">
                      <div class="events__card__head q-my-xs text-center">
                        <p>{{ post.title }}</p>
                      </div>
                      <q-separator class="events__card-line q-ml-md" />
                      <div class="q-pa-xs q-px-md">
                        <p>{{ post.text }}</p>
                      </div>
                      <div class="events__card__btn row justify-center">
                        <q-btn
                          no-caps
                          flat
                          @click="openDetail(post)"
                        >Подробнее</q-btn>
                      </div>
                    </div>
                  </q-card-section>
                </q-card>
              </template>
            </div>
          </div>
        </div>
      </q-tab-panel>
    </q-tab-panels>

    <q-dialog v-model="showDetail">
      <BlogDetail :post="selectedPost" />
    </q-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref, PropType, computed } from 'vue'
import { Post } from "src/models/post";
import BlogDetail from './BlogDetail.vue'; // Импортируйте компонент BlogDetail

const tab = ref('all')
const showDetail = ref(false)
const selectedPost = ref<Post | null>(null)

const props = defineProps({
  post: {
    type: Array as PropType<Post[]>,
    required: true
  }
})

const contentTypes = ['AR', 'IN', 'RE', 'RP', 'UP']

const contentTypeLabels = {
  AR: 'Статьи',
  IN: 'Интервью',
  RE: 'Исследования',
  RP: 'Отчеты',
  UP: 'Обновление платформы'
}

const postByType = computed(() => props.post.reduce((acc, post) => {
  if (!acc[post.contentType]) {
    acc[post.contentType] = []
  }
  acc[post.contentType].push(post)
  return acc
}, {}))

const openDetail = (post: Post) => {
  selectedPost.value = post
  showDetail.value = true
}
</script>
