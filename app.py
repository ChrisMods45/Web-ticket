from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime

app = FastAPI(title="ChrisAim Tickets")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# DEMO temporal. Luego lo cambiaremos por PostgreSQL/Supabase.
TICKETS = {
    "demo": {
        "id": "0001",
        "status": "Closed",
        "created_at": "September 13, 2026 • 5:42 PM",
        "closed_at": "September 13, 2026 • 5:51 PM",
        "user": {
            "name": "Christian",
            "username": "@christian"
        },
        "messages": [
            {
                "sender": "Christian",
                "role": "user",
                "time": "5:42 PM",
                "text": "Hello, I need help with the script."
            },
            {
                "sender": "ChrisAim Support",
                "role": "support",
                "time": "5:43 PM",
                "text": "Hello 👋 What problem are you having?"
            },
            {
                "sender": "Christian",
                "role": "user",
                "time": "5:44 PM",
                "text": "It isn't loading."
            },
            {
                "sender": "ChrisAim Support",
                "role": "support",
                "time": "5:45 PM",
                "text": "Send me a screenshot please."
            },
            {
                "sender": "Christian",
                "role": "user",
                "time": "5:46 PM",
                "text": "Okay, I will send it now."
            }
        ]
    }
}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "demo_url": "/transcript/demo"
        }
    )

@app.get("/transcript/{token}", response_class=HTMLResponse)
async def transcript(request: Request, token: str):
    ticket = TICKETS.get(token)
    if not ticket:
        raise HTTPException(status_code=404, detail="Transcript not found")

    return templates.TemplateResponse(
        "transcript.html",
        {
            "request": request,
            "ticket": ticket,
            "token": token
        }
    )

@app.get("/health")
async def health():
    return {"status": "ok"}
