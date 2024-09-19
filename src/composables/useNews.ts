import { api } from "boot/axios"
import { News, NewsDetail } from "models"
import { getAuthToken } from "./useAuth";

export function useNews() {
  const getNews = async () => {
    const response = await api.get<News[]>(`news/news-list/`, {
    })
    return response.data
  };
  const getNewsDetail = async (newsId: number | undefined) => {
    try {
      const response = await api.get<NewsDetail>(`news/news/${newsId}`);
      return response.data;
    } catch (error) {
      throw error;
    }
  };

  return{
    getNews,
    getNewsDetail
  }
}