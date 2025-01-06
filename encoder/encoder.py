__all__ = (
    "EncodingWeaver",
)

from core import pixel_and_msgb_compatibility, ModeEnum
from PIL import Image
from typing import List, Tuple


class EncodingWeaver:

    def __init__(
        self,
        mode_detector: ModeDetector
    ) -> None:

    def encode_message(self, img_name: str, message: str, mode: ModeEnum = ModeEnum.RGB) -> str:
        print("*** ENCODING ***")
        img = Image.open(img_name)
        pixels = list(img.getdata())

        modified_message = f'{len(message)}~' + message
        msg_in_binary = ''.join(format(ord(l), '08b') for l in modified_message)
        message_counter = len(msg_in_binary)
        counter = 0

        custom_img = Image.new(img.mode, img.size)
        custom_pixels: List[Tuple[int]] = []
        for (r, g, b) in pixels:
            if counter < message_counter:
                if not pixel_and_msgb_compatibility(chanel_value=r, msg_binary=int(msg_in_binary[counter])):
                    r = r + 1 if r + 1 <= 255 else r - 1
                counter += 1
                if not pixel_and_msgb_compatibility(chanel_value=g, msg_binary=int(msg_in_binary[counter])):
                    g = g + 1 if g + 1 <= 255 else g - 1
                counter += 1
                if not pixel_and_msgb_compatibility(chanel_value=b, msg_binary=int(msg_in_binary[counter])):
                    b = b + 1 if b + 1 <= 255 else b - 1
                counter += 1
            custom_pixels.append((r, g, b))

        custom_img.putdata(custom_pixels)
        custom_file_name = f'custom_{img_name.split(".")[0]}.png'
        custom_img.save(custom_file_name, format='png')
        return custom_file_name

    def _rgb_mode(self, ):
