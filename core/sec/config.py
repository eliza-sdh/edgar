"""
Configuration settings for SEC data collection and processing.
"""

from pathlib import Path
import os

class Config:
    # SEC API Configuration
    SEC_EMAIL = "elizaveta.kondrashoav@sdh.eu"
    SEC_ORGANIZATION = "SDH"
    SEC_API_KEY = os.getenv('SEC_API_KEY', '')  # Get from environment variable
    
    # File Paths
    DATA_DIR = Path(__file__).parent.parent.parent / 'data'
    CIK_DB_FILE = DATA_DIR / 'sec_fund_ciks.json'
    SEC_DATA_FILE = DATA_DIR / 'sec_cik_lookup_data.txt'
    
    # API Settings
    SEC_RATE_LIMIT = 10  # requests per second
    SEC_USER_AGENT = "Your Company Name yourname@company.com"
    
    # Matching Settings
    MIN_MATCH_SCORE = 0.7  # Minimum score for a valid match
    MAX_MATCHES = 5  # Maximum number of matches to return

    # OpenAI configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')  # Get from environment variable
    OPENAI_MODEL = "gpt-3.5-turbo"
    OPENAI_MAX_TOKENS = 200
    OPENAI_TEMPERATURE = 0.3

    # Create data directory if it doesn't exist
    DATA_DIR.mkdir(parents=True, exist_ok=True) 