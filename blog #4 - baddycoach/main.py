from fastapi import FastAPI

from playsound import playsound
import random
import time

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Welcome to the Baddy Coach API, your personalized Badminton Coach."}

@app.get("/leftrighttraining")
async def leftrighttraining(run_time: int, time_gap: int):
    run_time = 120 # in seconds
    time_gap = 4 # in seconds
    audio_files = ['audio/left.wav', 'audio/right.wav']

    end_time = time.time() + run_time

    while time.time() < end_time:
        playsound(random.choice(audio_files))
        time.sleep(time_gap)

    return {"message" : "Training complete."}