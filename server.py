import unicodedata
from fastapi import FastAPI
import sentencepiece as spm
from pydantic import BaseModel
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SP = spm.SentencePieceProcessor()
try:
    SP.load("amharic.model")
    print("Loaded amharic.model")
except Exception as e:
    print("Failed to load amharic.model:", e)
    SP = None

def normalize_text(t: str) -> str:
    try:
        return unicodedata.normalize("NFC", t).strip()
    except Exception:
        return t.strip()

class TokenReq(BaseModel):
    text: str
    mode: Optional[str] = "sentencepiece"   # btw here only sentencepiece mode uses model

class TokenResp(BaseModel):
    tokens: List[str]
    ids: Optional[List[int]] = None
    normalized: str

@app.post("/tokenize", response_model=TokenResp)
def tokenize(req: TokenReq):
    txt = normalize_text(req.text)
    mode = req.mode or "sentencepiece"
    if mode == "sentencepiece":
        if SP is None:
            return TokenResp(tokens=[], ids=[], normalized=txt)
        pieces = SP.encode_as_pieces(txt)
        ids = SP.encode_as_ids(txt)
        return TokenResp(tokens=pieces, ids=ids, normalized=txt)

    toks = txt.split()
    return TokenResp(tokens=toks, ids=None, normalized=txt)

@app.get("/")
def root():
    return {"status": "sentencepiece server running"}
