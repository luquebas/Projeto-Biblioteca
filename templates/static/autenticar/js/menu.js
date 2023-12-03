//Seleciona os itens clicado
var menuItem = document.querySelectorAll('.item-menu')

function selectLink(){
    menuItem.forEach((item)=>
        item.classList.remove('ativo')
    )
    this.classList.add('ativo')
}

// para cada item do menu (menuItem)
menuItem.forEach((item)=>
    item.addEventListener('click', selectLink)
)

//Expandir o menu
var btnExp = document.querySelector('#btn-exp')
var menuSide = document.querySelector('.menu-lateral')

// add evento ao botão 
btnExp.addEventListener('click', function(){
    menuSide.classList.toggle('expandir')
})


// dark mode
const btnJs = document.getElementById("tema-dark"); // Pegando o botão do HTML
btnJs.addEventListener('click', alternarTema); // Adicionando função ao botão

function alternarTema() {
    // guardando elementos em variáveis
    const body = document.body;
    const sidebarJs = document.querySelector('.menu-lateral');
    const btnJs = document.querySelector('#tema-dark');
    const h1 = document.querySelector('.h1-emprestimo-livros');
    const icons = document.querySelectorAll('.item-menu');

    // se body conter a classe '.dark'
    if (body.classList.contains('dark')) {
        // Modo claro
        // remover 
        body.classList.remove('dark');
        sidebarJs.classList.remove('dark'); // Remova a classe 'dark' da barra lateral
        btnJs.classList.remove('dark');

        icons.forEach((icon) => {
            icon.classList.remove('dark');
        });
    } else {
        // Modo escuro
        body.classList.add('dark');
        sidebarJs.classList.add('dark'); // Adicione a classe 'dark' à barra lateral
        btnJs.classList.add('dark');
        
        icons.forEach((icon) => {
            icon.classList.add('dark');
        });
    }
}

const openModalButton = document.querySelector("#cadLivro");
const openModalBtn = document.querySelector("#cadEmprestimo");
const closeModalButton = document.querySelector("#close-modal");
const closeModalBtn = document.querySelector("#close");
const modal = document.querySelector("#modal");
const fade = document.querySelector("#fade");
const modale = document.querySelector("#modale");
const fader = document.querySelector("#fader");
const btnPDF = document.querySelector('#gerarpdf')


// Função para alternar a visibilidade do modal e do fade
const toggleModal = () => {
    modal.classList.toggle("hide"); // Adiciona ou remove a classe "hide" do elemento modal
    fade.classList.toggle("hide");   // Adiciona ou remove a classe "hide" do elemento fade
};

// Adiciona um evento de clique aos elementos openModalButton, closeModalButton e fade,
// que chamará a função toggleModal quando clicados.
[openModalButton, closeModalButton, fade].forEach((el) => {
    el.addEventListener("click", () => toggleModal());
});

// Função para alternar a visibilidade de um segundo modal e de um segundo fade
const toggleModas = () => {
    modale.classList.toggle("hide"); // Adiciona ou remove a classe "hide" do elemento modale
    fader.classList.toggle("hide");  // Adiciona ou remove a classe "hide" do elemento fader
};

// Adiciona um evento de clique aos elementos openModalBtn, closeModalBtn e fader,
// que chamará a função toggleModas quando clicados.
[openModalBtn, closeModalBtn, fader].forEach((el) => {
    el.addEventListener("click", () => toggleModas());
});

