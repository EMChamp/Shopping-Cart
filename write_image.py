import base64

image_data = base64.b64decode(encoded_data)

with open("output.png", "wb") as f:
    f.write(image_data)