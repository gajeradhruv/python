from PIL import Image
import os

def resize_image(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(image_path)
    print(f"Resized image saved at {image_path}")
    return resized_image

def delete_original_image(image_path):
    
    if os.path.exists(image_path):
        os.remove(image_path)
        print(f"Original image deleted: {image_path}")
        return True
    else:
        print(f"Original image not found: {image_path}")
        return False

def convert_to_grayscale(image_path):
    original_image = Image.open(image_path)
    grayscale_image = original_image.convert("L")
    grayscale_image.save(image_path)
    print(f"Grayscale image saved at {image_path}")
    return grayscale_image

def rotate_image(image_path, degrees):
    original_image = Image.open(image_path)
    rotated_image = original_image.rotate(degrees)
    rotated_image.save(image_path)
    print(f"Rotated image saved at {image_path}")
    return rotated_image