

def password():
    password_use = input("Password?")
    password_capital = password_use.upper()
    password_lower = password_use.lower()
    if password_use != password_capital and password_use != password_lower and len(password_use) >= 8:
        print("Ok")
    else:
        print("Password must be at least 8 characters long, contain one uppercase letter, one lowercase letter, and one number.")



password()