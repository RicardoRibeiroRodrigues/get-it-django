const xhr = new XMLHttpRequest();

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}


document.addEventListener("DOMContentLoaded", function () {
  // Faz textarea aumentar a altura automaticamente
  // Fonte: https://www.geeksforgeeks.org/how-to-create-auto-resize-textarea-using-javascript-jquery/#:~:text=It%20can%20be%20achieved%20by,height%20of%20an%20element%20automatically.
  let textareas = document.getElementsByClassName("autoresize");
  for (let i = 0; i < textareas.length; i++) {
    let textarea = textareas[i];
    let tamanho = window.screen.width * 0.014;
    if (textarea.classList.contains("tituloIN")) {
      tamanho = window.screen.width * 0.01;
    }
    // Coloca automaticamente um numero de rows adequado para o conteudo.
    breaks = Math.floor(textarea.value.length / tamanho)
    textarea.rows = 1 + breaks;

    function autoResize() {
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    }

    textarea.addEventListener("input", autoResize, false);
  }

  // Sorteia classes de cores aleatoriamente para os cards
  let cards = document.getElementsByClassName("card");
  for (let i = 0; i < cards.length; i++) {
    let card = cards[i];
    card.className += ` card-color-${getRandomInt(
      1,
      5
    )} card-rotation-${getRandomInt(1, 11)}`;
  }

  // script para adicionar as tags.
  let botoes_tag = document.getElementsByClassName("update-tag");
  for (let botao_tag of botoes_tag) {
    botao_tag.addEventListener("click", async function (e) {
      console.log(`Entrou no update-tag, id=${this.id}`);
      // Cria um elemento para adicionar a tag
      barra_tag = document.getElementById(`${this.id}`).getElementsByClassName("tag-bar")[0];
      barra_tag.style.display = 'block';
      await new Promise(r => setTimeout(r, 100));
      barra_tag.style.transform = 'translate(150px)';
      barra_tag.style.transitionDuration = '0.2s';
    });
  }

  // Faz a requisicao do delete com o JS
  function delete_item() {
    let botao = document.getElementsByClassName("del");
    for (let i = 0; i < botao.length; i++) {
      element = botao[i];
      element.addEventListener("click", function (e) {
        console.log(`Entrou na funcao id=${this.id}`);
        const path = `/delete/${this.id}`
        console.log(path)
        xhr.open('DELETE', path, true);

        xhr.send(null);

        xhr.onload = () => {
          for (let i = 0; i < cards.length; i++) {
            if (cards[i].id == this.id) {
              cards[i].remove();

              // Chama a funcao novamente para recarregar a lista de cards e botoes.
              delete_item();
            }
          }
          console.log(xhr.response);
        }
      }, false);
    }
  }
  // Chama ela quando o conteúdo da pagina e carregado
  delete_item();
});