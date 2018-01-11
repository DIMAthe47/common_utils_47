import io
import numpy as np
from PIL import Image


def pure_pil_alpha_to_color_v2(pilimg, color=(255, 255, 255)):
    """Alpha composite an RGBA Image with a specified color.

    Simpler, faster version than the solutions above.

    Source: http://stackoverflow.com/a/9459208/284318

    Keyword Arguments:
    image -- PIL RGBA Image object
    color -- Tuple r, g, b (default 255, 255, 255)

    """
    pilimg.load()  # needed for split()
    background = Image.new('RGB', pilimg.size, color)
    background.paste(pilimg, mask=pilimg.split()[3])  # 3 is the alpha channel
    return background


def img_matrix_to_gray_img_matrix(img_matrix):
    pilimg_gray = img_matrix_to_pil_image(img_matrix, grayscale=True)
    img_gray_matrix = pilimage_to_matrix(pilimg_gray)
    return img_gray_matrix


def img_matrix_to_pil_image(img_matrix, grayscale=False):
    img_matrix = img_matrix.squeeze()
    img = Image.fromarray(img_matrix)
    if grayscale:
        img = img.convert('L')
    return img


def path_to_pilimage(path_):
    return Image.open(path_)


def pilimage_to_matrix(pilimage):
    img_matrix = np.fromstring(pilimage.tobytes(), dtype=np.uint8)
    img_matrix = img_matrix.reshape((pilimage.size[1], pilimage.size[0], len(pilimage.getbands())))
    return img_matrix


def path_to_matrix(path_):
    return pilimage_to_matrix(path_to_pilimage(path_))


def pilimg_to_jpeg(pilimg):
    b = io.BytesIO()
    pilimg.save(b, format="jpeg")
    b.seek(0)
    return b.read()


def jpeg_to_pilimg(jpeg_):
    return Image.open(io.BytesIO(jpeg_))


def jpeg_to_matrix(jpeg_):
    return pilimage_to_matrix(jpeg_to_pilimg(jpeg_))


def resize_pilimg(pilimg: Image.Image, size):
    return pilimg.resize(size)
