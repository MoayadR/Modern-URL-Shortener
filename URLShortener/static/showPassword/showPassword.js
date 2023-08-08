const showPass = document.getElementById("showPassword");
const passwordInput = document.getElementById("password")



showPass.addEventListener("click" , ()=>{
    console.log(password.value);
    if (showPass.checked == true)
    {
        passwordInput.type = "text";
    }
    else
    {
        passwordInput.type = "password";
    }
})