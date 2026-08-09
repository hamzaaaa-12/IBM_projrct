# IBM_project
# Emotion Detector
 
A web application that detects the emotions (anger, disgust, fear, joy, sadness) expressed in a piece of text, built using the Watson NLP library and deployed with Flask.
 
This project was built as the final assignment for the AI-based web application development course, covering the full lifecycle from library integration to static code analysis.
 
## Features
 
- Detects five emotions in a given text: **anger, disgust, fear, joy, sadness**
- Identifies the **dominant emotion** (the one with the highest score)
- Simple web UI for entering text and viewing results
- Graceful error handling for blank or invalid input
- Fully unit tested
- Passes static code analysis with a 10/10 `pylint` score
## Project Structure
 
```
emotion_detector/
├── EmotionDetection/
│   ├── __init__.py            # Package entry point
│   └── emotion_detection.py   # Core emotion_detector() function
├── templates/
│   └── index.html             # Web UI page
├── static/
│   └── mywebscript.js         # Client-side logic (calls the Flask endpoint)
├── server.py                  # Flask application
├── test_emotion_detection.py  # Unit tests
└── requirements.txt           # Python dependencies
```
 
## Requirements
 
- Python 3.7+
- Flask
- requests
- pylint (for static analysis, optional at runtime)
Install dependencies with:
 
```bash
pip install -r requirements.txt
```
 
## Running the Application
 
From the project root, start the Flask server:
 
```bash
python server.py
```
 
By default the app runs on `http://0.0.0.0:5000`. Open it in your browser:
 
```
http://localhost:5000
```
 
Type a sentence into the text box and click **Analyze** to see the emotion scores and dominant emotion.
 
## API Endpoint
 
### `GET /emotionDetector`
 
**Query parameter:**
 
| Name | Type | Description |
|------|------|-------------|
| `textToAnalyze` | string | The text to run emotion detection on |
 
**Example request:**
 
```
GET /emotionDetector?textToAnalyze=I am so happy today
```
 
**Example success response (200):**
 
```
For the given statement, the system response is 'anger': 0.0049, 'disgust': 0.0032,
'fear': 0.0057, 'joy': 0.9825 and 'sadness': 0.0128. The dominant emotion is joy.
```
 
**Example error response (400)**, returned when the input text is blank or invalid:
 
```
Invalid text! Please try again!
```
 
## Using the Package Directly
 
You can also call the emotion detection function directly in Python:
 
```python
from EmotionDetection.emotion_detection import emotion_detector
 
result = emotion_detector("I am thrilled about this project!")
print(result)
# {'anger': 0.002, 'disgust': 0.001, 'fear': 0.003, 'joy': 0.97,
#  'sadness': 0.004, 'dominant_emotion': 'joy'}
```
 
If the input text is blank, all values (including `dominant_emotion`) will be `None`.
 
## Running Unit Tests
 
```bash
python -m unittest test_emotion_detection.py
```
 
The test suite covers:
 
- Each of the five possible dominant emotions (anger, disgust, fear, joy, sadness)
- Blank/invalid input handling
## Static Code Analysis
 
This project is linted with `pylint`:
 
```bash
pylint server.py EmotionDetection/emotion_detection.py test_emotion_detection.py
```
 
All files score **10.00/10**.
 
## Error Handling
 
- Blank input is caught both **client-side** (JavaScript, before any request is sent) and **server-side** (Flask route and `emotion_detector` function).
- Network or API failures from the Watson NLP service are also handled gracefully, returning `None` values rather than raising an unhandled exception.
## Notes
 
This project uses IBM Watson NLP's `EmotionPredict` service via the Skills Network lab endpoint (`sn-watson-emotion.labs.skills.network`). This endpoint is only reachable from within the IBM Skills Network Cloud IDE / lab environment, so live emotion detection will only work when run there. Outside that environment, requests to the endpoint will fail at the network level, though the application logic, error handling, and tests remain fully functional and demonstrable.
 
## License
 
This project was created for educational purposes as part of a course assignment.
