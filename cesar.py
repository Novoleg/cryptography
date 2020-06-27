alphabet = 'abcdefghijklmnopqrstuvwxyz'
shift = int(input("Введи сдвиг: "))
message = input('Введи сообщение: ').strip()
security_message = ''
unsecurity_message = ''

for counter in message:
    security_message += alphabet[(alphabet.index(counter) + shift) % len(alphabet)]
print('Result: "' + security_message + '"')

for counter in security_message:
    unsecurity_message += alphabet[(alphabet.index(counter) - shift) % len(alphabet)]
print('Result: "' + unsecurity_message + '"')

print('fdfsfsdfs')
print('Durost')