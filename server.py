"""
Flask app for detecting emotions in text using the emotion_detector function.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detection')

@app.route('/emotionDetector')
def emotion_detector_route():
    """
    Flask app for detecting emotions in text using the emotion_detector function.
    """
    text_to_analyze = request.args.get('textToAnalye')
    response = emotion_detector(text_to_analyze)

    if response['anger'] is None:
        return 'Invalid text! Please try again!'

    formatted_response = f"""
        For the given statement, the system response is 
            'anger': {response['anger']}, 
            'disgust': {response['disgust']}, 
            'fear': {response['fear']}, 
            'joy': {response['joy']} and 
            'sadness': {response['sadness']}. 
        The dominant emotion is {response['dominant_emotion']}.
    """

    return formatted_response

@app.route('/')
def render_index_page():
    """
    Render the index HTML page.
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    