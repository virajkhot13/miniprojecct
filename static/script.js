document.addEventListener('DOMContentLoaded', function () {
    // Function to search for a student's attendance
    const searchButton = document.getElementById('search-button');
    const searchInput = document.getElementById('search-input');
    const tableBody = document.getElementById('attendance-table-body');

    searchButton.addEventListener('click', function () {
        const searchTerm = searchInput.value;
        fetch(`/search_attendance?name=${searchTerm}`)
            .then(response => response.json())
            .then(data => {
                // Clear the table
                tableBody.innerHTML = '';

                // Populate the table with attendance data
                data.forEach(attendance => {
                    const row = document.createElement('tr');
                    const nameCell = document.createElement('td');
                    nameCell.textContent = attendance.name;
                    const dateCell = document.createElement('td');
                    dateCell.textContent = attendance.date;

                    row.appendChild(nameCell);
                    row.appendChild(dateCell);
                    tableBody.appendChild(row);
                });
            });
    });
});
