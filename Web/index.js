
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
