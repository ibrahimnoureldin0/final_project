from EmotionDetection.emotion_detection import emotion_detector
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector():
    req = request.args.get("textToAnalyze")
    res = emotion_detector(req)

    if res['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    
    return f"""
            For the given statement, the system response is 'anger': {res['anger']}, 'disgust': {res['disgust']}, 
            'fear': {res['fear']}, 'joy': {res['joy']} and 'sadness': {res['sadness']}. The dominant emotion is {res['dominant_emotion']}.
            """

@app.route('/')
def renderPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
