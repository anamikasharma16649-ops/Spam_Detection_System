from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import pickle
from preprocesing import  preprocess, preprocess_texts

app = FastAPI(title="Email Spam Detection")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)


app.mount("/static", StaticFiles(directory="frontend"), name="static")

class UserReqt(BaseModel):
    Email: str


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