// Access the microphone input
function main(){
navigator.mediaDevices.getUserMedia({ audio: true })
    .then(function(stream) {
        const audioContext = new AudioContext();
        const analyser = audioContext.createAnalyser();
        const microphone = audioContext.createMediaStreamSource(stream);

        microphone.connect(analyser);

        // Define the analysis function
        function analyzeMicrophone() {
            const dataArray = new Uint8Array(analyser.fftSize);
            analyser.getByteTimeDomainData(dataArray);
            var
            const max = Math.max(...dataArray);
            const threshold = 140; // Adjust as needed

            const status = document.getElementById('status');
            const mic =document.querySelector('.innercircle');
            const circle=document.querySelector('circle')
            
            if (max > threshold) {
        
            mic.id="innercircle_id2"                         
            status.style.backgroundColor="red"
        
                // Perform your action here
            } else {
                mic.id="innercircle_id1"
                status.style.backgroundColor="yellow"
                status.innerHTML="hello"
                
            }

            requestAnimationFrame(analyzeMicrophone);
        }

        // Start the analysis
        analyzeMicrophone();
    })
    .catch(function(err) {
        console.error('Error accessing microphone:', err);
    });
}
button=document.querySelector('button')
button.addEventListener('click',main())
