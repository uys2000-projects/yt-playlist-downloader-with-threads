from dotenv import load_dotenv
from app.core import main
import os

load_dotenv()

token = os.getenv('APIKEY')
main(token)