from fastapi import FastAPI
from datetime import datetime, timezone
from fastapi.middleware.cors import CORSMiddleware
import pytz

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/api")
async def get_server_time():
    jst = pytz.timezone('Asia/Tokyo')
    server_time = datetime.now(jst)
    server_time = server_time.strftime("%m/%d/%Y, %I:%M:%S %p")
    return {"serverTime": server_time}