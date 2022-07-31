from resume_website.storage import PrivateMediaStorageOverwrite, PublicMediaStorageOverwrite
from io import BytesIO
from PIL import Image

max_size = 1000


def resize_s3_image(image, storage, crop):
    if image:
        memfile = BytesIO()
        img = Image.open(image)
        if img.height > max_size or img.width > max_size:
            output_size = (max_size, max_size)
            img.thumbnail(output_size, Image.ANTIALIAS)
            img.save(memfile, img.format, quality=95)
            storage.save(image.name, memfile)
            memfile.close()
        if crop and img.height != image.width:
            memfile = BytesIO()
            new_max = max([img.height, img.width])
            new_size = (new_max, new_max)
            new_im = Image.new(mode="RGB", size=new_size,)
            new_im.paste(img, (int((new_max - img.width) / 2), int((new_max - img.height) / 2)))

            new_im.save(memfile, img.format, quality=95)
            storage.save(image.name, memfile)
            new_im.close()
        img.close()


def resize_private_image(image, crop):
    default_storage = PrivateMediaStorageOverwrite()
    resize_s3_image(image, default_storage, crop)


def resize_public_image(image, crop):
    default_storage = PublicMediaStorageOverwrite()
    resize_s3_image(image, default_storage, crop)

