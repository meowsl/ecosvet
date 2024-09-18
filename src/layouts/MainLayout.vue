<template>
  <q-layout view="lhрh Lpr lFf">
    <q-header class="navigation q-mt-md">
      <q-toolbar class="row justify-center items-center">
        <div class="navigation q-gutter-x-md text-subtitle1 text-weight-medium text-black q-mr-md">
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
        </div>
        <div class="">
          <q-btn
            v-if="!isAuthorized"
            no-caps
            class="navigation__btn text-white text-subtitle1"
            @click="authDialog = true"
          >Войти</q-btn>
          <router-link
            v-else
            :to="{ name: $route.name === 'ProfilePage' ? 'IndexPage' : 'ProfilePage' }"
          >
            <q-btn
              no-caps
              :class="{ 'navigation__btn': true, 'profile-btn': $route.name === 'ProfilePage' }"
              class="text-white text-subtitle1"
            >
              <q-img
                v-if="$route.name === 'ProfilePage'"
                :src="ProfileBtnLeft"
                width="18px"
                height="34px"
                class="q-ma-sm"
              />
              {{ $route.name === 'ProfilePage' ? 'Вернуться' : 'Профиль' }}
              <q-img
                v-if="$route.name === 'ProfilePage'"
                :src="ProfileBtnRight"
                width="18px"
                height="34px"
                class="q-ma-sm"
              />
            </q-btn>
          </router-link>
        </div>
      </q-toolbar>
    </q-header>

    <q-dialog
      class="auth-dialog"
      v-model="authDialog"
    >
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
            <q-form @submit="onSubmit">
              <q-card-section>
                <div class="auth-form__head text-h6 text-center">Авторизация</div>
              </q-card-section>
              <q-separator class="auth-form__line q-mx-auto" />
              <q-card-section class="column justify-center items-center">
                <div class="">
                  <p class="auth-form__input-label q-ml-lg">Логин</p>
                  <q-input
                    class="auth-form__input q-mb-md"
                    rounded
                    outlined
                    v-model="username"
                    :rules="[val => !!val || 'Введите логин!']"
                  />
                </div>
                <div class="auth-form__input-section">
                  <p class="auth-form__input-label q-ml-lg">Пароль</p>
                  <q-input
                    class="auth-form__input q-mb-sm"
                    :type="isPwd ? 'password' : 'text'"
                    rounded
                    outlined
                    v-model="password"
                    :rules="[val => !!val || 'Введите пароль!']"
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
                <a
                  href="/"
                  class="q-mt-sm text-h6"
                >Забыли пароль?</a>
                <div class="row">
                  <p class="text-h6 q-mr-xs">Нет аккаунта?</p>
                  <a
                    class="q-mb-sm text-h6 text-blue cursor-pointer"
                    @click="isAuth = !isAuth"
                  >Зарегистрироваться.</a>
                </div>
                <q-separator class="auth-form__line q-mx-auto" />
                <TelegramLogin class="q-mt-md" />
              </q-card-actions>
            </q-form>
          </q-card-section>
          <q-card-section
            v-else
            key="registration"
            class="registration-form"
          >
            <q-form @submit="applySubmit">
              <q-card-section>
                <div class="registration-form__head text-h6 text-center">Регистрация</div>
              </q-card-section>
              <q-separator class="registration-form__line q-mx-auto" />
              <q-card-section class="column justify-center items-center">
                <div class="">
                  <p class="registration-form__input-label q-ml-lg">Ваше имя</p>
                  <q-input
                    class="registration-form__input"
                    rounded
                    outlined
                    v-model="fullName"
                    :rules="[val => !!val || 'Поле обязательно для заполнения']"
                  />
                </div>
                <div class="">
                  <p class="registration-form__input-label q-ml-lg">E-mail</p>
                  <q-input
                    class="registration-form__input"
                    rounded
                    outlined
                    v-model="email"
                    :rules="[val => !!val || 'Поле обязательно для заполнения', isValidEmail]"
                  />
                </div>
                <div class="">
                  <p class="registration-form__input-label q-ml-lg">Пароль</p>
                  <q-input
                    class="registration-form__input"
                    :type="isPwd ? 'password' : 'text'"
                    rounded
                    outlined
                    v-model="password"
                    :rules="[val => val.length > 6 || 'Пароль должен состоять из 6 или более символов']"
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
                <a
                  no-caps
                  flat
                  class="q-my-sm text-h6 text-blue cursor-pointer"
                  @click="isAuth = !isAuth"
                >Уже есть аккаунт?</a>
                <q-separator class="registration-form__line q-mx-auto" />
                <TelegramLogin class="q-mt-md" />
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
import { useQuasar } from 'quasar'
import { ref, onMounted, watch } from 'vue'
import TgIcon from "images/telegram-icon.svg"
import ProfileBtnLeft from "images/profile-btn-left.svg"
import ProfileBtnRight from "images/profile-btn-right.svg"
import { isAuthorizedFunc } from "src/services/isAuth"
import { useAuthStore } from 'src/stores/auth'
import { UserReference } from 'src/models/auth'
import { useAuth } from 'src/composables/useAuth'
import TelegramLogin from 'src/components/TelegramLogin.vue'

const $q = useQuasar()

const { regUser } = useAuth()
const isAuthorized = isAuthorizedFunc()
const authStore = useAuthStore()
const authDialog = ref(false)
const text = ref('')
const username = ref('')
const password = ref('')
const fullName = ref('')
const email = ref('')
const isPwd = ref(true)
const isAuth = ref(true)

const isValidEmail = (val: string) => {
  const emailPattern = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/;
  return emailPattern.test(val) || 'Неверный формат email!';
}


const onSubmit = async () => {
  try {
    await authStore.userLogin(username.value.toLowerCase(), password.value);
  } catch (error) {
    console.error(error)
  }

}

const applySubmit = async () => {
  if (!fullName.value || !email.value || !password.value) {
    // $q.notify({
    //   type: 'negative',
    //   message: 'Пожалуйста, заполните все поля!',
    // });
    return;
  }
  const userData: UserReference = {
    fullName: fullName.value,
    email: email.value,
    password: password.value,
  };
  try {
    const response = await regUser(userData);

    if (response.status !== 201) return;
    location.reload();

    // $q.notify({
    //   type: 'positive',
    //   message: 'Заявка успешно отправлена!',
    // });
    // setTimeout(() => {
    //   isAuth.value = true
    // }, 1000);
  } catch (error) {
    console.error('Error submitting application:', error);
    // $q.notify({
    //   type: 'negative',
    //   message: 'Ошибка при отправке заявки!',
    // });
  }
}


</script>
