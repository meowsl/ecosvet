import { user, UserReference } from "src/models/auth"
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
  const regUser = async (data: UserReference) => {
    try {
      const response = await api.post('auth/register/', data, {
        headers: {
          'Content-Type': 'application/json',
        }
      });
      return response;
    } catch (error) {
      console.error('Error uploading application:', error);
      throw error;
    }
  }

  return {
    getUserInfo,
    regUser,
  }
}