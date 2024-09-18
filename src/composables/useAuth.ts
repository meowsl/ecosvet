import { user } from "src/models/auth"
import { api } from "boot/axios"

export const getAuthToken = () => {
  if (localStorage.getItem('token')) {
    return `Bearer ${localStorage.getItem('token')}`
  }
}

export function useAuth() {

  const getUserInfo = async () => {
    const response = await api.get<user>('auth/info/', {
      headers: {
        'Authorization': getAuthToken()
      }
    })
    return response.data
  }

  return {
    getUserInfo,
  }
}