from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime, timedelta

router = APIRouter(prefix="/admin")

@router.get('/users')
def get_users(db: Session = Depends(get_db)):
    """Get all users and their subscription status"""
    return {
        'users': [
            {
                'id': 'user1',
                'email': 'user@example.com',
                'plan': 'pro',
                'mrr': 49.00,
                'joined': '2024-01-01'
            }
        ]
    }

@router.get('/revenue')
def get_revenue_stats(db: Session = Depends(get_db)):
    """Get revenue statistics"""
    return {
        'mrr': 4900.00,
        'arr': 58800.00,
        'churn_rate': 2.5
    }

@router.get('/activity')
def get_activity_log(db: Session = Depends(get_db)):
    """Get recent activity across all users"""
    return {
        'activities': [
            {
                'user_id': 'user1',
                'action': 'scheduled_post',
                'timestamp': '2024-12-08T10:00:00Z'
            }
        ]
    }