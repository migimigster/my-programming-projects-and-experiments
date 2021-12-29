from caesar_cipher_art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, code_direction):
  end_text = ""
  for char in start_text:
    if char in alphabet:      
      position = alphabet.index(char)
      if code_direction=="encode":
        new_position = position + shift_amount
      elif code_direction=="decode":
        new_position = position - shift_amount
      end_text += alphabet[new_position]
    else:
      end_text+=char
    
  print(f"Here's the {code_direction}d result: {end_text}")

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  #if input is greater than 26, loop to 0
  shift=shift%26
  caesar(start_text=text, shift_amount=shift, code_direction=direction)

  x=input("Do you want to continue? yes or no? ").lower()
  if x=="no":
    should_continue=False
    print("Thank you for using caesar cipher")