import re

def is_valid_email(email):
    # Simple email validation using a regular expression
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False

def sanitize_input(input_string):
    # Perform input sanitization to prevent XSS
    # You can use libraries like 'html.escape' for more robust sanitization
    return input_string.replace("<", "&lt;").replace(">", "&gt;")
