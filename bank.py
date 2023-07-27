
def verify_recipient_details(recipient_account, recipient_bank):
   
    if recipient_account and recipient_bank:
        return True
    return False

def check_sufficient_balance(sender_account, transfer_amount):
    
    sender_balance = 10000 
    if sender_balance >= transfer_amount:
        return True
    return False

def check_transaction_limits(transfer_amount, daily_limit):
   
    if transfer_amount <= daily_limit:
        return True
    return False

def perform_transaction_verification():
    print("Performing transaction verification...")
    return True

def transfer_amount(sender_account, recipient_account, recipient_bank, transfer_amount):
    
    if not verify_recipient_details(recipient_account, recipient_bank):
        print("Error: Invalid recipient account or bank details.")
        return

    if not check_sufficient_balance(sender_account, transfer_amount):
        print("Error: Insufficient balance in the sender's account.")
        return

    daily_transaction_limit = 10000  
    if not check_transaction_limits(transfer_amount, daily_transaction_limit):
        print("Error: Transfer amount exceeds the daily transaction limit.")
        return

    if not perform_transaction_verification():
        print("Error: Transaction verification failed.")
        return

    transaction_data = {
        "sender_account": sender_account,
        "recipient_account": recipient_account,
        "recipient_bank": recipient_bank,
        "amount": transfer_amount,
    }

    print("Transfer successful. Amount transferred:", transfer_amount)
    
    
transfer_amount("Sender_Account", "Recipient_Account", "Recipient_BankXYZ",5000)

