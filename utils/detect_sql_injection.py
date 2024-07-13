import re
from utils.sql_keywords import sql_injection_patterns

def detect_sql_injection(input_string):
    for pattern in sql_injection_patterns:
        if re.search(pattern, input_string, re.IGNORECASE):
            print(f"Pattern '{pattern}' matched in input '{input_string}'")
            return True
    return False
