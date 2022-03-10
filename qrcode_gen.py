import os

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import HorizontalGradiantColorMask


def generate_qr(reference):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=6,
        border=2
    )
    qr.add_data(reference)
    qr.make(fit=True)

    img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(),
                        color_mask=HorizontalGradiantColorMask(right_color=(209, 103, 0)))
    img.save(f"{reference}.png")


def delete_qr(reference):
    os.remove(f"{reference}.png")
