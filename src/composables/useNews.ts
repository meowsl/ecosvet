import { api } from "boot/axios"
import { News } from "models"
import { getAuthToken } from "./useAuth";

export function useNews() {
  const getNews = async () => {
    const response = await api.get<News[]>(`news/news-list/`, {
    })
    return response.data
  };

  return{
    getNews
  }
}