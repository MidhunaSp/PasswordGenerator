import random
import string


def generate_password(length, include_uppercase=True, include_digits=True, include_special_chars=True):
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_digits else ''
    special_chars = string.punctuation if include_special_chars else ''
    
    
    all_chars = lowercase + uppercase + digits + special_chars
    
    
    if not all_chars:
        raise ValueError("No character types selected! Please include at least one type of character.")
    
   
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password


def main():
    print("Welcome to the Password Generator!")
    
    
    while True:
        try:
            length = int(input("Enter the desired password length (e.g., 8, 12, 16): "))
            if length < 1:
                raise ValueError
            break
        except ValueError:
            print("Invalid input! Please enter a positive integer.")
    
    
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    
    
    try:
        password = generate_password(length, include_uppercase, include_digits, include_special_chars)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
