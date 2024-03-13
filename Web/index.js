import {getCookie} from "./Utility.js";

async function setup() {
    await read_username();
    await read_teams();
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
        content += "<option value="+i+">"+ teams["teams"][i]["_Team__name"] + "</option>"
    }
    const combo_teams = document.getElementById("team-select");
    combo_teams.innerHTML += content;
}

window.addEventListener("load", setup);

let team = ""
let driverOne = document.getElementById("member-one").value
let driverTwo = document.getElementById("member-two").value

if (driverOne < 0 && driverTwo < 0) {
    var but = document.getElementById("WettButton");
    but.disabled = true;
}

document.getElementById("team-select").addEventListener("change", function() {
    team = this.value;
    var labelone = document.querySelector('label[for="member-one"]');
    labelone.textContent = "Mazepin:";
    var labeltwo = document.querySelector('label[for="member-two"]');
    labeltwo.textContent = "Latifi:";
});

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
