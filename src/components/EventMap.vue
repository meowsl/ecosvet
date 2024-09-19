<template>
  <div class="map">
    <yandex-map
      :settings="{
        location: {
          center: [37.617644, 55.755819],
          zoom: 9,
        },
      }"
      width="95%"
      height="350px"
      @ymapsready="initMap"
    >
      <yandex-map-default-marker :settings="markerInfo" />
      <yandex-map-default-scheme-layer />
      <yandex-map-default-features-layer />
      <yandex-map-controls :settings="{ position: 'right' }">
        <yandex-map-zoom-control />
      </yandex-map-controls>
    </yandex-map>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, defineProps, PropType } from 'vue';
import type { LngLat } from '@yandex/ymaps3-types';
import {
  YandexMap,
  YandexMapDefaultSchemeLayer,
  YandexMapDefaultFeaturesLayer,
  initYmaps,
  createYmapsOptions,
  YandexMapDefaultMarker,
  YandexMapControls,
  YandexMapZoomControl
} from 'vue-yandex-maps';
import { settings } from 'cluster';

const map = ref();

const markerInfo = ref();

const props = defineProps({
  address: {
    type: String as PropType<string | undefined>,
    required: true,
  },
});

/* Тут получаем координаты по адресу */
async function geocodeAddress(address: string | any) {
  const apiKey = 'c0d403ab-e5be-4049-908c-8122a58acf23';
  const response = await fetch(
    `https://geocode-maps.yandex.ru/1.x/?apikey=${apiKey}&geocode=${encodeURIComponent(
      address
    )}&format=json`
  );

  const data = await response.json();

  if (data.response.GeoObjectCollection.featureMember.length > 0) {
    const [lon, lat] = data.response.GeoObjectCollection.featureMember[0].GeoObject.Point.pos.split(' ');
    return [parseFloat(lon), parseFloat(lat)] as LngLat;
  } else {
    return null;
  }
}

async function initMap() {
  const eventCoord = new Map();
  try {
    const coords: LngLat | null = await geocodeAddress(props.address);
    if (coords) {
      markerInfo.value = {
        coordinates: coords,
        title: props.address,
      }
    }
  } catch (error) {
    console.error('Error initializing map:', error);
  }
}

onMounted(async () => {
  initMap();


  const options = createYmapsOptions({
    apikey: 'c0d403ab-e5be-4049-908c-8122a58acf23',
  });

  await initYmaps(options);
});
</script>

<style scoped>
.map {
  width: 95%;
}
</style>