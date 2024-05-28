const API_URL_CLIENTES = "http://127.0.0.1:8000/APIclientes"

// ------------------------------------------- CLIENTES LISTVIEW -------------------------------------------

fetch(API_URL_CLIENTES)
    .then(response => response.json())
    .then(json => {
        addRowsClientes(json);
    });

function addRowsClientes(clientes) {
    tbody = document.querySelector("#fetchCliente");
    if(tbody) {
        clientes.forEach(element => {
            tbody.appendChild(createClienteRow(element));
        });
    }
}

function createClienteRow(cliente){
    let row = document.createElement("tr");

    let name = document.createElement("td");
    let link_detail = document.createElement("a");
        link_detail.setAttribute('href', "http://127.0.0.1:8000/clientes/"+cliente.id);
        link_detail.innerHTML = cliente.nombre;
        name.append(link_detail);
        row.appendChild(name);

    let tel = document.createElement("td");
        tel.textContent = cliente.telefono;
        row.appendChild(tel);

    let address = document.createElement("td")
        address.textContent = cliente.direccion;
        row.appendChild(address);
    
    let link_row = document.createElement("td");
        link_row.className = "btn-tablas";
    let link_edit = document.createElement("a");
        link_edit.setAttribute('href', "http://127.0.0.1:8000/clientes/"+cliente.id+"/editar");
        link_edit.className = "btn btn-secondary";
        link_edit.innerHTML = "Editar";
        link_row.append(link_edit);
    let link_delete = document.createElement("a")
        link_delete.setAttribute('href', "http://127.0.0.1:8000/clientes/"+cliente.id+"/borrar");
        link_delete.className = "btn btn-danger";
        link_delete.innerHTML = "Borrar";
        link_row.append(link_delete);
        row.appendChild(link_row);
    console.log(row);
    return row;
}

// --------------------------------------------------------------------------------------------------------