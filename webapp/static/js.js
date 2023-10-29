
document.addEventListener('DOMContentLoaded', function () {
    const alertElements = document.querySelectorAll('.alert');
    
    alertElements.forEach(function (alert) {
        setTimeout(function () {
            alert.classList.add('visually-hidden');
            setTimeout(function () {
                alert.remove();
            }, 1000); // Change delay if necessary
        }, 1000); // Time in milliseconds - 3 seconds
    });
});
