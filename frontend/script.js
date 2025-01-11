const API_URL = 'http://localhost:8000/api/';

// Função para login
function login(event) {
    event.preventDefault()
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;

    const data = { username, password };

    fetch(API_URL + 'accounts/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        const loginMessage = document.getElementById('login-message');
        if (data.access) {
            loginMessage.textContent = 'Login bem-sucedido!';
            loginMessage.style.color = 'green';
            localStorage.setItem('access_token', data.access); // Armazena o token
        } else {
            loginMessage.textContent = 'Erro de login.';
            loginMessage.style.color = 'red';
        }
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}

// Função para cadastrar novo estudante
function registerStudent() {
    const name = document.getElementById('student-name').value;
    const age = document.getElementById('student-age').value;

    const data = { name, age };

    fetch(API_URL + 'students', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + localStorage.getItem('access_token'),  // Autenticação com o token
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        const registerMessage = document.getElementById('register-message');
        if (data.id) {
            registerMessage.textContent = 'Estudante cadastrado com sucesso!';
            registerMessage.style.color = 'green';
        } else {
            registerMessage.textContent = 'Erro ao cadastrar estudante.';
            registerMessage.style.color = 'red';
        }
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}

// Função para listar estudantes
function fetchStudents() {
    fetch(API_URL + 'students', {
        method: 'GET',
        headers: {
            'Authorization': 'Bearer ' + localStorage.getItem('access_token'),
        },
    })
    .then(response => response.json())
    .then(data => {
        const studentsList = document.getElementById('students');
        studentsList.innerHTML = '';  // Limpa a lista antes de adicionar novos estudantes
        data.forEach(student => {
            const li = document.createElement('li');
            li.textContent = `${student.name} (Idade: ${student.age})`;
            studentsList.appendChild(li);
        });
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}
