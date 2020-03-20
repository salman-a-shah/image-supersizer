import os
import dotenv

"""
A convenient script for loading environment variables
"""

path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(path)