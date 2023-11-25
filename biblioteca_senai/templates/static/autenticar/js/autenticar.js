const loginContainer = document.getElementById('login_container')
const btnCadastrar = document.getElementById('btnCadastrar')
const btnEntrar = document.getElementById('btnEntrar')
const aLogin = document.getElementById('registroMobileLogin')
const aCad = document.getElementById('registroMobileCad')

/*Recebe outra classe*/
btnCadastrar.addEventListener('click', () => {
    loginContainer.className = 'login_container move'
})

btnEntrar.addEventListener('click', () => {
    loginContainer.className = 'login_container'
})

aCad.addEventListener('click', () => {
    loginContainer.className = 'login_container move'
})

aLogin.addEventListener('click', () => {
    loginContainer.className = 'login_container'
})

// const password = document.querySelector('.strongPassword')
// var invisiblePassword = document.querySelector('#invisible-password')
// var visiblePassword = document.querySelector('#visible-password')
// const svg = document.querySelector('.icon-Password')

// svg.addEventListener('click', passwordFunction)
// function passwordFunction () {
//     if (password.type === 'password') { // se o tipo for de 'password', 
//         password.setAttribute('type', 'text') // mudar para tipo de 'text' para deixar visível
//         invisiblePassword.classList.add('hide') // adicionando uma classe para o ícone de senha invisível
//         visiblePassword.classList.add('hide') // adicionando uma classe para o ícone de senha visível
//     }
//     else {
//         password.setAttribute('type', 'password') // se o tipo for 'password' (invisível), voltar às configurações iniciais da senha (no CSS)
//         invisiblePassword.classList.remove('hide')
//         visiblePassword.classList.remove('hide')
//     }
// }

// gerador de senhas fortes

    // Obtém o elemento HTML com o ID "input-senhaForte"
    var senhaInput = document.querySelector("#input-senhaForte");
    // Função para gerar uma combinação de senha
    function generateP() {
        var pass = '';
        var str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
        var num = '0123456789';
        var especial = '@/-_#&%*$';

        // Função para gerar caracteres aleatórios de uma string
        function getRandomChar(charSet) {
            var char = Math.floor(Math.random() * charSet.length);
            return charSet.charAt(char);
        }

        for (var i = 0; i < 3; i++) {
            pass += getRandomChar(str);
            pass += getRandomChar(num);
            pass += getRandomChar(especial);
        }

        pass = pass.split('').sort(function () {
            return 0.5 - Math.random();
        }).join('');

        return pass;
    }

    // Função que executa a geração de senha e atualiza o valor do input
    function gfg_Run() {
        var senhaCopiar = document.querySelector("#icon-copiarSenha")
        var senhaGerada = generateP();
        senhaInput.value = senhaGerada; // Define o valor do input como a senha gerada
        senhaCopiar.style.display = 'block'
    }
function copiar () {
    navigator.clipboard.writeText(senhaInput.value).then(() => {
    })
}
    // Adiciona um ouvinte de evento ao botão para chamar a função gfg_Run
    var addSenha = document.querySelector("#icon-gerarSenha");
    addSenha.addEventListener('click', gfg_Run);
    
    var senhaCopiar = document.querySelector("#icon-copiarSenha")
    senhaCopiar.addEventListener('click', copiar)