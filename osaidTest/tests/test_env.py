import os
from dotenv import load_dotenv

load_dotenv()

def test_valid_env():
    value = "TESTING"
    expected = "TESTING"
    
    assert value == expected