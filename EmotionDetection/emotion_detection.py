import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    obj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=obj, headers=header)
    json_response = json.loads(response.text)

    formatted_response = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

    if response.status_code == 400:
        return formatted_response

    emotions = json_response['emotionPredictions'][0]['emotion']

    formatted_response['anger'] = emotions['anger']
    formatted_response['disgust'] = emotions['disgust']
    formatted_response['fear'] = emotions['fear']
    formatted_response['joy'] = emotions['joy']
    formatted_response['sadness'] = emotions['sadness']
    formatted_response['dominant_emotion'] = {'emotion': None, 'score': 0}
    
    max_score = formatted_response['dominant_emotion']['score']
    dominant_emotion = ormatted_response['dominant_emotion']['emotion']

    for emotion, score in emotions.items():
        if(score > max_score):
            max_score = score
            dominant_emotion = emotion


    return formatted_response 

