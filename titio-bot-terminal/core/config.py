# title --- Core Config ---
from __future__ import annotations
import os
from typing import Final, Any
from dotenv import load_dotenv

load_dotenv()

class Config:
	"""Loads environment variables and defaults"""
	ENV: Final[str] = os.getenv("ENV", "prod")
	DEBUG: Final[bool] = os.getenv("DEBUG", "0") in ("1", "true", "True")
	API_KEY: Final[str] = os.getenv("API_KEY", "")
	TIMEOUT: Final[int] = int(os.getenv("TIMEOUT", "30"))
	
	@classmethod
	def get(cls, key: str, default: Any = None) -> Any: return getattr(cls, key, default)
	@classmethod
	def is_dev(cls) -> bool: return cls.ENV == "dev"
