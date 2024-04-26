from django.test import TestCase
from pathlib import Path
# Create your tests here.
from dotenv import load_dotenv
import os
load_dotenv(os.path.join(Path(__file__).resolve().parent.parent,'.env'))
print(os.getenv('openai_API_Key'))

