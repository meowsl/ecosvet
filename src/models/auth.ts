export interface user {
  id: number | undefined
  username: string | undefined
  firstName: string | undefined
  lastName: string | undefined
  email?: string | undefined
  surname?: string | undefined
}

export interface UserReference {
  fullName?: string | undefined
  email?: string | undefined
  password?: string | undefined
}

export interface UserEvent {
  user?: string | undefined
  event?: string | undefined
}

export interface AuthState {
  user: user | null
}

export interface JWTTokenDecode {
  sub: number
  exp: number
}