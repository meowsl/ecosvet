import { boot } from 'quasar/wrappers'
import axios, { AxiosInstance, AxiosResponse, AxiosError } from 'axios'
import { useAuthStore } from 'src/stores/auth'
import { Notify } from 'quasar'
import { getAuthToken } from 'src/composables/useAuth'

declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $axios: AxiosInstance
    $api: AxiosInstance
  }
}

const api = axios.create({
  baseURL: process.env.DEV ? 'http://localhost:8000/api/v1/' : '/api/v1/',
  withCredentials: true,
  headers: {
    'Content-Type': 'application/json',
    'Authorization': getAuthToken()
  },
})

export default boot(({ app }) => {
  const authStore = useAuthStore()
  app.config.globalProperties.$axios = axios
  app.config.globalProperties.$api = api
  api.interceptors.response.use(
    (response: AxiosResponse) => {
      return response
    },
    (error: AxiosError) => {
      if (error.response?.status === 401) {
        authStore.userLogout()
        Notify.create({
          type: 'negative',
          message: 'Пожалуйста, авторизуйтесь снова!'
        })
        return error.response?.status
      }
      return Promise.reject(error)
    },
  )
})

export { api }
