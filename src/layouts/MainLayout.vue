<template>
  <q-layout view="lhрh Lpr lFf">
    <q-header class="navigation q-mt-md">
            <q-toolbar class="row justify-center items-center">
              <div
                class="navigation q-gutter-x-md text-subtitle1 text-weight-medium text-capitalize text-black q-mx-xl"
              >
                <router-link :to="{ name: 'IndexPage' }">
                  Главная
                </router-link>
                <router-link :to="{ name: 'NewsPage' }">
                  Новости
                </router-link>
                <router-link :to="{ name: 'BlogPage' }">
                  Блог
                </router-link>
                <router-link :to="{ name: 'AboutPage' }">
                  О нас
                </router-link>
                <q-btn no-caps class="navigation__btn text-white text-subtitle1" @click="alert = true">Войти</q-btn>
              </div>
            </q-toolbar>
      </q-header>

      <q-dialog class="auth-dialog" v-model="alert">
        <q-card
          class="auth-dialog__card column justify-center"
          :class="{ 'auth-dialog__card--auth ': isAuth, 'auth-dialog__card--registration': !isAuth }"
        >
          <transition
            name="fade"
            mode="out-in"
          >
            <q-card-section
              v-if="isAuth"
              key="auth"
              class="auth-form column justify-center"
            >
              <q-form
                @submit="onSubmit"
              >
                <q-card-section>
                  <div class="auth-form__head text-h6 text-center">Авторизация</div>
                </q-card-section>
                <q-separator class="auth-form__line q-mx-auto"/>
                <q-card-section class="column justify-center items-center">
                  <div class="">
                    <p class="auth-form__input-label q-ml-lg">Логин</p>
                    <q-input class="auth-form__input q-mb-md" rounded outlined v-model="text"/>
                  </div>
                  <div class="auth-form__input-section">
                    <p class="auth-form__input-label q-ml-lg">Пароль</p>
                    <q-input
                      class="auth-form__input q-mb-sm"
                      :type="isPwd ? 'password' : 'text'"
                      rounded
                      outlined
                      v-model="password"
                    >
                      <template v-slot:append>
                        <q-icon
                          :name="isPwd ? 'visibility_off' : 'visibility'"
                          class="cursor-pointer"
                          @click="isPwd = !isPwd"
                        />
                      </template>
                    </q-input>
                  </div>
                </q-card-section>
                <q-card-actions class="column">
                  <q-btn
                    class="auth-form__btn text-white"
                    flat
                    no-caps
                    type="submit"
                  >Войти</q-btn>
                  <a href="/" class="q-mt-sm text-h6">Забыли пароль?</a>
                  <div class="row">
                    <p class="text-h6 q-mr-xs">Нет аккаунта?</p>
                    <a class="q-mb-sm text-h6 text-blue cursor-pointer" @click="isAuth = !isAuth">Зарегистрироваться.</a>
                  </div>
                  <q-separator class="auth-form__line q-mx-auto"/>
                  <a href="https://yandex.ru" target="_blank" class="auth-form__tg-btn q-mt-sm">
                    <q-img :src="TgIcon"></q-img>
                  </a>
                </q-card-actions>
              </q-form>
            </q-card-section>
            <q-card-section
              v-else
              key="registration"
              class="registration-form"
            >
              <q-form
                @submit="onSubmit"
              >
                <q-card-section>
                  <div class="registration-form__head text-h6 text-center">Регистрация</div>
                </q-card-section>
                <q-separator class="registration-form__line q-mx-auto"/>
                <q-card-section class="column justify-center items-center">
                  <div class="">
                    <p class="registration-form__input-label q-ml-lg">Ваше имя</p>
                    <q-input class="registration-form__input q-mb-md" rounded outlined v-model="text"/>
                  </div>
                  <div class="">
                    <p class="registration-form__input-label q-ml-lg">E-mail</p>
                    <q-input class="registration-form__input q-mb-md" rounded outlined v-model="text"/>
                  </div>
                  <div class="">
                    <p class="registration-form__input-label q-ml-lg">Пароль</p>
                    <q-input
                      class="registration-form__input q-mb-sm"
                      :type="isPwd ? 'password' : 'text'"
                      rounded
                      outlined
                      v-model="password"
                    >
                      <template v-slot:append>
                        <q-icon
                          :name="isPwd ? 'visibility_off' : 'visibility'"
                          class="cursor-pointer"
                          @click="isPwd = !isPwd"
                        />
                      </template>
                    </q-input>
                  </div>
                </q-card-section>
                <q-card-actions class="column">
                  <q-btn
                    class="registration-form__btn text-white"
                    flat
                    no-caps
                    type="submit"
                  >Регистрация</q-btn>
                  <a no-caps flat class="q-my-sm text-h6 text-blue cursor-pointer" @click="isAuth = !isAuth">Уже есть аккаунт?</a>
                  <q-separator class="registration-form__line q-mx-auto"/>
                  <a href="https://yandex.ru" target="_blank" class="registration-form__tg-btn q-mt-sm">
                    <q-img :src="TgIcon"></q-img>
                  </a>
                </q-card-actions>
              </q-form>
            </q-card-section>
          </transition>
        </q-card>
      </q-dialog>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import TgIcon from "images/telegram-icon.svg"
const alert = ref(false)
const text = ref('')
const password = ref('')
const isPwd = ref(true)
const isAuth = ref(true)

const onSubmit = async () => {
  console.log('AAAAAAA')
}

</script>
