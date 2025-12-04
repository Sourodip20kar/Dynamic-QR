import qrcode
from config import QR_ENDPOINT

img=qrcode.make(QR_ENDPOINT)
img.save("static/universal_calender_qr.png")

print("✅ QR generated and saved at static/universal_calendar_qr.png")
print(f"Scan URL → {QR_ENDPOINT}")