from fastapi import FastAPI
from pydantic import BaseModel
from .spam_model import SpamClassifier

app = FastAPI()
model = SpamClassifier()

class EmailText(BaseModel):
    text: str

@app.post("/predict")
def predict_email(data: EmailText):
    result = model.predict(data.text)
    return {"label": result}
