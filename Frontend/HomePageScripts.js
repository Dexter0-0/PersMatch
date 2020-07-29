var UsernameElement = document.getElementById("Username")
var AgeElement = document.getElementById("Age")
var InstagramElement = document.getElementById("Instagram")

var UserUsername = "Lmao Androginescu"
var UserAge = "69"
var UserInstagram = "nandra._.rares"

var InstagramLink = "https://www.instagram.com/" + String(UserInstagram) + "/"

UsernameElement.textContent = UserUsername;
AgeElement.textContent = UserAge;
InstagramElement.textContent = UserInstagram;
InstagramElement.setAttribute('href', InstagramLink);