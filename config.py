import os

class Config:
    API_ID = int(os.getenv("API_ID", "10471716" ))
    API_HASH = os.getenv("API_HASH", 'f8a1b21a13af154596e2ff5bed164860')
    BOT_TOKEN = os.getenv("BOT_TOKEN", '6999401413:AAHgF1ZpUsCT5MgWX1Wky7GbegyeHvzi2AU')
