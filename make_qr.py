"""
make_qr.py — makes a QR code for your website, for networking.

Print it on a card or save it to your phone's photos so people can scan it.

How to use:
  1. Install the QR library once:  pip install "qrcode[pil]"
  2. Change SITE_URL below to your real domain
  3. Run:  python make_qr.py
  4. A file called qr-code.png appears in this folder
"""

import qrcode  # the library that draws QR codes

SITE_URL = "https://khadijafranklin.me"  # your website address

# Set up the QR code
qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # still scans if a bit smudged
    box_size=12,   # size of each little square, in pixels
    border=4,      # quiet white margin around it (scanners need this)
)
qr.add_data(SITE_URL)  # put your web address inside the code
qr.make(fit=True)      # pick the smallest grid that fits the address

# Draw it in your brand's deep indigo on white
image = qr.make_image(fill_color="#1F2A44", back_color="white")
image.save("qr-code.png")
print(f"Saved qr-code.png pointing to {SITE_URL}")
