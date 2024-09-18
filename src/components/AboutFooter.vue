<template>
  <div class="about-footer row justify-between q-pa-lg">
    <div class="">
      <p class="q-mb-md">Разработано с душой и любовью <br>
      командой <span class="text-weight-regular">template</span></p>
      <p>© 2024</p>
    </div>
    <div class="">
      <p class="q-mb-md">Контакты команды</p>
      <div class="text-right q-gutter-sm">
        <q-img :src="FigmaIcon" width="30px" height="30px"></q-img>
        <q-img :src="GitHubIcon" width="30px" height="30px"></q-img>
        <q-img :src="TgIcon" width="30px" height="30px"></q-img>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import TgIcon from "images/telegram-icon.svg"
import GitHubIcon from "images/github-icon.svg"
import FigmaIcon from "images/figma-icon.svg"
</script>