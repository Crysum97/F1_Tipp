    // Function to get a cookie by name
function getCookie(name) {
    var nameEQ = name + "=";
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i];
        while (cookie.charAt(0) === ' ') {
            cookie = cookie.substring(1, cookie.length);
        }
        if (cookie.indexOf(nameEQ) === 0) {
            return cookie.substring(nameEQ.length, cookie.length);
        }
    }
    return null;
}

// Function to set a cookie with expiration time in hours
function setCookie(name, value, hours) {
    var expires = "";
    if (hours) {
        var date = new Date();
        date.setTime(date.getTime() + (hours * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + value + expires + "; path=/";
}

function deleteCookie(name) {
    document.cookie = name + "=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
}


async function check_login() {
        let user_cookie = getCookie("username");
        let auth_cookie = getCookie("auth");

        if(user_cookie == null || auth_cookie == null) return;


        const auth = await fetch("http://localhost/auth/" + user_cookie + "?auth_key=" + auth_cookie)
            .then((response) => response);

        if (auth.status === 200) {
            window.location.href = "http://localhost/bets";
        }
}

export {getCookie, setCookie, deleteCookie, check_login};