# Код Морзе для представления цифр и букв использует тире и точки. Напишите функцию для кодирования текстового сообщения в соответствии с кодом Морзе
morse = {
                'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',  " ": "   "
        }

def encode_morse(text: str) -> str:
        global morse
        text = text.upper()
        encode_text = []
        for elem in text:
                if elem in morse:
                        encode_text.append(morse[elem])
        return "   ".join(encode_text)
print(encode_morse('hello python'))


def dencode_morse(text: str) -> str:
        global morse
        text = text.split('   ')
        decod_text = []
        for elem in text:
                for key, val in morse.items():
                        if elem == val:
                                decod_text.append(key)
                                break
        return ''.join(decod_text)

result = encode_morse('hello python')
print(result)
print(dencode_morse(result))
