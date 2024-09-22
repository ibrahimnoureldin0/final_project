import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    resp = requests.post(url, json = myobj, headers=header)
    
    formated_resp = json.loads(resp.text)


    if resp.status_code == 200:
        anger_score = formated_resp["emotionPredictions"][0]["emotion"]["anger"]
        disgust_score = formated_resp["emotionPredictions"][0]["emotion"]["disgust"]
        fear_score = formated_resp["emotionPredictions"][0]["emotion"]["fear"]
        joy_score = formated_resp["emotionPredictions"][0]["emotion"]["joy"]
        sadness_score = formated_resp["emotionPredictions"][0]["emotion"]["sadness"]

        emotions = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        }
        dominant_emotion = sorted(emotions)[-1]


    elif resp.status_code == 400:
        anger_score = None
        disgust_score = None
        joy_score = None
        sadness_score = None
        fear_score = None


    assessment = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

    return assessment

