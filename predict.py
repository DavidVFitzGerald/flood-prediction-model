
import pickle


with open("model.bin", "rb") as f_in:
    model = pickle.load(f_in) 

record = [7, 5, 8, 4, 8, 4, 8, 4, 3, 7, 3, 5, 7, 4, 7, 2, 3, 6, 7, 2]

predicted_proba = model.predict([record])[0]
print(f"Predicted Flood Probability: {predicted_proba:.3f}")
