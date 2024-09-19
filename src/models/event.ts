export interface Event {
  id: number | undefined
  name: string | undefined
  description: string | undefined
  image: string | undefined
}
export interface EventDetail {
  id: number | undefined
  event: Event
  date: string | undefined
  address: string | undefined
  landmark: string | undefined
  author: string | undefined
  description?: string | undefined
}
