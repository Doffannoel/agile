document.addEventListener('DOMContentLoaded', function() {
    const viewDetailsBtns = document.querySelectorAll('.view-details-btn');
    const hideDetailsBtns = document.querySelectorAll('.hide-details-btn');

    // Ketika tombol "View Details" ditekan
    viewDetailsBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const extraDetails = this.closest('.job-card').querySelectorAll('.extra-details'); // Ambil semua extra-details
            const registrationForm = this.closest('.job-card').querySelector('.registration-form');
            const hideDetailsBtn = this.closest('.job-card').querySelector('.hide-details-btn');

            // Menampilkan semua extra-details
            extraDetails.forEach(details => {
                details.style.display = 'grid'; // Menampilkan dalam dua kolom dengan grid
            });
            registrationForm.style.display = 'block'; // Menampilkan form registrasi
            hideDetailsBtn.style.display = 'inline-block'; // Menampilkan tombol "Hide Details"
            this.style.display = 'none'; // Menyembunyikan tombol "View Details"
        });
    });

    // Ketika tombol "Hide Details" ditekan
    hideDetailsBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const extraDetails = this.closest('.job-card').querySelectorAll('.extra-details');
            const registrationForm = this.closest('.job-card').querySelector('.registration-form');
            const viewDetailsBtn = this.closest('.job-card').querySelector('.view-details-btn');

            // Menyembunyikan semua extra-details
            extraDetails.forEach(details => {
                details.style.display = 'none'; // Menyembunyikan extra-details
            });
            registrationForm.style.display = 'none'; // Menyembunyikan form registrasi
            this.style.display = 'none'; // Menyembunyikan tombol "Hide Details"
            viewDetailsBtn.style.display = 'inline-block'; // Menampilkan tombol "View Details"
        });
    });
});
