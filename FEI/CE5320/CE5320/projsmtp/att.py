import base64

base64_text = 'VGhpcyBpcyB0aGUgdGVzdCBkb2N1bWVudCBmb3IgY2xpZW50IDIhISEK'

base64_text_bytes = base64_text.encode('utf-8')
with open('decoded_text.txt', 'wb') as file_to_save:
    decoded_text_data = base64.decodebytes(base64_text_bytes)
    file_to_save.write(decoded_text_data)
