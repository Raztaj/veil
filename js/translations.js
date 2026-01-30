document.addEventListener('DOMContentLoaded', () => {
    const langToggleBtn = document.getElementById('lang-toggle');
    const htmlEl = document.documentElement;

    // Default to 'ar' if not set
    let currentLang = localStorage.getItem('lang') || 'ar';

    // Initial Load
    setLanguage(currentLang);

    langToggleBtn.addEventListener('click', (e) => {
        e.preventDefault();
        currentLang = currentLang === 'ar' ? 'en' : 'ar';
        setLanguage(currentLang);
    });

    function setLanguage(lang) {
        document.body.style.opacity = '0';
        document.body.style.transition = 'opacity 0.3s ease';

        setTimeout(() => {
            localStorage.setItem('lang', lang);
            htmlEl.setAttribute('lang', lang);
            htmlEl.setAttribute('dir', lang === 'ar' ? 'rtl' : 'ltr');

            // Load JSON file
            fetch(`${lang}.json`)
                .then(response => response.json())
                .then(translations => {
                    applyTranslations(translations);
                    updateToggleButton(lang);
                    document.body.style.opacity = '1';
                })
                .catch(error => {
                    console.error('Error loading translations:', error);
                    document.body.style.opacity = '1';
                });
        }, 300);
    }

    function applyTranslations(translations) {
        const elements = document.querySelectorAll('[data-i18n]');
        elements.forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (translations[key]) {
                // If it's an input with placeholder, update placeholder
                if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
                    el.placeholder = translations[key];
                } else {
                    el.textContent = translations[key];
                }
            }
        });
    }

    function updateToggleButton(lang) {
        // Handled by data-i18n="lang_toggle"
    }

    // Mobile Menu Toggle
    const mobileToggle = document.querySelector('.header__mobile-toggle');
    const nav = document.querySelector('.header__nav');
    if (mobileToggle && nav) {
        mobileToggle.addEventListener('click', () => {
            nav.classList.toggle('active');
        });
    }
});
