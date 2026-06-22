from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

class Item(BaseModel):
    username: str
    password: str

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/login")
async def login(data: Item):
    print(f"🔔 后台监听到 -> 用户名: {data.username}, 密码: {data.password}")
    if data.username == "admin" and data.password == "123456":
        return {"success": True,"message":"登陆成功"}
    else:
        return {"success":False,"message":"登陆失败，请检查用户名或密码"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)