// Obtener los elementos de texto
var subheadings = document.getElementsByClassName("subheading");

// Obtener los botones de aumento y disminución
var increaseButton = document.getElementById("increase");
var decreaseButton = document.getElementById("decrease");

const toggleButtons = document.querySelectorAll(".toggle-table");
const tables = document.querySelectorAll(".tablas");
const titles = document.querySelectorAll(".subheading");
const seeMoreButtons = document.querySelectorAll("a.btn");

toggleButtons.forEach(function (button, index) {
  button.addEventListener("click", function () {
    // Verificar si la tabla está oculta
    if (tables[index].style.display === "none") {
      // Mostrar el título correspondiente
      titles[index].style.display = "block";

      // Mostrar la tabla correspondiente
      tables[index].style.display = "table";

      seeMoreButtons[index].style.display = "";

      // Cambiar el texto del botón a "Ocultar"
      this.textContent = "Ocultar";
    } else {
      // Ocultar el título correspondiente
      titles[index].style.display = "none";

      // Ocultar la tabla correspondiente
      tables[index].style.display = "none";

      seeMoreButtons[index].style.display = "none";

      // Cambiar el texto del botón a "Expandir"
      this.textContent = "Expandir";
    }
  });
});

// Agregar el evento al botón de aumento
if (increaseButton) {
  increaseButton.addEventListener("click", function () {
    increaseFontSize();
  });
}

// Agregar el evento al botón de disminución
if (decreaseButton) {
  decreaseButton.addEventListener("click", function () {
    decreaseFontSize();
  });
}

// Función para aumentar el tamaño de fuente
function increaseFontSize() {

  for (var i = 0; i < subheadings.length; i++) {
    var currentSize = parseInt(
      window.getComputedStyle(subheadings[i]).fontSize
    );
    subheadings[i].style.fontSize = currentSize + 2 + "px";
  }

  var tables = document.getElementsByClassName("tablas");

  for (var i = 0; i < tables.length; i++) {
    var cells = tables[i].getElementsByTagName("td");

    for (var j = 0; j < cells.length; j++) {
      var currentFontSize = parseFloat(
        window.getComputedStyle(cells[j]).fontSize
      );
      cells[j].style.fontSize = currentFontSize + 1 + "px";
    }
  }
}

// Función para disminuir el tamaño de fuente
function decreaseFontSize() {

  for (var i = 0; i < subheadings.length; i++) {
    var currentSize = parseInt(
      window.getComputedStyle(subheadings[i]).fontSize
    );
    subheadings[i].style.fontSize = currentSize - 2 + "px";
  }

  var tables = document.getElementsByClassName("tablas");

  for (var i = 0; i < tables.length; i++) {
    var cells = tables[i].getElementsByTagName("td");

    for (var j = 0; j < cells.length; j++) {
      var currentFontSize = parseFloat(
        window.getComputedStyle(cells[j]).fontSize
      );
      cells[j].style.fontSize = currentFontSize - 1 + "px";
    }
  }
}

function validarFormularioProyecto() {
  const fecha_inicio = document.getElementById(
    "fecha_inicio"
  ).value;
  const fecha_fin = document.getElementById(
    "fecha_fin"
  ).value;
  const hoy = new Date().toISOString().split("T")[0];
  var mensaje = document.getElementById("mensaje");

  // Realiza la validación comparando las fechas
  if (fecha_inicio < hoy) {
    mensaje.textContent =
      "La fecha de inicio de un proyecto debe ser mayor o igual al día de hoy.";
    return false;
  } else {
    mensaje.textContent = ""; // Limpiar el mensaje si los campos son válidos
  }

  if (fecha_fin <= fecha_inicio) {
    mensaje.textContent =
      "La fecha de finalización de un proyecto debe ser mayor al día de comienzo del proyecto.";
    return false;
  } else {
    mensaje.textContent = ""; // Limpiar el mensaje si los campos son válidos
  }

  // Si todas las validaciones son exitosas, enviar el formulario
  return true;
}