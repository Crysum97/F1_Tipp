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

async function set_event() {
    let event = await fetch("https://localhost/catchevent/").then((result) => {
        return result.json();
    });
    console.log(event


    )
    const eventDisplay = document.getElementById("event")
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


async function set_bet() {
    let bets = await fetch("http://localhost/bet")
        .then((result) => result.json());

    let tbodyRef = document.getElementById('betTable').getElementsByTagName('tbody')[0]

    for (let i = 0; i < bets["bets"].length; i++) {
        let values = Object.values(bets["bets"][i])
        console.log(values)
        let newRow = tbodyRef.insertRow();
        let userCell = newRow.insertCell(0);

        userCell.innerHTML = values[0];
        let teamCell = newRow.insertCell(1);

        teamCell.innerHTML = values[1];
        let driveroneCell = newRow.insertCell(2);

        driveroneCell.innerHTML = values[2];
        let ploneCell = newRow.insertCell(3);
        ploneCell.innerHTML = values[3];

        let drivertwoCell = newRow.insertCell(4);
        drivertwoCell.innerHTML = values[4];

        let pltwoCell = newRow.insertCell(5);
        pltwoCell.innerHTML = values[5];

        let eventCell = newRow.insertCell(6);
        eventCell.innerHTML = values[6];
    }
}

async function send_bet() {
    const pl_one  = document.getElementById("member-one").value;
    const pl_two = document.getElementById("member-two").value;

    const driver_one = document.getElementById("driver_one").innerHTML;
    const driver_two = document.getElementById("driver_two").innerHTML;
    let selectElement = document.getElementById('team-select');
    const team = selectElement.options[selectElement.selectedIndex].text;
    const user = getCookie("username");



    const data = {
        user: user,
        team: team,
        first_driver: driver_one,
        first_pl: parseInt(pl_one),
        second_driver: driver_two,
        second_pl: parseInt(pl_two)
    };

    await fetch("http://localhost/insertbet", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
}

window.addEventListener("load", setup);
document.getElementById("team-select").addEventListener("change", set_drivers);
window.addEventListener("load", set_bet);
document.getElementById("WettButton").addEventListener("click", send_bet)



