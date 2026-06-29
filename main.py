from fastapi import FastAPI
from pydantic import BaseModel
import pickle


app = FastAPI(title="Email Spam Detection")

model = pickle.load(open("model.pkl","rb"))