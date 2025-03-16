import pandas as pd
from .CustomData import CustomData


# Function to make prediction on the new data
def predict_new(data: CustomData, processor, model):
     data = pd.DataFrame([data.dict()])
     processed_data = processor.transform(data)
     prediction = model.predict(processed_data)
     prediction_proba = model.predict_proba(processed_data)
     
     
     return {
          "Churn prediction": bool(prediction[0]),
          "Churn_probability": float(prediction_proba[0][1])
     }


