from sympy import randprime

# Генератор 8 - битного открытого ключа
p = 0
q = 0
n = 257
while n > 256:
    p = randprime(2, 250)
    q = randprime(2, 250)
    n = p * q
print("Модуль = ", n)
# Функция Эйлера
e = (p - 1) * (q - 1)
print("Значение функции Эйлера = ", e)
# Открытая экспонента
pub_key = randprime(2, e)
print("Публичный ключ: ", pub_key)
# Private key generation
d = 0

# Генерация закрытого ключа
while d < 1000000000:
    if (pub_key * d) % e == 1:
        break
    d = d + 1
priv_key = d
print("Закрытый ключ: ", priv_key)


def cipher_message(message):
    encrypt_text = []
    for letter in message:
        m = ord(letter)
        cipher_text = (m ** pub_key) % n
        encrypt_text.append(cipher_text)
    print("Зашифрованное сообщение: ", encrypt_text)
    return (encrypt_text)


def decrypt_message(message):
    decrypt_text = ""
    for letter in message:
        c = letter
        decrypt_letter = (c ** priv_key) % n
        ascii_convert = chr(decrypt_letter)
        decrypt_text = decrypt_text + ascii_convert
    print("Дешифрованное сообщениие: ", decrypt_text)
    return (decrypt_text)


# Testing
test = cipher_message(input("Введи сообщение: "))
decrypt_message(test)
