from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]
    return {"result": random.choice(omikuji_list)}
