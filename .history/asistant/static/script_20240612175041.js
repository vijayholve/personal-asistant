const sendData = async () => {
    const data = { speech_data: 'Your speech data here' };  // Replace with actual data

    try {
        const csrftoken = getCookie('csrftoken');

        const response = await fetch('/process/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
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

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
