from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="Cloud Backup Service")

backups: Dict[str, str] = {}

class BackupRequest(BaseModel):
    backup_id: str
    data: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/backup")
def create_backup(req: BackupRequest):
    backups[req.backup_id] = req.data
    return {"message": "backup stored", "id": req.backup_id}

@app.get("/backup/{backup_id}")
def get_backup(backup_id: str):
    if backup_id not in backups:
        raise HTTPException(status_code=404, detail="Backup not found")
    return {"id": backup_id, "data": backups[backup_id]}
