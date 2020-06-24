import operator

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

text_message = str(input('Введи сообщение: '))
key = text_to_bits(str(input('Введи ключ: ')))
binary_message = ''
security_binary_message = ''
decrypted_message = ''



for counter in range(len(text_message)):
    binary_message += text_to_bits(text_message[counter])

for counter in range(len(binary_message)):
    security_binary_message += str(operator.xor(int(binary_message[counter]),int(key[counter])))

for counter in range(len(security_binary_message)):
    decrypted_message +=  str(operator.xor(int(security_binary_message[counter]),int(key[counter])))


print('Двоичное представление сообщения: ',binary_message)
print('Шифрованное двоичное представление сообщения', security_binary_message)
print('Шифрованное текстовое сообщение: ',text_from_bits(security_binary_message))
print('Дешифрованное сообщение', text_from_bits(decrypted_message))


 
