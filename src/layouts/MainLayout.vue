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
                <q-btn class="">Войти</q-btn>                  
              </div>
            </q-toolbar>
        </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
</script>
