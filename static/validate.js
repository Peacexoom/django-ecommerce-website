const username=document.getElementById("username");
const email=document.getElementById("email");
const password1=document.getElementById("password1");
const password2=document.getElementById("password2");


const usernameError=document.getElementById("username-error");
const emailError=document.getElementById("email-error");
const password1Error=document.getElementById("pass1-error");
const password2Error=document.getElementById("pass2-error");


function validate(){
    
    const usernameValue = username.value.trim();
	const emailValue = email.value.trim();
	const password1Value = password1.value.trim();
	const password2Value = password2.value.trim();

    if(usernameValue === ""){
        usernameError.innerHTML="Required"
        usernameError.style.display= 'block';
        return false;
    }
    else if(!(usernameValue.length<=25 && usernameValue.length>=3)){
        usernameError.innerHTML="There should be 3 to 25 characters"
        usernameError.style.display= 'block';
        return false;
    }
    else{
        usernameError.style.display= 'none';
    }

    if(emailValue === "") {
        emailError.innerHTML="Required"
        emailError.style.display= 'block';
        return false;
	} 
    else if (!isEmail(emailValue)) {
        emailError.innerHTML="Not a valid email"
        emailError.style.display= 'block';
        return false;
	} 
    else {
		emailError.style.display= 'none';
	}

    if(password1Value === "") {
        password1Error.innerHTML="Required"
        password1Error.style.display= 'block';
        return false;
	} 
    else if (password1Value.length < 8) {
        password1Error.innerHTML = "Password should be at least 8 characters";
        password1Error.style.display = 'block';
        return false;
    }
    else{
        password1Error.style.display= 'none';
    }
	
    if(password2Value === "") {
        password2Error.innerHTML="Required"
        password2Error.style.display= 'block';
        return false;
	} 
    else if(password1Value !== password2Value){
        password2Error.innerHTML="Passwords does not match"
        password2Error.style.display= 'block';
        return false;
    }
    else{
        password2Error.style.display= 'none';
    }

}

function isEmail(email) {
	return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}

