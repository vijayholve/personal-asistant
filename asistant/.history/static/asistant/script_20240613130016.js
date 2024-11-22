document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('start').addEventListener('click', function() {
      captureSpeech();
    });
  
    async function captureSpeech() {
      try {
        const recognition = new webkitSpeechRecognition();
        recognition.continuous = false;
        recognition.lang = 'en-IN';
  
        recognition.onstart = function() {
          document.getElementById('status').innerText = 'Listening...';
          document.getElementById('status').style.color = 'green';
        };
  
        recognition.onresult = async function(event) {
          const text = event.results[0][0].transcript;
          console.log('You said:', text);
          await sendData(text);
        };
  
        recognition.onerror = function(event) {
          console.error('Error occurred in recognition:', event.error);
          document.getElementById('status').innerText = 'Error occurred. Please try again.';
          document.getElementById('status').style.color = 'red';
        };
  
        recognition.onend = function() {
          document.getElementById('status').innerText = 'Silent';
          document.getElementById('status').style.color = 'white';
        };
  
        recognition.start();
      } catch (error) {
        console.error('Error starting speech recognition:', error);
        document.getElementById('status').innerText = 'Error starting recognition.';
        document.getElementById('status').style.color = 'red';
      }
    }
  
    async function sendData(speechData) {
      try {
        const csrftoken = getCookie('csrftoken');
  
        const response = await fetch('/process_audio/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
          },
          body: JSON.stringify({ text: speechData }),
        });
  
        if (!response.ok) {
          throw new Error('Network response was not ok.');
        }
  
        const jsonResponse = await response.json();
        console.log(jsonResponse);
        updateUI(jsonResponse);
      } catch (error) {
        console.error('Error:', error);
      }
    }
  
    function updateUI(data) {
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
    }
  
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
  });
  