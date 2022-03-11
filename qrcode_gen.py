import os

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import HorizontalGradiantColorMask, SolidFillColorMask, RadialGradiantColorMask


def generate_qr(reference, data=None):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=6,
        border=1
    )

    qr_data = data if data is not None else reference

    qr.add_data(qr_data)
    qr.make(fit=True)

    img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(),
                        color_mask=RadialGradiantColorMask(center_color=(255, 159, 53), edge_color=(27, 39, 51)))
    img.save(f"{reference}.png")


def delete_qr(reference):
    os.remove(f"{reference}.png")
