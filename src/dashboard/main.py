from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from ..backend.database import get_db
from ..backend.security import KeyEncryption

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get('/posts/scheduled')
def get_scheduled_posts(db: Session = Depends(get_db)):
    # Get all scheduled posts for the user
    return [
        {
            'id': 1,
            'content': 'Scheduled post 1',
            'platforms': ['twitter', 'linkedin'],
            'schedule_time': '2024-12-10 15:00:00'
        }
    ]

@app.post('/posts/schedule')
def schedule_post(post_data: dict, db: Session = Depends(get_db)):
    # Schedule a new post
    return {'status': 'scheduled'}