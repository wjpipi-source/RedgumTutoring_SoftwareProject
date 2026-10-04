document.addEventListener('DOMContentLoaded', () => {
    const mobileToggle = document.querySelector('.mobile-toggle');
    const sidebar = document.querySelector('.sidebar');

    if (mobileToggle && sidebar) {
        mobileToggle.addEventListener('click', () => {
            sidebar.classList.toggle('is-open');
        });
    }

    document.querySelectorAll('.confirm-delete').forEach((button) => {
        button.addEventListener('click', (event) => {
            const message = button.dataset.message || 'Are you sure you want to continue?';
            const shouldDelete = window.confirm(message);
            if (!shouldDelete) {
                event.preventDefault();
            }
        });
    });

    const forms = document.querySelectorAll('.needs-validation');
    forms.forEach((form) => {
        form.addEventListener('submit', (event) => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });

    const scheduleButtons = document.querySelectorAll('.schedule-toggle .btn');
    scheduleButtons.forEach((button) => {
        button.addEventListener('click', () => {
            scheduleButtons.forEach((item) => {
                item.classList.remove('active', 'btn-primary');
                item.classList.add('btn-outline-secondary');
            });
            button.classList.remove('btn-outline-secondary');
            button.classList.add('btn-primary', 'active');
        });
    });

    document.querySelectorAll('input[type="search"]').forEach((input) => {
        input.addEventListener('input', () => {
            const value = input.value.trim().toLowerCase();
            const table = input.closest('.toolbar')?.nextElementSibling?.querySelector('table');
            if (!table) return;

            const rows = table.querySelectorAll('tbody tr');
            rows.forEach((row) => {
                const text = row.textContent.toLowerCase();
                row.style.display = text.includes(value) ? '' : 'none';
            });
        });
    });
});
