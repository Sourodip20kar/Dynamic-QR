""" import qrcode
from config import QR_ENDPOINT

# 1. Create a QR Code Object (This lets us customize it)
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H, # 'H' is High error correction (good for printing)
    box_size=5,
    border=3,
)

# 2. Add your data (The link)
qr.add_data(QR_ENDPOINT)
qr.make(fit=True)

# 3. Create the image with CUSTOM COLORS 🎨
# fill_color = The QR code itself (e.g., Red)
# back_color = The background (usually White)
img = qr.make_image(fill_color="#CA1212", back_color="white") 

# Save it
img.save("static/universal_calender_qr_red2.png")

print("✅ Red QR generated and saved at static/universal_calender_qr_red.png")
print(f"Scan URL → {QR_ENDPOINT}") """

import qrcode
import qrcode.image.svg
from config import QR_ENDPOINT

# 1. Setup the QR Code with high error correction (Essential for print!)
qr = qrcode.QRCode(
    version=1,
    # 'H' (High) allows 30% of the code to be damaged/covered and still work.
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=5,
    border=2,
)

# 2. Add the dynamic link
qr.add_data(QR_ENDPOINT)
qr.make(fit=True)

# 3. Generate as RED SVG (Vector) 🎨
# We use the SvgPathImage factory to create a scalable vector.
# We simply pass the hex code for Red (#FF0000) to fill_color.
factory = qrcode.image.svg.SvgPathImage
img = qr.make_image(
    image_factory=factory,
    fill_color="#FF0000",  # Red Color
    back_color="white"     # White Background
)

# 4. Save the file
filename = "static/universal_calendar_final_red.svg"
img.save(filename)

print(f"✅ FINAL RED SVG generated: {filename}")
print(f"🔗 Points to: {QR_ENDPOINT}")
print("🚀 Send this .svg file to your printer!")