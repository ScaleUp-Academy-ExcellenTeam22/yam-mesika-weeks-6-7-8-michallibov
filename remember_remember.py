from PIL import Image


def encrypt_terrorists_message(image_path: str) -> str:
    """
    This function gets a path to an image and encrypts the message that is hidden in it. The hidden message
    should be in a format of black pixels, when each pixel's index represents a letter of the message we want
    to encrypt.
    :param image_path: the path of the image that we received from main
    :return: the encrypted message
    """
    image = Image.open(image_path)
    px = image.load()
    encrypted_message = ''.join([chr(line) for col in range(0, image.size[0]) for line in range(0, image.size[1])
                                if px[col, line] != 255])
    return encrypted_message


if __name__ == '__main__':
    print(encrypt_terrorists_message("C:\\Users\\Michal\\Downloads\\Notebooks-master\\week06\\resources\\code.png"))
