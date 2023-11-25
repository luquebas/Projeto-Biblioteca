/*
// Código anterior para rolagem suave
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();

    // Obtém o ID do elemento de destino da âncora clicada
    const targetId = this.getAttribute('href').substring(1);
    // Encontra o elemento de destino pelo ID
    const targetElement = document.getElementById(targetId);

    // Verifica se o elemento de destino existe
    if (targetElement) {
      // Rolagem suave até o elemento de destino
      targetElement.scrollIntoView({
        behavior: 'smooth',
        block: 'start',
      });
    }
  });
});
*/

// Definindo a classe MobileNavbar
class MobileNavbar {
  constructor(mobileMenu, navList, navLinks) {
    // Seleciona o elemento do menu móvel
    this.mobileMenu = document.querySelector(mobileMenu);
    // Seleciona a lista de navegação móvel
    this.navList = document.querySelector(navList);
    // Seleciona todos os links da lista de navegação móvel
    this.navLinks = document.querySelectorAll(navLinks);
    // Classe para ativar/desativar elementos móveis
    this.activeClass = "active";

    // Liga o método handleClick à instância atual da classe
    this.handleClick = this.handleClick.bind(this);
  }

  // Método para animar os links da navegação
  animateLinks() {
    this.navLinks.forEach((link, index) => {
      // Adiciona animação aos links para efeito de fade-in
      link.style.animation
        ? (link.style.animation = "")
        : (link.style.animation = `navLinkFade 0.5s ease forwards ${
            index / 7 + 0.3
          }s`);
    });
  }

  // Método para lidar com o clique no menu móvel
  handleClick() {
    // Alterna a classe 'active' na lista de navegação móvel
    this.navList.classList.toggle(this.activeClass);
    // Alterna a classe 'active' no menu móvel (ícone do hambúrguer)
    this.mobileMenu.classList.toggle(this.activeClass);
    // Chama o método para animar os links
    this.animateLinks();
  }

  // Adiciona um evento de clique ao menu móvel
  addClickEvent() {
    this.mobileMenu.addEventListener("click", this.handleClick);
  }

  // Inicializa a classe MobileNavbar
  init() {
    if (this.mobileMenu) {
      this.addClickEvent();
    }
    return this;
  }
}

// Cria uma instância da classe MobileNavbar e a inicializa
const mobileNavbar = new MobileNavbar(
  ".mobile-menu",
  ".nav-list",
  ".nav-list li",
);
mobileNavbar.init();

/* Código anterior comentado:

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();

    const targetId = this.getAttribute('href').substring(1);
    const targetElement = document.getElementById(targetId);

    if (targetElement) {
      targetElement.scrollIntoView({
        behavior: 'smooth',
        block: 'start',
      });
    }
  });
});

// Seletor para o ícone do menu de hambúrguer
const mobileMenu = document.querySelector('.mobile-menu');
mobileMenu.bind();
// Seletor para a lista de navegação móvel
const navList = document.querySelector('.nav-list');

// Adicione um ouvinte de eventos de clique ao ícone do menu de hambúrguer
mobileMenu.addEventListener('click', () => {
  // Toggle (alternar) a classe 'active' na lista de navegação móvel
  navList.classList.toggle('active');
});
*/
