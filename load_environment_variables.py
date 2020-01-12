import os
import dotenv

path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(path)