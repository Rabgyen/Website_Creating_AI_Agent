// Smooth scrolling for anchor links
document.addEventListener('DOMContentLoaded', () => {
    // Highlight active navigation item when scrolling
    const navLinks = document.querySelectorAll('.nav a');
    const sections = document.querySelectorAll('section[id]');

    let lastScrolledId = null;

    window.addEventListener('scroll', () => {
        const currentSection = document.querySelector(`#${document.activeElement.closest('section').id}`);
        if (currentSection) {
            lastScrolledId = currentSection.id;
        }

        navLinks.forEach(link => {
            link.classList.toggle('active', link.getAttribute('href') === `#${lastScrolledId}`);
        });
    });

    // Animate menu items on hover
    const menuItems = document.querySelectorAll('.menu-item');
    menuItems.forEach(item => {
        item.style.transition = 'all 0.3s ease';
    });
});