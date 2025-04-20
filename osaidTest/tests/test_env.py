import os
from dotenv import load_dotenv

load_dotenv()

def test_valid_env():
    value = "not Testing"
    expected = "TESTING"
    
    assert value == expected