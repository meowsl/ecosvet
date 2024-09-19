export interface Post {
  id: number | undefined,
  title: string | undefined,
  text: string | undefined,
  contentType: string | undefined,
  image: string | undefined,
  publishDate: string | undefined | Date
}