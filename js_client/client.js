const loginForm = document.getElementById("login-form")
const baseEndpoint = "http://localhost:8000/api"


if (loginForm){
    loginForm.addEventListener('submit', handleLogin)

}

function handleLogin(e){
    // console.log(e)
    e.preventDefault()
    const loginEndpoint = `${baseEndpoint}/token/`
    let loginFormData = new FormData(loginForm)
    let loginObjectData = Object.fromEntries(loginFormData)
    let bodyStr = JSON.stringify(loginObjectData)
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: bodyStr

    }
    fetch(loginEndpoint, options)
    .then(response => response.json())
    .then(data => console.log(data))
}