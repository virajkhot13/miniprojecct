// Get input element and list of names
const searchInput = document.getElementById('searchInput');
const nameList = document.getElementById('nameList');
const searchResults = document.getElementById('searchResults');

// Add event listener for keyup event on the input field
searchInput.addEventListener('keyup', function() {
    // Get the search query
    const query = searchInput.value.toLowerCase();

    // Clear previous search results
    searchResults.innerHTML = '';

    // Iterate through the names and check if they match the query
    for (let i = 0; i < nameList.children.length; i++) {
        const name = nameList.children[i].innerText.toLowerCase();

        if (name.includes(query)) {
            // Create a new list item for each matching name
            const resultItem = document.createElement('li');
            resultItem.innerText = nameList.children[i].innerText;
            searchResults.appendChild(resultItem);
        }
    }
});
