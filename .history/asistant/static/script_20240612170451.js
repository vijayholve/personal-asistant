document.getElementById('start').addEventListener('click', function() {
    fetch('/process/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')
      },
      body: JSON.stringify({})
    })
    .then(response => response.json())
    .then(data => {
      const status = document.getElementById('status');
      const mic = document.querySelector('.innercircle');
      if (data.status === 'success') {
        mic.classList.add('jelly');
        status.innerText = data.message;
        status.style.color = 'red';
      } else {
        mic.classList.remove('jelly');
        status.innerText = data.message;
        status.style.color = 'white';
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
  });
  
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  