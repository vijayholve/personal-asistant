const sendData = async () => {
    const data = { speech_data: 'Your speech data here' };  // Replace with actual data

    try {
        const csrftoken = getCookie('csrftoken');  // Replace with your function to get the CSRF token

        const response = await fetch('/process/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,  // Include CSRF token in headers
            },
            body: JSON.stringify(data),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok.');
        }

        const jsonResponse = await response.json();
        console.log(jsonResponse);  // Log the response from Django
    } catch (error) {
        console.error('Error:', error);
    }
};

sendData();
