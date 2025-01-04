__all__ = (
    "DecodingWeaver",
)

from PIL import Image


class DecodingWeaver:

    def decode_message(img_path: str) -> str:
        print("*** DECODING ***")
        img = Image.open(img_path)
        pixels = list(img.getdata())
        binary_message = ''

        for (r, g, b) in pixels:
            rb = '0' if r % 2 == 0 else '1'
            gb = '0' if g % 2 == 0 else '1'
            bb = '0' if b % 2 == 0 else '1'
            binary_message += rb + gb + bb

        message_length_b = binary_message[:40]
        message_length_ascii = ''.join(
            [chr(int(message_length_b[i:i + 8], 2)) for i in range(0, len(message_length_b), 8)])
        decoded_length = int(message_length_ascii.split('~')[0])
        message_start = int(len(str(decoded_length)) + 1)
        encoded_message = binary_message[message_start * 8:(decoded_length + message_start) * 8]
        message_ascii = ''.join([chr(int(encoded_message[i:i + 8], 2)) for i in range(0, len(encoded_message), 8)])
        return message_ascii
