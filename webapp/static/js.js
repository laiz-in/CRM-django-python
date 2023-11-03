
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


function searchFunction() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("searchInput");
    filter = input.value.toUpperCase();
    table = document.querySelector(".table-data");
    tr = table.getElementsByTagName("tr");

    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0]; // Adjust index as per the column you want to search

        if (td) {
            txtValue = td.textContent || td.innerText;

            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

function searchNames(input) {
    var names = document.querySelectorAll('tbody tr');

    names.forEach(function(name) {
        var fullName = name.getElementsByTagName('td')[0].innerText.toLowerCase(); // Name
        var id = name.getElementsByTagName('td')[8].innerText.toLowerCase(); // ID

        if (fullName.includes(input.toLowerCase()) || id.includes(input.toLowerCase())) {
            name.style.display = "table-row"; // Show the row if either name or ID matches
        } else {
            name.style.display = "none"; // Hide the row if neither name nor ID matches
        }
    });
}