import cv2
import numpy as np
from tensorflow.keras.models import load_model

EMOTION_LABELS = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

class EmotionDetector:
    def __init__(self, model_path='data/models/fer2013_mini_XCEPTION.102-0.66.hdf5'):
        try:
            self.model = load_model(model_path, compile=False)
        except Exception as e:
            raise ValueError(f"Error loading model from {model_path}: {e}")
        
    def preprocess_image(self, face_img):
        try:
            face_img_gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
            resized = cv2.resize(face_img_gray, (64, 64))
            normalized = resized / 255.0
            reshaped = np.reshape(normalized, (1, 64, 64, 1))
            return reshaped
        except Exception as e:
            raise ValueError(f"Error preprocessing image: {e}")
    
    def detect_emotion(self, face_img):
        try:
            preprocessed_img = self.preprocess_image(face_img)
            predictions = self.model.predict(preprocessed_img, verbose=0)
            emotion_label = EMOTION_LABELS[np.argmax(predictions)]
            return emotion_label
        except Exception as e:
            raise ValueError(f"Error detecting emotion: {e}")