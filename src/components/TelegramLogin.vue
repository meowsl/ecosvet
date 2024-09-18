<template>
  <div id="telegram-login"></div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import { useAuthStore } from 'src/stores/auth';

const authStore = useAuthStore()

onMounted(() => {
  initTelegramLogin();
});

function initTelegramLogin() {
  const script = document.createElement('script');
  script.src = 'https://telegram.org/js/telegram-widget.js?22';
  script.setAttribute('data-telegram-login', 'EcologySvet_bot');
  script.setAttribute('data-size', 'large');
  script.setAttribute('data-radius', '5');
  script.setAttribute('data-request-access', 'write');
  script.setAttribute('data-userpic', 'false');
  script.setAttribute('data-onauth', 'handleTelegramAuth(user)');
  document.getElementById('telegram-login')?.appendChild(script);
}

window.handleTelegramAuth = async function (user: any) {
  try {
    authStore.userTelegramLogin(user.id, user.username)
  } catch (error) {
    console.error('Error during Telegram auth:', error);
  }
};
</script>
