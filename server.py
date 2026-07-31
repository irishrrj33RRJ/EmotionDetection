# pylint: disable=import-error
""" Flask server for the emotion detection web application. """

from flask import Flask, render_template, request
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def render_index_page():
    """ Render the main page. """
    return render_template('index.html')

@app.route('/emotionDetector')
def sent_detector():
    """ Analyze user text and return formatted emotion results. """
    text_to_analyze=request.args.get('textToAnalyze')

    if not text_to_analyze or not text_to_analyze.strip():
        return 'Invalid text! Please try again. ', 400

    response=emotion_detector(text_to_analyze)

    if response.get('error'):
        return response['error'], 504

    if response.get('dominant_emotion') is None:
        return 'Invalid text! Please try again. ', 400

    return (
        f"For the given statement, the system response is: "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}, "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
