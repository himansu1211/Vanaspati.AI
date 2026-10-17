import { useState } from 'react'
import { useAuthContext } from './useAuthContext'

export const useSignup = () => {
  const [error, setError] = useState(null)
  const [isLoading, setIsLoading] = useState(null)
  const { dispatch } = useAuthContext()

  const signup = async (email, password) => {
    setIsLoading(true)
    setError(null)

    const response = await fetch('http://127.0.0.1:4000/api/user/signup', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ email, password })
    })
    const json = await response.json()

    if (!response.ok) {
      setIsLoading(false)
      setError(json.error)
    }
    if (response.ok) {
      // saving the user to local storage
      localStorage.setItem('user', JSON.stringify(json))

      // updating the auth context
      dispatch({type: 'LOGIN', payload: json})

      // updating loading state
      setIsLoading(false)
    }
  }

  return { signup, isLoading, error }
}