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
        <a
          target="_blank"
          href="https://www.figma.com/design/wiotFXVsLsShy6vIbojjG3/%D0%AD%D0%9A%D0%9E%D0%A1%D0%B2%D0%B5%D1%82?node-id=0-1&t=N4YP2C0YOVa1EdyN-1"
        >
          <q-img
            :src="FigmaIcon"
            width="30px"
            height="30px"
          />
        </a>
        <a
          target="_blank"
          href="https://github.com/meowsl/ecosvet"
        >
          <q-img
            :src="GitHubIcon"
            width="30px"
            height="30px"
          ></q-img>
        </a>
        <a
          target="_blank"
          href="https://t.me/slay_meow"
        >
          <q-img
            :src="TgIcon"
            width="30px"
            height="30px"
          ></q-img>
        </a>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import TgIcon from "images/telegram-icon.svg"
import GitHubIcon from "images/github-icon.svg"
import FigmaIcon from "images/figma-icon.svg"
</script>