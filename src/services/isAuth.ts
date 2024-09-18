export const isAuthorizedFunc = () => {
  const token = localStorage.getItem('token')
  return !!token
}