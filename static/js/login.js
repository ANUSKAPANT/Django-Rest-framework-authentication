loginForm = document.querySelector('form');


const loginUser = async(username, password) => {
	const api = 'http://127.0.0.1:8000/api/api-auth-token/';
	const response = await fetch(api,{
					method : 'post',
					headers: { 
	                  'Accept': 'application/json',
	                  'Content-Type': 'application/json',  
	              	},
					body : JSON.stringify({'username':username, 'password':password})
	});
	const data = await response.json();	
	console.log(data.token);
	if(data.token){
		location.href = "/home/";
	}

	

};

loginForm.addEventListener('submit', e => {
	e.preventDefault();
	username = loginForm.username.value.trim();
	password = loginForm.password.value.trim();

	loginUser(username, password);
});