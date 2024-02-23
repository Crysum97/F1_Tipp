async function onSubmit() {
    const user = document.getElementById("username");
    const pass = document.getElementById("password");


    var json = await fetch("http://localhost/user/" + user.value)
                            .then((response) => response.json())

    await sha256HashString(pass.value + json["Salt"])
        .then((result) => {
            if (result == json["Password"]) {
                console.log("Success");
            }
        })
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