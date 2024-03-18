import {getCookie, setCookie, check_login} from "./Utility.js";

window.onload = () => check_login();

// access user input
    const user = document.getElementById("username");
    const pass = document.getElementById("password");

async function onSubmit(){


    // get user data by name
    const json = await fetch("http://localhost/user/" + user.value)
        .then((response) => response.json());

    // generate hash using a given salt
    const hash = await sha256HashString(pass.value + json["Salt"]);

    // authenticate the user
    const auth = await fetch("http://localhost/auth?name=" + user.value + "&sha256_hash=" + hash)
        .then((result) => {
            return result;
        });

    const auth_json = auth.status === 200 ? await auth.json() : null;

    // save auth key as cookie
    if (auth_json != null && auth_json.hasOwnProperty("key")) {
            console.log("Access granted!");
            setCookie("username", user.value, 1);
            setCookie("auth", auth_json["key"], 1);
            window.location.href = "/bets";
    } else {
        window.alert("Wrong user data!");
    }
}
// Function to hash a string using SHA-256
async function sha256HashString(inputString) {
    // Convert the input string to an array buffer
    const encoder = new TextEncoder();
    const data = encoder.encode(inputString);

    // Use the Web Crypto API to generate the SHA-256 hash
    const hashBuffer = await crypto.subtle.digest('SHA-256', data);

    // Convert the hash buffer to a hex string
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    return hashArray.map(byte => byte.toString(16).padStart(2, '0')).join('');
}



function enterHandler(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        document.getElementById("submitBtn").click();
    }
}

document.querySelector('button').addEventListener('click', onSubmit);
// register key press event listener to allow login on enter
pass.addEventListener("keypress",enterHandler);
user.addEventListener("keypress",enterHandler);