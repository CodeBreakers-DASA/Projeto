# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import cv2
import base64

app = FastAPI()

# CORS para permitir acesso do React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # pode restringir para ["http://localhost:5173"]
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carrega imagem
imagem = cv2.imread("Imagem.PNG")

@app.get("/imagem")
def get_imagem():
    # Codifica imagem para base64
    _, buffer = cv2.imencode(".jpg", imagem)
    img_base64 = base64.b64encode(buffer).decode("utf-8")
    return JSONResponse(content={"imagem": img_base64})

from pydantic import BaseModel

class Ponto(BaseModel):
    x: int
    y: int

@app.post("/clique")
def clique(ponto: Ponto):
    print(f"Clique recebido: ({ponto.x}, {ponto.y})")
    # Aqui você pode atualizar a imagem com OpenCV
    return {"status": "ok"}