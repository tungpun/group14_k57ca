function validateLoginUsername()
{
    var login_username = document.forms["login"]["username"].value;
    document.getElementById("logLoginUsername").innerHTML = "Ok"
    if (login_username.length < 3) {
        document.getElementById("logLoginUsername").innerHTML = "Length of username is too short. Try again!";
    }
    for (var i = 0; i < login_username.length; i++) {
        var c = login_username[i];
        if (isNaN(c)) {
            if (! (('A' <= c && c <= 'Z') || ('a' <= c && c <= 'z')) ) {
                document.getElementById("logLoginUsername").innerHTML = "Username must only contain numbers or letters";
                return false;
            }
        }
    }
}

function validateLoginPassword() {
    document.getElementById("logLoginPassword").innerHTML = "Ok";
    var login_password = document.forms["login"]["password"].value;
    if (login_password.length < 6) {
        document.getElementById("logLoginPassword").innerHTML = "Length of password is too short. Try again!";
        return false;
    }
}

function validateRegisterUsername()
{
    var register_username = document.forms["register"]["username"].value;
    document.getElementById("logRegisterUsername").innerHTML = "Ok"
    if (register_username.length < 3) {
        document.getElementById("logRegisterUsername").innerHTML = "Length of username is too short. Try again!";
    }
    for (var i = 0; i < register_username.length; i++) {
        var c = register_username[i];
        if (isNaN(c)) {
            if (! (('A' <= c && c <= 'Z') || ('a' <= c && c <= 'z')) ) {
                document.getElementById("logRegisterUsername").innerHTML = "Username must only contain numbers or letters";
                return false;
            }
        }
    }
}

function validateRegisterFirstname()
{
    var register_firstname = document.forms["register"]["first_name"].value;
    document.getElementById("logRegisterFirstname").innerHTML = "Ok"
    if (register_firstname.length < 3) {
        document.getElementById("logRegisterFirstname").innerHTML = "Length of your first name is too short. Try again!";
    }
    for (var i = 0; i < register_firstname.length; i++) {
        var c = register_firstname[i];
        if (! (('A' <= c && c <= 'Z') || ('a' <= c && c <= 'z')) ) {
            document.getElementById("logRegisterFirstname").innerHTML = "Firstname must only contain numbers or letters";
            return false;
        }
    }
}


function validateRegisterLastname()
{
    var register_lastname = document.forms["register"]["last_name"].value;
    document.getElementById("logRegisterLastname").innerHTML = "Ok"
    if (register_lastname.length < 3) {
        document.getElementById("logRegisterLastname").innerHTML = "Length of your last name is too short. Try again!";
    }
    for (var i = 0; i < register_lastname.length; i++) {
        var c = register_lastname[i];
        if (! (('A' <= c && c <= 'Z') || ('a' <= c && c <= 'z')) ) {
                document.getElementById("logRegisterLastname").innerHTML = "Lastname must only contain numbers or letters";
                return false;
        }
    }
}

function validateRegisterEmail() {
    var register_email = document.forms["register"]["email"].value;
    document.getElementById("logRegisterEmail").innerHTML = "Ok"
    var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if (!re.test(register_email)) {
        document.getElementById("logRegisterEmail").innerHTML = "Invalid email!"
    }
}

function validateRegisterPassword()
{
    var register_password = document.forms["register"]["password"].value;
    document.getElementById("logRegisterPassword").innerHTML = "Ok"
    if (register_password.length < 6) {
        document.getElementById("logRegisterPassword").innerHTML = "Length of password is too short. Try again!";
        return false;
    }
}


function validateRegisterRPassword()
{
    var register_password = document.forms["register"]["password"].value;
    var register_rpassword = document.forms["register"]["rpassword"].value;
    document.getElementById("logRegisterRPassword").innerHTML = "Ok"

    if  (register_password != register_rpassword) {
        document.getElementById("logRegisterRPassword").innerHTML = "Password does not match the confirm password. Try again!";
        return false;
    }
}

function validateRegisterMobile()
{
    var register_mobile = document.forms["register"]["mobile"].value;
    document.getElementById("logRegisterMobile").innerHTML = "Ok";

    if (register_mobile[0] != '0') {
        if (register_mobile.length < 12 || register_mobile.length > 13) {
             document.getElementById("logRegisterMobile").innerHTML = "Invalid mobile number";
            return false;
        }
        if (register_mobile[0] == '+') {
            if (register_mobile[1] == '8') {
                if (register_mobile[2] != '4') {
                    document.getElementById("logRegisterMobile").innerHTML = "Invalid mobile number";
                    return false;
                }
            }
            else {
                document.getElementById("logRegisterMobile").innerHTML = "Invalid mobile number";
                return false;
            }
        }
        else {
            document.getElementById("logRegisterMobile").innerHTML = "Invalid mobile number";
            return false;
        }
    }
    else {
        if (register_mobile.length < 10 || register_mobile.length > 11) {
            document.getElementById("logRegisterMobile").innerHTML = "Invalid mobile number";
            return false;
        }
    }
}

function validateRegisterAddress()
{
    var register_address = document.forms["register"]["address"].value;
    document.getElementById("logRegisterAddress").innerHTML = "Ok"

    for (var i = 0; i < register_address.length; i++) {
        var c = register_address[i];
        if (isNaN(c)) {
            if (! (('A' <= c && c <= 'Z') || ('a' <= c && c <= 'z') || (c == ',')) ) {
                document.getElementById("logRegisterAddress").innerHTML = "Invalid address. Try again!";
                return false;
            }
        }
    }
}


function validateRegisterAge()
{
    var register_age = document.forms["register"]["age"].value;
    document.getElementById("logRegisterAge").innerHTML = "Ok"
    for (var i = 0; i < register_age.length; i++) {
        var c = register_age[i];
        if (isNaN(c)) {
            document.getElementById("logRegisterAge").innerHTML = "Plz type your age. Try again!";
            return false;
        }
    }
}


function validateLoginForm()
{

    var login_username = document.forms["login"]["username"].value;
    var login_password = document.forms["login"]["password"].value;
    if (login_username.length < 3) {
        alert("Length of username is too short. Try again!");
        return false;
    }
    if (login_username.length > 20) {
        alert("Length of username is too long. Try again!");
        return false;
    }
    if (login_password.length < 6) {
        alert("Length of password is too short. Try again!");
        return false;
    }
    for (var i = 0; i < login_username.length; i++) {
        var c = login_username[i];
        if (isNaN(c)) {
            if (! (('A' <= c && c <= 'Z') || ('a' <= c && c <= 'z')) ) {
                alert("Username must only contain numbers or letters")
                return false;
            }
        }
    }
    alert("Login completed")
    return true;
}

function validateRegisterForm()
{
    var register_username = document.forms["register"]["username"].value;
    var register_password = document.forms["register"]["password"].value;
    var register_rpassword = document.forms["register"]["rpassword"].value;
    var register_mobile = document.forms["register"]["mobile"].value;
    var register_address = document.forms["register"]["address"].value;
    var register_age = document.forms["register"]["age"].value;
    var register_email = document.forms["register"]["email"].value;

    if (register_username.length < 3) {
        alert("Length of username is too short. Try again!");
        return false;
    }
    if (register_username.length > 20) {
        alert("Length of username is too long. Try again!");
        return false;
    }

     if (validateRegisterFirstname()) {
        alert("Invalid firstname")
        return false;
    }

    if (validateRegisterLastname()) {
        alert("Invalid lastname")
        return false;
    }


    var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if (!re.test(register_email)) {
        alert("Invalid email. Try again!");
        return false;
    }

    if (register_password.length < 6) {
        alert("Length of password is too short. Try again!");
        return false;
    }
    for (var i = 0; i < register_username.length; i++) {
        var c = register_username[i];
        if (isNaN(c)) {
            if (! (('A' <= c && c <= 'Z') || ('a' <= c && c <= 'z')) ) {
                alert("Username must only contain numbers or letters. Try again!")
                return false;
            }
        }
    }
    if  (register_password != register_rpassword) {
        alert("Password does not match the confirm password. Try again!");
        return false;
    }

    if (register_mobile[0] != '0') {
        if (register_mobile.length < 12 || register_mobile.length > 13) {
            alert("Invalid mobile number");
            return false;
        }
        if (register_mobile[0] == '+') {
            if (register_mobile[1] == '8') {
                if (register_mobile[2] != '4') {
                    alert("Invalid mobile number");
                    return false;
                }
            }
            else {
                alert("Invalid mobile number");
                return false;
            }
        }
        else {
            alert("Invalid mobile number");
            return false;
        }
    }
    else {
        if (register_mobile.length < 10 || register_mobile.length > 11) {
            alert("Invalid mobile number");
            return false;
        }
    }

    for (var i = 0; i < register_address.length; i++) {
        var c = register_address[i];
        if (isNaN(c)) {
            if (! (('A' <= c && c <= 'Z') || ('a' <= c && c <= 'z') || (c == ',')) ) {
                alert("Invalid address. Try again!")
                return false;
            }
        }
    }

    for (var i = 0; i < register_age.length; i++) {
        var c = register_age[i];
        if (isNaN(c)) {
            alert("Plz type your age. Try again!")
            return false;
        }
    }



    return true;
}



