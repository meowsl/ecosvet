import { api } from "boot/axios"
import { Post } from "models"

export function usePost() {
  const getPost = async () => {
    const response = await api.get<Post[]>(`blog/post-list/`, {
    })
    return response.data
  };

  return{
    getPost
  }
}