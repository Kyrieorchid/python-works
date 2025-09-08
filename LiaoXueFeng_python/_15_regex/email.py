import re

email_addr = re.compile("[a-zA-Z.]+[@][a-zA-Z]+.com")

def is_valid_email(addr):
    if email_addr.match(addr):
        return True
    else:
        return False

# test
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')    
