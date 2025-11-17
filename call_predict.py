
import requests


url = "http://localhost:8000/predict"

record = [7, 5, 8, 4, 8, 4, 8, 4, 3, 7, 3, 5, 7, 4, 7, 2, 3, 6, 7, 2]

response = requests.post(url, json=record)
predicted_proba = response.json()
print(f"Predicted Flood Probability: {predicted_proba["flood_probability"]:.3f}")