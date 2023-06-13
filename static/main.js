function text(x) {

    if (x == 0) {
        document.getElementById("hidden_rn").style.display = "none";
        document.getElementById("hidden_rop").style.display = "none";
        document.getElementById("hidden_bo").style.display = "block";
        document.getElementById("hidden_ddd").style.display = "block";

    }
    else if (x == 1) {
        document.getElementById("hidden_rn").style.display = "none";
        document.getElementById("hidden_rop").style.display = "none";
        document.getElementById("hidden_bo").style.display = "none";
        document.getElementById("hidden_ddd").style.display = "block";

    } 
    else if (x == 2) {
        document.getElementById("hidden_rn").style.display = "block";
        document.getElementById("hidden_rop").style.display = "block";
        document.getElementById("hidden_bo").style.display = "none";
        document.getElementById("hidden_ddd").style.display = "none";
    }
    else if (x == 3) {
        document.getElementById("hidden_rn").style.display = "block";
        document.getElementById("hidden_rop").style.display = "block";
        document.getElementById("hidden_bo").style.display = "none";
        document.getElementById("hidden_ddd").style.display = "block";
    }

    
    return;
}