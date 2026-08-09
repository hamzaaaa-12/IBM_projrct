/**
 * mywebscript.js
 *
 * Sends the text entered by the user to the /emotionDetector Flask
 * endpoint and displays the formatted response (or an error message)
 * on the page.
 */

function RunSentimentAnalysis() {
    const textToAnalyze = document.getElementById("textToAnalyze").value;
    const responseDiv = document.getElementById("system_response");

    if (!textToAnalyze.trim()) {
        responseDiv.innerText = "Invalid text! Please try again!";
        return;
    }

    const xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState === 4) {
            if (this.status === 200) {
                responseDiv.innerText = this.responseText;
            } else {
                responseDiv.innerText = "Invalid text! Please try again!";
            }
        }
    };

    xhttp.open(
        "GET",
        "/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze),
        true
    );
    xhttp.send();
}
