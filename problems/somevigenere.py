def encrypt(plaintext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = plaintext.replace(" ", "")
    key_length = len(key)
    key_expanded = (key * ((len(plaintext) // key_length) + 1))[:len(plaintext)]
    encrypted_text = []
    
    for pt_char, key_char in zip(plaintext, key_expanded):
        pt_index = alphabet.index(pt_char)
        key_index = alphabet.index(key_char)
        encrypted_index = (pt_index + key_index) % 26
        encrypted_text.append(alphabet[encrypted_index])
    
    encrypted_result = ''.join(encrypted_text)
    
    if encrypted_result:
        print(encrypted_result)
    else:
        print("NOTHING")

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    plaintext = data[0]
    key = data[1]
    
    encrypt(plaintext, key)
