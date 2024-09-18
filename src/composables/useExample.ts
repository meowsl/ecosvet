import { api } from 'boot/axios'
import { Example } from 'src/models/example'

export function useExample() {
  const getExampleList = async () => {
    const { data } = await api.get<Example[]>('example/list')
    return data
  }

  return {
    getExampleList,
  }
}
