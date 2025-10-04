import os

# start uvicorn server
os.system("uvicorn main:app --reload --host 0.0.0.0 --port 8000") 