import {getCookie, deleteCookie} from "../resources/Utility.js";

let team_combo = document.getElementById("team-select");

async function setup() {
    await read_username();
    await read_teams();
    let user_profile = document.getElementById("user-profile");
    let logout = document.getElementById("user-menu");
    user_profile.addEventListener("mouseover", show_menu);
    user_profile.addEventListener("mouseleave", hide_menu);
    logout.addEventListener("click", return_to_login);
}

function return_to_login() {
    deleteCookie("username");
    deleteCookie("auth");
    window.location.replace("http://localhost");
}

function show_menu() {
    let menu = document.getElementById("user-menu");
    menu.style.visibility = "visible";
}

function hide_menu() {
    let menu = document.getElementById("user-menu");
    menu.style.visibility = "hidden";
}

async function read_username() {
    const username = getCookie("username");
    const userDisplay = document.getElementById("username");
    userDisplay.innerHTML = username;
}

async function read_teams() {
    let teams = await fetch("http://localhost/team/").then((result) => {
        return result.json();
    });

    let content = "";
    for (let i = 0; i < teams["teams"].length; i++) {
        content += "<option value="+(i + 1)+">"+ teams["teams"][i]["_Team__name"] + "</option>"
    }
    const combo_teams = document.getElementById("team-select");
    combo_teams.innerHTML += content;
}

async function set_drivers() {
    let team_value = team_combo.value;
    let drivers = await fetch("http://localhost/driver/" + team_value)
        .then((result) => result.json());

    let driver_one = document.querySelector('label[for="member-one"]');
    let driver_two = document.querySelector('label[for="member-two"]');

    driver_one.textContent = drivers["drivers"][0];
    driver_two.textContent = drivers["drivers"][1];
}


window.addEventListener("load", setup);
document.getElementById("team-select").addEventListener("change", set_drivers);

async function bet() {
    var driverOne = document.getElementById("member-one").value
    var driverTwo = document.getElementById("member-two").value
    var but = document.getElementById("WettButton");

    if (driverTwo > -1) {
        but.disabled = false;
    } else {
        but.disabled = true;
    }
}
