import string

# Caesar Cipher

# Implement a Caesar cipher, both encoding and decoding. The key is an integer from 1 to 25. This cipher rotates the letters of the alphabet (A to Z). The encoding replaces each
# letter with the 1st to 25th next letter in the alphabet (wrapping Z to A). So key 2 encrypts “HI” to “JK”, but key 20 encrypts “HI” to “BC”.

def encrypt(message, key):
  alphabet_l = string.ascii_lowercase
  alphabet_u = string.ascii_uppercase

  def encrypt_letter(letter, key):
    if letter in alphabet_l:
      index = alphabet_l.index(letter)
      return alphabet_l[(index + key) % len(alphabet_l)]
    elif letter in alphabet_u:
      index = alphabet_u.index(letter)
      return alphabet_u[(index + key) % len(alphabet_u)]
      
    return letter

  encrypted_message = [encrypt_letter(letter, key) for letter in message]
  return ''.join(encrypted_message)
  
decrypt = lambda message, key: encrypt(message, -key)

selection = input("Do you wish to 'Encrypt' or 'Decrypt' a message? ").lower()
message = input('Enter your message: ')
key = int(input('Enter your key: '))

if selection == 'encrypt':
  print(encrypt(message, key))
elif selection == 'decrypt':
  print(decrypt(message, key))