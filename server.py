''' 
This function initiates the application of Emotion Detection 
to be executed over the flask channel and is deployed on localhost:5000
'''


from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():

    ''' this function takes the text input from the HTML interface
        and runs emotion detection over it using the emotion_detector() function
        This will return an output that consists of labels for each emotion along
        with the confidence score for each emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    message = f"""For the given statement, the system response is
                'anger': {response['anger']}, 'disgust': {response['disgust']}, 
                'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}.
                The dominant emotion is {response['dominant_emotion']}."""
    if response['dominant_emotion'] == None:
        return "Invalid input! Please try again"
    else:
        return message

@app.route("/")
def render_index_page():

    '''
        This function renders the main application page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
