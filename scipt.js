<script>
document.getElementById('url-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevents the default form submission
    
    const url = document.getElementById('url-input').value.trim(); // Get and trim the URL

    // Check if the URL input is empty
    if (!url) {
        document.getElementById('result').innerHTML = 'Please enter a valid URL.';
        return; // Stop further execution if URL is empty
    }

    // Send the POST request to the Flask server
    fetch('/check-phishing', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded', // Send data as URL-encoded
        },
        body: new URLSearchParams({ url: url }) // Send the URL as form data
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Server error: ${response.statusText}`); // Handle non-2xx HTTP responses
        }
        return response.json(); // Parse the JSON response from Flask
    })
    .then(data => {
        if (data.hasOwnProperty('phishing')) {
            // Check if the response contains the 'phishing' field
            document.getElementById('result').innerHTML = `Phishing: ${data.phishing ? 'Yes' : 'No'}`;
        } else {
            document.getElementById('result').innerHTML = 'Invalid response from the server';
        }
    })
    .catch(error => {
        // Handle any errors (e.g., network error, server error)
        console.error('Error:', error);
        document.getElementById('result').innerHTML = 'Error checking URL. Please try again later.';
    });
});
</script>
