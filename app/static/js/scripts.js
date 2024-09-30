document.addEventListener('DOMContentLoaded', function () {
    // Simple example of handling a button click to fetch APT data
    const fetchButton = document.getElementById('fetch-apt-data');

    if (fetchButton) {
        fetchButton.addEventListener('click', function () {
            alert('Fetching latest APT activity...');
            // Here you could include more complex AJAX calls if needed
        });
    }
});

