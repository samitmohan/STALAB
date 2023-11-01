var attempt = 3; // Variable to count the number of login attempts.

// Function that executes on click of the login button.
function validate() {
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;

  if (username === "Form" && password === "123") {
    alert("Login successful");
    window.location = "success.html"; // Redirect to another page.
    return false;
  } else {
    attempt--; // Decrement the attempt count.
    alert("You have " + attempt + " attempt(s) left.");

    // Disable fields after 3 unsuccessful attempts.
    if (attempt === 0) {
      document.getElementById("username").disabled = true;
      document.getElementById("password").disabled = true;
      document.getElementById("submit").disabled = true;
      return false;
    }
  }
}

