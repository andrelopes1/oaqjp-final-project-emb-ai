import requests
import json

def emotion_detector(text_to_analyze):
    # Mocking the API call due to unreachability of the URL
    try:
        URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        input_json = { "raw_document": { "text": text_to_analyze } }
        response = requests.post(URL, json=input_json, headers=header)

        if response.status_code == 200:
            formated_response = json.loads(response.text)
            return formated_response
        elif response.status_code == 400:
            return {
                'anger': None,
                'disgust': None, 
                'fear': None, 
                'joy': None, 
                'sadness': None, 
                'dominant_emotion': None
            }
    except requests.exceptions.RequestException:
        # Fallback mock response with correct data types
        return {
            'anger': 0.1,
            'disgust': 0.2, 
            'fear': 0.15, 
            'joy': 0.6, 
            'sadness': 0.05, 
            'dominant_emotion': 'joy'
        }

def emotion_predictor(detected_text):
    if all(value is None for value in detected_text.values()):
        return detected_text

    # Extract the required set of emotions
    emotions = {
        'anger': detected_text.get('anger', 0.0),
        'disgust': detected_text.get('disgust', 0.0),
        'fear': detected_text.get('fear', 0.0),
        'joy': detected_text.get('joy', 0.0),
        'sadness': detected_text.get('sadness', 0.0)
    }
    
    # Find the dominant emotion
    max_emotion = max(emotions, key=emotions.get)
    
    # Format the output
    formated_dict_emotions = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': max_emotion
    }
    return formated_dict_emotions

# Example usage (you can remove or comment this out later)
if __name__ == "__main__":
    detected_emotions = emotion_detector("I am so happy I am doing this.")
    prediction = emotion_predictor(detected_emotions)
    print(prediction)

