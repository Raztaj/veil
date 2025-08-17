document.addEventListener('DOMContentLoaded', () => {
    // Animated Counters
    const counters = document.querySelectorAll('.result-metric');
    const speed = 200; // The lower the slower

    const animateCounter = (counter) => {
        const target = +counter.getAttribute('data-target');
        // Initialize counter text if it's not a number
        counter.innerText = '+0%';

        const updateCount = () => {
            const count = +counter.innerText.replace('+', '').replace('%', '');
            const inc = target / speed;

            if (count < target) {
                counter.innerText = `+${Math.ceil(count + inc)}`;
                setTimeout(updateCount, 15);
            } else {
                counter.innerText = `+${target}%`;
            }
        };
        updateCount();
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.8
    });

    counters.forEach(counter => {
        observer.observe(counter);
    });

    // Simple hover effect for service icons
    const serviceItems = document.querySelectorAll('.service-item');
    serviceItems.forEach(item => {
        item.addEventListener('mouseenter', () => {
            item.style.transform = 'translateY(-5px)';
        });
        item.addEventListener('mouseleave', () => {
            item.style.transform = 'translateY(0)';
        });
        item.style.transition = 'transform 0.3s ease';
    });

    // Portfolio Filtering
    const filterButtons = document.querySelectorAll('.filters .filter-button');
    const portfolioItems = document.querySelectorAll('.portfolio-grid .portfolio-item');

    if (filterButtons.length > 0 && portfolioItems.length > 0) {
        filterButtons.forEach(button => {
            button.addEventListener('click', () => {
                // Set active class on button
                filterButtons.forEach(btn => btn.classList.remove('active'));
                button.classList.add('active');

                const filter = button.getAttribute('data-filter');

                portfolioItems.forEach(item => {
                    item.style.display = 'none'; // hide all items first
                    if (filter === 'all' || item.getAttribute('data-category').includes(filter)) {
                        item.style.display = 'block'; // then show the ones that match
                    }
                });
            });
        });
    }
});
