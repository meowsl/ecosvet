<template>
  <div class="about-targets about-container row justify-center items-center">
    <div class="about-title about-targets__title">Наши цели</div>
    <div class="row q-mt-lg justify-center items-center q-mt-xl">
      <div class="col-7">
        <p class="about-text">Выбрав этот кейс примерно две недели назад перед командой сразу встал серьезный вопрос - <span class="about-span">“Для кого?”</span></p>
        <br>
        <p class="about-text">Кажется, что ответ вполне очевиден, однако среди <span class="about-span"> экологического сообщества </span> так же сущесвует множество других <span class="about-span"> социальных групп </span>, где <span class="about-span">вкусы</span> могут значительно различаться</p>
      </div>
      <div class="col-5 row justify-end items-center">
        <q-img :src="targetsFirst" width="400px" height="440px"></q-img>
      </div>
    </div>
    <div class="row q-mt-lg justify-center items-center">
      <div class="col-5 row justify-start items-center">
        <q-img :src="targetsSecond" width="400px" height="400px"></q-img>
      </div>
      <div class="col-7">
        <p class="about-text">После недолгих раздумий, наша команда дала максимально <span class="about-span">простой ответ</span>, который уже менее очевиден</p>
        <p class="about-span text-h4 text-right"> - Для всех!</p>
        <p class="about-text">Именно поэтому данный прототип способен заинтересовать все подгруппы <span class="about-span">одного большого сообщества!</span></p>
      </div>
    </div>
  </div>
  <div class="about-title about-targets__marquee-title q-mt-lg">То, что нас объединяет</div>
  <div class="wrap">
      <div class="items-wrap">
        <div class="items marquee">
          <div class="item">Система уровней</div>
          <div class="item mt-xl">Бонусная программа</div>
          <div class="item">Собственный бот</div>
          <div class="item mt-xl">Современный дизайн</div>
          <div class="item">Авторский блог</div>
          <div class="item mt-xl">Свежие новости</div>
        </div>
        <div aria-hidden="true" class="items marquee">
          <div class="item">Система уровней</div>
          <div class="item mt-xl">Бонусная программа</div>
          <div class="item">Собственный бот</div>
          <div class="item mt-xl">Современный дизайн</div>
          <div class="item">Авторский блог</div>
          <div class="item mt-xl">Свежие новости</div>
        </div>
      </div>
    </div>
</template>

<script setup lang="ts">
import targetsFirst from 'images/targets-first.svg'
import targetsSecond from 'images/targets-second.svg'
import targetsTitleBack from 'images/targets-title-back.svg'
</script>