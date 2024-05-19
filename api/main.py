from fastapi import FastAPI
from datetime import datetime, timezone
from fastapi.middleware.cors import CORSMiddleware
import pytz
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://server-user-timer.vercel.app"],
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

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)