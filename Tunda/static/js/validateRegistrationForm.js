var registrationForm = document.getElementById('registration-form');
var emailField = document.getElementById('id_email');

//console.log(Object.getOwnPropertyNames(emailField))
emailField.onkeyup= function(){
    emailValue= document.getElementById('id_email').value;
    var atpostion = emailValue.indexOf('@');
    var dotposition = emailValue.indexOf('.');

    if (atposition< 1 || dotposision<atposition+2 || dotposition+2>=emailValue.length) {
        alert("Not a valid e-mail address");
        return false;
    }
}

var submitForm = document.getElementById('submit-registration-form');