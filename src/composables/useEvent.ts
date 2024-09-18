import { api } from "boot/axios"
import { Event, EventDetail } from "models"

export function useEvent() {
  const getEvent = async () => {
    const response = await api.get<Event[]>(`events/event-list/`, {
    })
    return response.data
  };
  const getEventDetail = async (eventId: number | undefined) => {
    try {
      const response = await api.get<EventDetail>(`events/event/${eventId}`);
      return response.data;
    } catch (error) {
      throw error;
    }
  };

  return{
    getEvent,
    getEventDetail
  }
}