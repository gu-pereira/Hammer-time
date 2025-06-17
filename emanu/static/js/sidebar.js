// Mostrar/ocultar sidebar em dispositivos pequenos
document.getElementById("sidebarToggle").addEventListener("click", function () {
    const sidebar = document.getElementById("sidebar");
    sidebar.classList.toggle("show");
});

// Minimizar/maximizar sidebar em dispositivos maiores
document.getElementById("sidebarMinimize").addEventListener("click", function () {
    const sidebar = document.getElementById("sidebar");
    const spans = sidebar.querySelectorAll(".menu-text");

    if (sidebar.classList.contains("minimized")) {
        // Expandir
        sidebar.classList.remove("minimized");
        this.querySelector("i").classList.replace("bi-chevron-double-right", "bi-chevron-double-left");
        spans.forEach(span => span.style.display = "inline");
    } else {
        //  Minimizar
        sidebar.classList.add("minimized");
        this.querySelector("i").classList.replace("bi-chevron-double-left", "bi-chevron-double-right");
        spans.forEach(span => span.style.display = "none");
    }
});