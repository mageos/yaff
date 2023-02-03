"""
Settings: General Settings objects that can be configures
"""
from pydantic import BaseModel
from rules import Action

class GlobalSettings(BaseModel):
    enable_nat: bool
    default_action: Action

