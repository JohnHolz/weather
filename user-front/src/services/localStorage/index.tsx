export const getToken = () => {
    try {
        const token = window.localStorage.getItem('user_token')
        if (!token) throw new Error("token not found");
        return token
    } catch (error) {
        console.error(error)
    }
}

export const setToken = (token: string) => {
    try {
        window.localStorage.setItem('user_token', token)
    } catch (error) {
        console.error(error)
    }
}

export const isUserLogged = () => {
    try {
        const token = window.localStorage.getItem('user_token')
        if (!token) return false
        return true
    } catch (error) {
        console.error(error)
    }
}