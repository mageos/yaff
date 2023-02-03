"""
Abstract class that represents an engine required for managing firewall rules
"""

from abc import ABC, abstractmethod
from yaff.settings import GlobalSettings
from yaff.rules import Rule

class BaseEngine(ABC):
    def __init__(self, settings: GlobalSettings):
        self.settings = settings

    @abstractmethod
    def add_rule(self, rule: Rule) -> None:
        pass