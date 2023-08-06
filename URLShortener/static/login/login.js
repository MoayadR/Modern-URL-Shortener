const username = document.getElementById("username")
const password = document.getElementById("password")
const form = document.getElementById("form")

form.addEventListener("submit" , (e)=> {
    e.preventDefault();
    if (username.value && password.value)
    {
        form.submit();
    }
    else
    {
        alert("Missing Input Field !");
    }
})