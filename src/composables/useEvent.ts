import { api } from "boot/axios"
import { Event, EventDetail, UserEvent } from "models"
import { getAuthToken } from "./useAuth";

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
  const getUserEvent = async () => {
    try {
      const response = await api.get<UserEvent>(`events/user-event`);
      return response.data;
    } catch (error) {
      throw error;
    }
  };
  const eventJoin = async (eventId: number | undefined, data: UserEvent) => {
    try {
      const response = await api.post(`events/event/${eventId}/join`, data, {
        headers: {
        'Authorization': getAuthToken()
        }
      });
      return response.data;
    } catch (error) {
      throw error;
    }
  };

  return{
    getEvent,
    getEventDetail,
    getUserEvent,
    eventJoin
  }
}