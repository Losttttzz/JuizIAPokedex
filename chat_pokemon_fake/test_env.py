from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="key.env")

print("Chave:", os.getenv("GEMINI_API_KEY"))
