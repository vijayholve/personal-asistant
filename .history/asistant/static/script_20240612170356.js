document.getElementById('start').addEventListener('click', function() {
    navigator.mediaDevices.getUserMedia({ audio: true })
      .then(function(stream) {
        const audioContext = new (window.AudioContext || window.webkitAudioContext)();
        const analyser = audioContext.createAnalyser();
        const microphone = audioContext.createMediaStreamSource(stream);
        microphone.connect(analyser);
        analyser.fftSize = 256;
        const dataArray = new Uint8Array(analyser.fftSize);
  
        function analyzeMicrophone() {
          analyser.getByteTimeDomainData(dataArray);
          const max = Math.max(...dataArray);
          const threshold = 140; // Adjust as needed
  
          const mic = document.querySelector('.innercircle');
          const status = document.getElementById('status');
  
          if (max > threshold) {
            mic.classList.add('jelly');
            status.style.color = "red";
            status.innerText = "Speaking";
          } else {
            mic.classList.remove('jelly');
            status.style.color = "white";
            status.innerText = "Silent";
          }
  
          requestAnimationFrame(analyzeMicrophone);
        }
  
        analyzeMicrophone();
      })
      .catch(function(err) {
        console.error('Error accessing microphone:', err);
      });
  });
  