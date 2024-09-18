import { defineStore } from 'pinia'
import { api } from 'boot/axios'
import type { AuthState } from 'src/models/auth'

export const useAuthStore = defineStore('authStore', {
  state: (): AuthState => ({
    user: {
      id: undefined,
      username: undefined,
      firstName: undefined,
      lastName: undefined,
      email: undefined,
      surname: undefined
    },
  }),
  actions: {
    async userLogin(username: string, password: string) {
      await api
        .post('/auth/token/', { username, password })
        .then(async e => {
          const token = e.data.access
          localStorage.setItem('token', token)
          const userData = await this.getUserData()
          this.user = userData.data
          window.location.reload()
        })
        .catch(e => {
          if (e.response && e.response.status === 401) {
            console.log('Такого пользователя не существует')
          }
        })
    },
    async getUserData() {
      const token = localStorage.getItem('token')
      if (!token) {
        throw new Error('No token available')
      }
      return api.get('/auth/info/', {
        headers: { Authorization: `Bearer ${token}` },
      })
    },
    async userLogout() {
      localStorage.removeItem('token')
      this.router.push({ name: 'IndexPage' })
    },
    clear() {
      this.user = null
    },
  },
})
