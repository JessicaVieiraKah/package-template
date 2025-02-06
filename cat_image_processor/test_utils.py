from cat_processor.utils import is_cat_image

def test_is_cat_image():
    cat_image = "tests/sample_cat.jpg"  # Imagem de teste com um gato
    non_cat_image = "tests/sample_dog.jpg"  # Imagem de teste sem gatos
    
    assert is_cat_image(cat_image) is True
    assert is_cat_image(non_cat_image) is False
