export interface News {
    id: number | undefined
    title: string | undefined
    text: string | undefined
    image: string | undefined
  }
export interface NewsDetail {
    news: News
    publishedDate: string | undefined
    updatedDate: string | undefined
  }