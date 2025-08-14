import re

class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string
    
    def parse(self):
        # Split the string by commas and spaces to get individual parts
        parts = re.split(r'[,\s]+', self.email_string)
        
        # Filter for valid email addresses
        emails = []
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        for part in parts:
            if re.match(email_pattern, part):
                emails.append(part)
        
        # Return sorted list of unique emails
        return sorted(list(set(emails)))
