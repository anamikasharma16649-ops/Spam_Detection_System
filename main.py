from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import pickle
import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

app = FastAPI(title="Email Spam Detection")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = pickle.load(open("model.pkl", "rb"))


app.mount("/static", StaticFiles(directory="frontend"), name="static")

class UserReqt(BaseModel):
    Email: str

def preprocess(text):
    text = text.lower()
    text = re.sub("[^a-zA-Z0-9 ]", "", text)
    text = text.split()
    text = [word for word in text if word not in ENGLISH_STOP_WORDS]
    return " ".join(text)

@app.get("/")
def home():
    return  FileResponse("frontend/index.html")


@app.post("/prediction")
def predict(data: UserReqt):
    text = preprocess(data.Email)

    print("Original:", data.Email)
    print("Processed:", text)

    prediction = model.predict([text])

    print("Prediction:", prediction)

    return {"prediction": int(prediction[0])}