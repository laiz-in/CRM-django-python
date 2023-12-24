
document.addEventListener('DOMContentLoaded', function () {
    const alertElements = document.querySelectorAll('.alert');
    
    alertElements.forEach(function (alert) {
        setTimeout(function () {
            alert.classList.add('visually-hidden');
            setTimeout(function () {
                alert.remove();
            }, 1000); // Change delay if necessary
        }, 3000); // Time in milliseconds - 3 seconds
    });
});



function searchNames(input) {
    var names = document.querySelectorAll('tbody tr');

    names.forEach(function(name) {
        var fullName = name.querySelector('.student-name').innerText.toLowerCase(); // Assuming 'student-name' is the class of the name column
        var id = name.getElementsByTagName('td')[8].innerText.toLowerCase(); // ID

        if (fullName.includes(input.toLowerCase()) || id.includes(input.toLowerCase())) {
            name.style.display = "table-row"; // Show the row if either name or ID matches
        } else {
            name.style.display = "none"; // Hide the row if neither name nor ID matches
        }
    });
}


function searchheads(input) {
    var names = document.querySelectorAll('h5');

    names.forEach(function(name) {
        var fullName = name.querySelector('.heads').innerText.toLowerCase(); // Assuming 'student-name' is the class of the name column

        if (fullName.includes(input.toLowerCase())) {
            name.style.display = "hod-cards"; // Show the row if either name or ID matches
        } else {
            name.style.display = "none"; // Hide the row if neither name nor ID matches
        }
    });
}
function openPopup() {
    document.getElementById('popup').style.display = 'flex';
  }

function closePopup() {
    document.getElementById('popup').style.display = 'none';
  }

  