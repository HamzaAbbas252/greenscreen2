from PIL import Image

# Opening the primary image (used in background)
img1 = Image.open(r"C:\Users\HP\Downloads\depositphotos_13280842-stock-photo-tv-screen-white.jpg")

# Opening the secondary image (overlay image)
img2 = Image.open(r"C:\Users\HP\Downloads\ca722833e2d1f37eb75e130ffb438082.jpg").convert("RGBA")

# Pasting img2 image on top of img1
# starting at coordinates (0, 0)
img1.paste(img2.resize((500,550)) , (0, 0,), mask=img2)

# Displaying the image
img1.show()