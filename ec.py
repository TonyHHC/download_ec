from PIL import Image
import os
import glob

pdf_path = r'D:\Temp\ec.pdf'

files = glob.glob(r'D:\Temp\EC\*.png')
files.sort

images = [
    Image.open(f)
    for f in files
]

images[0].save(
    pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
)