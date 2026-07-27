from dotenv import load_dotenv
import os

load_dotenv()

MONDAY_API_KEY = os.getenv("MONDAY_API_KEY")
DEALS_BOARD_ID = os.getenv("DEALS_BOARD_ID")
WORKORDERS_BOARD_ID = os.getenv("WORKORDERS_BOARD_ID")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")