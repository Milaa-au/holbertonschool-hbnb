#!/usr/bin/python3
from app import db
import uuid
from datetime import datetime

class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self):
        """
        Initialize a new BaseModel instance.

        Generates a unique UUID and sets creation and update
        timestamps to the current datetime.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
        Update the last modification timestamp.

        This method should be called whenever the object state
        changes to reflect the latest update time.
        """
        self.updated_at = datetime.now()

    def update(self, data):
        """
        Update model attributes from a dictionary.

        Iterates over the provided key-value pairs and updates
        existing attributes only, then refreshes the update
        timestamp.

        Args:
            data (dict): Dictionary containing attributes to update.
        """
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()
