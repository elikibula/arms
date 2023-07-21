function scrollToSection(targetId) {
    document.querySelector(targetId).scrollIntoView({
        behavior: 'smooth'
    });
}