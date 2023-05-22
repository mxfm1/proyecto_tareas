document.getElementById("dropdown-btn").addEventListener("click", function() {
    var dropdownMenu = document.getElementById("dropdown-menu");
    if (dropdownMenu.style.display === "none") {
      dropdownMenu.style.display = "block";
    } else {
      dropdownMenu.style.display = "none";
    }
  });

  function confirmarBorrado() {
    if (confirm("¿Estás seguro de que quieres borrar esta tarea?")) {
        // Si se confirma el borrado, enviar el formulario
        return true;
    } else {
        // Si se cancela el borrado, no enviar el formulario
        return false;
    }
}