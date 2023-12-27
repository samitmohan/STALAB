var attempt = 3;
function validate() {
    var un = document.getElementById("username").value;
    var pw = document.getElementById("password").value;
    if (un == "Form" && pw == '123') {
	alert("Login sucess");
	window.location = "success.html"; // redirect
	return false;
    } else {
	attempt--;
	alert("You have " + attempt + " attempts left");
	if (attempt == 0) {
	    document.getElementById("username").disabled = true;
	    document.getElementById("password").disabled = true;
	    document.getElementById("submit").disabled = true;
	    return false;
	}
    }
}
