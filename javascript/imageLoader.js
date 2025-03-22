document.addEventListener('DOMContentLoaded', function() {
    // Get all project images
    const images = document.querySelectorAll('.project img');
    
    // Create intersection observer
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                // Start loading the image
                if (img.dataset.src) {
                    img.src = img.dataset.src;
                    img.classList.add('loading');
                    
                    img.onload = () => {
                        img.classList.remove('loading');
                        img.classList.add('loaded');
                    }
                    
                    // Stop observing the image
                    observer.unobserve(img);
                }
            }
        });
    });
    
    // Observe each image
    images.forEach(img => {
        imageObserver.observe(img);
    });
}); 