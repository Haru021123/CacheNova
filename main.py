from fastapi import FastAPI, HTTPException, UploadFile, File, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

app = FastAPI()

# Add CORS middleware to allow frontend-backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your frontend's URL for better security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models for API requests and responses
class ItemInput(BaseModel):
    itemId: str
    name: str
    width: float
    depth: float
    height: float
    priority: int = Field(..., ge=1, le=100)
    expiryDate: Optional[str]
    usageLimit: Optional[int]
    preferredZone: str

class ContainerInput(BaseModel):
    containerId: str
    zone: str
    width: float
    depth: float
    height: float

class Coordinates(BaseModel):
    width: float
    depth: float
    height: float

class Position(BaseModel):
    startCoordinates: Coordinates
    endCoordinates: Coordinates

class PlacementResult(BaseModel):
    itemId: str
    containerId: str
    position: Position

@app.post("/api/placement")
async def placement_recommendation(items: List[ItemInput], containers: List[ContainerInput]):
    # Simplified placement logic (mock response for testing)
    placements = []
    
    for item in items:
        # Mock placement result (replace with actual logic)
        placements.append(
            PlacementResult(
                itemId=item.itemId,
                containerId=containers[0].containerId if containers else "unknown",
                position=Position(
                    startCoordinates=Coordinates(width=0, depth=0, height=0),
                    endCoordinates=Coordinates(width=item.width, depth=item.depth, height=item.height),
                ),
            )
        )
    
    return {"success": True, "placements": placements}

@app.get("/api/search")
async def search_item(itemId: Optional[str] = None):
    if not itemId:
        raise HTTPException(status_code=400, detail="Item ID is required")
    
    # Mock response for testing purposes
    return {
        "success": True,
        "found": True,
        "item": {
            "itemId": itemId,
            "name": "Mock Item",
            "containerId": "contA",
            "zone": "Crew Quarters",
            "position": {
                "startCoordinates": {"width": 0, "depth": 0, "height": 0},
                "endCoordinates": {"width": 10, "depth": 10, "height": 20},
            },
        },
        "retrievalSteps": [],
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, ssl_keyfile="key.pem", ssl_certfile="cert.pem")
