import {check_login} from "./Utility.js";

window.onload = () => check_login();

async function register_user() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const check_user = await fetch("http://localhost/user/" + username)
        .then(result => result);

    const salt = await fetch("http://localhost/salt").then(result => result.json());

    const hash = await sha256HashString(password + salt["salt"]).then(result => result);

    if (check_user.status === 404) {
        await fetch("http://localhost/user", {
            method: "POST",
            body: JSON.stringify({
                'name': username.toString(),
                'pass_hash': hash,
                'salt': salt["salt"]
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        });
    } else {
        window.alert("Username already taken!");
    }
}

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

document.getElementById("registerBtn").addEventListener("click", register_user);