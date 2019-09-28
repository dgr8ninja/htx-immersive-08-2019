function stopWatch() {
    let time, intervalId;
    let startBtn = document.getElementById("stopwatch.start");
    let stopBtn = document.getElementById("stopwatch.stop");
    let resetBtn = document.getElementById("Stopwatch.reset")

    startBtn.addEventListener("click", function () {
        time = -1;
        incrementTime();
        intervalId = setInterval(incrementTime, 1000);
        startBtn.disabled = true;
        stopBtn.disabled = false;
    });

    stopBtn.addEventListener("click", function () {
        clearInterval(intervalId);
        startBtn.disabled = false;
        stopBtn.disabled = true;
    });

    resetBtn.addEventListener("click", function() {
        h1.textContent = "00:00:00";
        seconds = 0; minutes = 0; hours = 0;

    });

    function incrementTime() {
        time++;
        document.getElementById("time").textContent =
                ("0" + Math.trunc(time / 60)).slice(-2) +
                ":" + ("0" + (time % 60)).slice(-2);
    }
        // resetBtn.addEventListener('click', function () {

                    

        // }
}
