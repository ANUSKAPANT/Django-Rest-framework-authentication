registerForm = document.querySelector('form');
error = document.querySelector('.message');


const registerUser = async (username, email, password) => {
	const api = 'http://127.0.0.1:8000/api/user-register/';
	const response = await fetch(api, {
              method: 'post',
              headers: { 
                  'Accept': 'application/json',
                  'Content-Type': 'application/json' 
              },
              body:JSON.stringify({'username': username, 'email' : email, 'password' : password})            
    });
    const data = await response.json()
    console.log(response);
    
};



registerForm.addEventListener('submit', e => {
	e.preventDefault();

	const username = registerForm.username.value.trim();
	const email  = registerForm.email.value.trim();
	const password = registerForm.password1.value.trim();
	const confirmPassword= registerForm.password2.value.trim();
	
	if(confirmPassword === password) {
		registerUser(username, email, password);
	}
	else{
		const html = `<p>Password doesn't match<p>`;
		error.innerHTML = html;
		error.classList.toggle('d-none');
	}

})


