from PIL import Image, ImageFilter

def apply_grayscale(image_path, output_path):
    """Converte a imagem para tons de cinza."""
    img = Image.open(image_path)
    grayscale_img = img.convert("L")
    grayscale_img.save(output_path)
    return output_path

def blur_image(image_path, output_path):
    """Aplica um filtro de desfoque na imagem."""
    img = Image.open(image_path)
    blurred_img = img.filter(ImageFilter.BLUR)
    blurred_img.save(output_path)
    return output_path
