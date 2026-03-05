from pydantic import BaseModel, Field
from typing import Literal


class UserProfile(BaseModel):
    age: int = Field(..., ge=15, le=60)
    gender: Literal["Male", "Female"]
    height: float = Field(..., ge=100, le=220)
    weight: float = Field(..., ge=30, le=150)
    goal: Literal["Weight gain", "Fat loss", "Maintenance"]
    budget: Literal["Low", "Medium", "High"]
    food_type: Literal["Vegetarian", "Non-veg", "Vegan", "Jain"]
    equipment: Literal["None", "Dumbbells", "Gym"]
    time: int = Field(..., ge=15, le=120)
    stress: Literal["Low", "Medium", "High"]
    sleep: float = Field(..., ge=3, le=10)