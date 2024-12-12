from PIL import Image
import numpy as np

print("Welcome to Image Encryption Program")

def encrypt_image(image_path, key):
    original_image = Image.open(image_path)
    image_array = np.array(original_image)
    encrypted_image_array = (image_array*key)/(key+1)
    encrypted_image = Image.fromarray(np.uint8(encrypted_image_array))

    encrypted_image_path = "encrypted_image.png"
    encrypted_image.save(encrypted_image_path)
    print("Image encrypted successfully. \n Encrpted Image saved at : {encrypted_image_path}.")


def decrypt_image(encrypted_image_path, key):
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_image_array = np.array(encrypted_image)
    decrypted_image_array = (encrypted_image_array*(key+1))/(key)
    decrypted_image_array = np.clip(decrypted_image_array,0,255)
    decrypted_image = Image.fromarray(np.uint8(decrypted_image_array))

    decrypted_image_path = "decrypted_image.png"
    decrypted_image.save(decrypted_image_path)
    print("Image decrypted successfully. \n Decrypted Image saved at : {decrypted_image_path}.")
def main():
    while True:
        print("Type \n'e' for encryption\n'd' for decryption\n'q' to quit.")
        choice = input("Your Choice ?? ")

        if choice == "e":
            encrypt()
        elif choice == "d":
            decrypt()
        elif choice == "q":
            print("Exiting Program.............")
            break
        else:
            print("Enter Valid choice !!!!")
    
def encrypt():
    key = int(input("Enter Encryption Key : "))
    image_location = input("Enter Location or URL of the Image : ")

    try:
        encrypt_image(image_location,key)
    except FileNotFoundError:
        print("Invalid Location, Image Not Founf. Please restart process.")

def decrypt():
    key = int(input("Enter Decryption Key : "))
    encrypted_image_location = input("Enter Location of the Encrypted Image : ")

    try:
        decrypt_image(encrypted_image_location, key)
    except FileNotFoundError:
        print("Invalid Location, Image Not Founf. Please restart process.")

if __name__ == "__main__":
    main()