
import pickle

import uvicorn
from fastapi import FastAPI


app = FastAPI(title="Flood Probability Prediction API")


with open("model.bin", "rb") as f_in:
    model = pickle.load(f_in)


@app.post("/predict")
def predict_flood_probability(record: list[int]) -> dict[str, float]:
    predicted_proba = model.predict([record])[0]
    return {"flood_probability": predicted_proba}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

