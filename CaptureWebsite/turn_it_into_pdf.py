import os
from PIL import Image

def images_to_pdf(folder_path, output_pdf_path=None):
    # Get all image files in the folder (common formats)
    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')
    images = [os.path.join(folder_path, f) for f in os.listdir(folder_path)
              if f.lower().endswith(image_extensions)]
    images.sort()  # Optional: sort by filename

    if not images:
        raise ValueError("No images found in the folder.")

    # Open images and convert to RGB
    img_list = []
    for img_path in images:
        img = Image.open(img_path)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img_list.append(img)

    # Set output path if not provided
    if output_pdf_path is None:
        output_pdf_path = os.path.join(folder_path, "output.pdf")

    # Save as PDF
    img_list[0].save(output_pdf_path, save_all=True, append_images=img_list[1:])

    return output_pdf_path