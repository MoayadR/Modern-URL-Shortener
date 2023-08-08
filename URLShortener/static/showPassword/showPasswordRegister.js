const showPass = document.getElementById("showPassword");
const passwordInput = document.getElementById("id_password")

showPass.addEventListener("click" , ()=>{
    if (showPass.checked == true)
    {
        passwordInput.type = "text";
    }
    else
    {
        passwordInput.type = "password";
    }
})