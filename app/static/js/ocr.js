function createTr(item, quantidade) {
    let tr = document.createElement('tr');

    let th = document.createElement('th');
    let th2 = document.createElement('th');
    let th3 = document.createElement('th');
    let btnHtml = "<th><a class='btn btn-primary' onclick='excluir(this)' href='javascript:void(0)'>Excluir</a></th>";
    th3.innerHTML = btnHtml;
   
    th.appendChild(document.createTextNode(item));
    th2.appendChild(document.createTextNode(quantidade));
    
    tr.appendChild(th);
    tr.appendChild(th2);
    tr.appendChild(th3);

    return tr;
}


function excluir(el) {
    el.parentElement.parentElement.remove();
  }
  

function submitForm(event) {
    event.preventDefault();
    let form = document.getElementById('form-extract');
    let url = document.getElementById('form-extract').action;
    let data = new FormData(form);
    const xhr = new XMLHttpRequest();
    xhr.open('POST', url, true);
    xhr.onload = function () {
        let dados = JSON.parse(this.responseText);
        
        dados.forEach(element => {
            document.getElementById('tbody').appendChild(createTr(element.item, element.quantidade));
        });
        
    };
    xhr.send(data);
}

document.getElementById('form-extract').addEventListener("submit", submitForm, true);


  
document.getElementById('btn-save').onclick = () => {
    let item = document.getElementById('item').value;
    let quantidade = document.getElementById('quantidade').value;

    if (!item ?? '') {
        alert('O campo Item é obrigatório.');
        return;
    }

    if (!quantidade ?? '') {
        alert('O campo Quantidade é obrigatório.');
        return;
    }
    
    document.getElementById('tbody').appendChild(createTr(item, quantidade));
    document.getElementById('item').value = '';
    document.getElementById('quantidade').value = '';
    document.getElementById('exampleModal').click();
};

