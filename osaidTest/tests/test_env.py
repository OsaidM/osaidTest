import os
from dotenv import load_dotenv

load_dotenv()

def test_valid_env():
    value = os.environ.get("DJANGO_ENV")
    expected = "TESTING"
    
    assert value == expected