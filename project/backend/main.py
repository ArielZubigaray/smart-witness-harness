# TODO: Implement Smart Witness Backend API
from fastapi import FastAPI, HTTPException, Header, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import json

app = FastAPI(
    title="Smart Witness API",
    description="Backend for IoT alarm verification system",
    version="1.0.0"
)

# CORS for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001", "http://localhost:3002"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok", "service": "smart-witness-api", "version": "1.0.0"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/api/v1/alarm")
async def receive_alarm(
    metadata: str = Form(...),
    photo: UploadFile = File(...),
    x_api_key: str = Header(..., alias="X-API-Key"),
    x_device_id: str = Header(..., alias="X-Device-ID")
):
    """Receive alarm event with photo from device"""
    # TODO: Validate API key, store photo, create event
    return {
        "status": "ok",
        "event_id": "evt_001",
        "photo_id": "photo_001",
        "commands_pending": False,
        "next_capture_in": 30
    }


@app.get("/api/v1/sync")
async def sync_config(
    x_api_key: str = Header(..., alias="X-API-Key"),
    x_device_id: str = Header(..., alias="X-Device-ID"),
    x_config_version: int = Header(0, alias="X-Config-Version")
):
    """Check for config updates"""
    return {"update_available": False, "current_version": x_config_version}


@app.get("/api/v1/commands")
async def get_commands(
    x_api_key: str = Header(..., alias="X-API-Key"),
    x_device_id: str = Header(..., alias="X-Device-ID")
):
    """Get pending commands for device"""
    return {"commands": []}


@app.post("/api/v1/commands/ack")
async def ack_command(
    x_api_key: str = Header(..., alias="X-API-Key"),
    x_device_id: str = Header(..., alias="X-Device-ID")
):
    """Acknowledge command execution"""
    return {"status": "ok"}


@app.get("/api/v1/sites")
async def list_sites():
    """List user's sites"""
    return {
        "sites": [
            {
                "id": "site_001",
                "name": "Casa Buenos Aires",
                "address": "Av. Corrientes 1234",
                "devices_count": 2,
                "wifi_ssid": "FibertelXXX",
                "community_enabled": True
            }
        ]
    }


@app.get("/api/v1/events")
async def list_events():
    """List alarm events"""
    return {"events": [], "total": 0, "page": 1}


@app.get("/api/v1/events/{event_id}")
async def get_event(event_id: str):
    """Get event details with photos"""
    raise HTTPException(status_code=404, detail="Event not found")


@app.get("/api/v1/devices")
async def list_devices():
    """List devices"""
    return {"devices": []}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
