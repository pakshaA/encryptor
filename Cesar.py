alphabet_ru_up = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alphabet_ru_down = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet_en_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_en_down = "abcdefghijklmnopqrstuvwxyz"
alphabet_ru_count = 33
alphabet_en_count = 26


def do_encryption_things(key, i, lang, do_encrypt=False):
    alphabet_up = alphabet_ru_up if lang == 'rus' else alphabet_en_up
    alphabet_down = alphabet_ru_down if lang == 'rus' else alphabet_en_down
    alph_count = alphabet_ru_count if lang == 'rus' else alphabet_en_count

    curr_alph = alphabet_up if i in alphabet_up else alphabet_down
    place = curr_alph.find(i)

    new_place = place + key if do_encrypt else place - key
    new_place %= alph_count

    result = curr_alph[new_place]
    return result


def encryption(message, key):
    result = ""
    for i in message:
        is_eng = i in alphabet_en_up or i in alphabet_en_down
        is_rus = i in alphabet_ru_up or i in alphabet_ru_down
        if is_eng:
            result += do_encryption_things(key, i, 'eng', True)
        elif is_rus:
            result += do_encryption_things(key, i, 'rus', True)
        else:
            result += i
    return result


def decryption(message, key):
    result = ""
    for i in message:
        is_eng = i in alphabet_en_up or i in alphabet_en_down
        is_rus = i in alphabet_ru_up or i in alphabet_ru_down
        if is_eng:
            result += do_encryption_things(key, i, 'eng')
        elif is_rus:
            result += do_encryption_things(key, i, 'rus')
        else:
            result += i
    return result


def get_caesar(message, key, action):
    return encryption(message, key) if action == 0 else decryption(message, key)