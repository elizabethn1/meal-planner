let diet, restrictions, planLength;

document.getElementById("submit").onclick = function(event) {
    event.preventDefault();

    diet = document.getElementById("diet").value;
    restrictions = document.getElementById("restrictions").value;
    planLength = document.getElementById("planLength").value;

    console.log(diet);
    console.log(restrictions);
    console.log(planLength);
}