from app.models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        if not first_name:
            raise ValueError("First name is required")
        if len(first_name) > 50:
            raise ValueError("First name must be 50 characters or less")
        self.first_name = first_name

        if not last_name:
            raise ValueError("Last name is required")
        if len(last_name) > 50:
            raise ValueError("Last name must be 50 characters or less")
        self.last_name = last_name

        if not email:
            raise ValueError("Email is required")
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format")
        self.email = email

        self.is_admin = is_admin
