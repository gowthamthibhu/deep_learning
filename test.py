from rembg import remove  
from PIL import Image
import io

input_path = r"C:\Users\gowth\OneDrive\Pictures\Saved Pictures\WhatsApp Image 2023-12-09 at 15.46.23_364434a3.jpg"
output_path = r"C:\Users\gowth\Downloads"

input_image = Image.open(input_path)

input_image_bytes = io.BytesIO()
input_image.save(input_image_bytes, format='PNG')
input_image_bytes = input_image_bytes.getvalue()

output_image_bytes = remove(input_image_bytes)

output_image = Image.open(io.BytesIO(output_image_bytes))
output_image.save(output_path)
