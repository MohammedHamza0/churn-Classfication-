from dotenv import load_dotenv
import os
import joblib


load_dotenv(override=True)

# .env variables
APP_NAME = os.getenv("APP_NAME")
SECRET_KEY = os.getenv("SECRET_KEY")
VERSION = os.getenv("VERSION")


# DIRs
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
models_folder_path = os.path.join(BASE_DIR, "models")


# models
preprocessor = joblib.load(os.path.join(models_folder_path, "processor.pkl"))
RandomForest = joblib.load(os.path.join(models_folder_path, "RandomForest.pkl"))