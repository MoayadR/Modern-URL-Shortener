const longURL = document.getElementById("longURL");
const shortURL = document.getElementById("shortURL");
const btn = document.getElementById("submit-btn");
const buttonDiv = document.getElementById("shortURL-buttons")
const visitBtn = document.getElementById("visit");
const copyBtn = document.getElementById("copy");
const shareBtn = document.getElementById("share");

btn.addEventListener("click" , () => {
    if(longURL.value && URLValidator(longURL.value))
    {
        getShortURL();
    }
    else
    {
        alert("Long URL Field Missing!")
    }
})

function displayShortURL(shortURLObj)
{
    shortURL.value = shortURLObj["shortURL"];
    buttonDiv.style.display = "flex";
}

async function getShortURL(){
    return await fetch("http://127.0.0.1:8000/api/short-url/" , {method: 'POST' , body: JSON.stringify({'longURL' : longURL.value})})   .then(response => response.json())
    .then(json => {displayShortURL(json);});
}

function URLValidator(url){
    try{
        new URL(url);
        return true;
    }
    catch(error)
    {
        return false;
    }
}


copyBtn.addEventListener("click" , () => {
    navigator.clipboard.writeText(shortURL.value);
})

visitBtn.addEventListener("click" , () => {
    window.open(shortURL.value , '_blank');
})