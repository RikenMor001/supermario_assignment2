from PIL import Image, ImageDraw
from datetime import datetime

def generate_demo_image():
    image = Image.new("RGB", (800, 450), "lightblue")
    draw = ImageDraw.Draw(image)

    draw.text((50, 50), "Super Mario Security Simulation", fill="black")
    draw.text((50, 100), "Synthetic test image", fill="black")
    draw.text((50, 150), str(datetime.now()), fill="black")

    image.save("static/demo.png")
    print("Synthetic image generated.")

if __name__ == "__main__":
    generate_demo_image()