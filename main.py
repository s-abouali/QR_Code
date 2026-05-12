import qrcode
from PIL import Image
import os


def create_github_qr(github_username, save_name="github_qr.png"):
    """
    Create a QR code that links to your GitHub profile
    """
    # Create GitHub profile URL
    github_url = f"https://github.com/{github_username}"

    print(f"🔗 Creating QR code for: {github_url}")

    # QR Code configuration
    qr = qrcode.QRCode(
        version=1,  # Size (1-40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # 7% error correction
        box_size=10,  # Size of each box
        border=4,  # White border thickness
    )

    # Add GitHub URL to QR code
    qr.add_data(github_url)
    qr.make(fit=True)

    # Create image with GitHub theme colors
    img = qr.make_image(
        fill_color="black",  # QR code color
        back_color="white"  # Background color
    )

    # Save the QR code
    img.save(save_name)
    print(f"✅ QR Code saved as: {save_name}")
    print(f"📱 Scan to visit: {github_url}")

    # Display image (if possible)
    try:
        img.show()
    except:
        print("📸 Image opened (check your default image viewer)")

    return img, github_url


def create_fancy_github_qr(github_username, save_name="github_qr_fancy.png"):
    """
    Create a fancy QR code with GitHub logo overlay
    """
    github_url = f"https://github.com/{github_username}"

    # Basic QR code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(github_url)
    qr.make(fit=True)

    # Create fancy QR
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Add GitHub logo (simple text overlay for demo)
    fancy_img = Image.new('RGB', (qr_img.size[0], qr_img.size[1] + 100), color='black')
    fancy_img.paste(qr_img, (0, 100))

    # Add text overlay
    from PIL import ImageDraw, ImageFont
    draw = ImageDraw.Draw(fancy_img)

    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except:
        font = ImageFont.load_default()

    # GitHub branding
    draw.text((10, 10), f"Scan to visit:", fill="white", font=font)
    draw.text((10, 45), f"@{github_username}", fill="#1DA1F2", font=font)
    draw.text((10, 75), github_url, fill="white", font=ImageFont.load_default())

    fancy_img.save(save_name)
    print(f"✨ Fancy QR saved as: {save_name}")

    return fancy_img


# 🚀 MAIN PROGRAM
if __name__ == "__main__":
    print("🔗 GitHub QR Code Generator")
    print("=" * 40)

    # CHANGE THIS to your GitHub username!
    YOUR_GITHUB_USERNAME = "yourusername"  # ← EDIT THIS!


    qr_img, url = create_github_qr(YOUR_GITHUB_USERNAME)

