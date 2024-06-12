document.getElementById('start').addEventListener('click', function() {
    fetch('/process/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')
      },
      body: JSON.stringify({})
    })
    .then(response =>
  