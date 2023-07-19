function validate() {
    var pass = document.getElementById("password").value;
    var cpass = document.getElementById("cpassword").value;
    if (pass == cpass) {
        return true;
    } else {
        alert("Passwords do not match");
        return false;
    }
}

function validateOTP() {
    var otpCode = document.getElementById("otpCode").value;
    if (otpCode == "abc123") {
        return true;
    } else {
        return false;
    }
}


