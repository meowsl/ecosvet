import { api } from "boot/axios"
import { Event } from "models"

export function useEvent() {
  const getEvent = async () => {
    const response = await api.get<Event[]>(`events/event-list/`, {
    })
    return response.data
  };
  return{
    getEvent
  }
}