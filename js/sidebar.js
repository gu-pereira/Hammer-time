const toggleDropdown = (dropdown, menu, isOpen) => {
    dropdown.classList.toggle('open', isOpen);
    menu.style.height = isOpen ? `${menu.scrollHeight}px` : 0;
}

const closeAllDropdowns = () => {
    document.querySelectorAll('.dropdown-container.open').forEach(openDropdown => {
        toggleDropdown(openDropdown, openDropdown.querySelector('.dropdown'), false);

    });
}

document.querySelectorAll('.dropdown-opcao').forEach(dropdownToggle => {
    dropdownToggle.addEventListener('click', e => {
        e.preventDefault();
        
        const dropdown = e.target.closest('.dropdown-container');
        const menu = dropdown.querySelector('.dropdown');
        const isOpen = dropdown.classList.contains('open');

        toggleDropdown(dropdown, menu, !isOpen);
    });
})

document.querySelector(".sidebar-toggler").addEventListener("click", () => {
    closeAllDropdowns();
    
    // Toggle collapsed class on sidebar
    document.querySelector(".sidebar").classList.toggle("collapsed");
    document.querySelector(".main").classList.toggle("collapsed");
    document.querySelector(".header").classList.toggle("collapsed");
})