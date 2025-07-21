import cipher_module as cm
import getpass

print("1.Encrypt a message")
print("2. Decrypt a message")
print("3. Exit")
while True:
    choice = input("enter you choice(1 or 3): ")

    if choice == "1":
        key = cm.key()
        cm.save_key(key)
        message = input("Enter Your Message: ")
        encrypted = cm.encrypt(message, key)
        print("Encrypted:", encrypted)

    elif choice == "2":
        input_password = getpass.getpass("Enter Your Decrypt Password: ")
        if cm.check_password(input_password):
            message = input("Enter The Encrypted Message:  ")
            key = cm.load_key()
            decrypted = cm.decrypt(message, key)
            print("Decrypted:", decrypted)
        else:
            print("Incorrect Password! Decryption Denied.")

    elif choice == "3":
        print("GoodBye")
        break
        