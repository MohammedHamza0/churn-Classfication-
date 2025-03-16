from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from utils.inferance import predict_new
from utils.config import APP_NAME, SECRET_KEY, VERSION, RandomForest, preprocessor
from utils.CustomData import CustomData

app = FastAPI(title=APP_NAME, version=VERSION)
app.add_middleware(
     CORSMiddleware,
     allow_origins=["*"],
     allow_methods=["*"],     
     allow_headers=["*"]
)

@app.get("/", tags=["General"])
def home():
     return {
          "Message" : f"Welcome to my {APP_NAME} API V{VERSION}"
     }
     

@app.post("/predict/forest", tags=["Models"])
def predict_data(data: CustomData) -> dict:
     try:
          result = predict_new(data=data, processor=preprocessor, model=RandomForest)
          return result
     except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))