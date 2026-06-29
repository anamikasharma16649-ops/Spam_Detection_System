from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

app = FastAPI(title="Email Spam Detection")

model = pickle.load(open("model.pkl", "rb"))

class UserReqt(BaseModel):
    Email: str

# same preprocessing used in training
def preprocess(text):
    text = text.lower()
    text = re.sub("[^a-zA-Z0-9 ]", "", text)
    text = text.split()
    text = [word for word in text if word not in ENGLISH_STOP_WORDS]
    return " ".join(text)

@app.get("/")
def home():
    return {"message": "Email Spam Detection"}

@app.post("/prediction")
def predict(data: UserReqt):
    email = preprocess(data.Email)
    prediction = model.predict([email])
    return {"prediction": int(prediction[0])}