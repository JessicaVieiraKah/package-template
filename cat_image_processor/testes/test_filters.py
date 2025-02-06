from cat_processor.filters import apply_grayscale

def test_apply_grayscale(tmp_path):
    input_image = "IMG_20230811_213941_027.jpg"
    output_image = tmp_path / "output.jpg"
    
    result = apply_grayscale(input_image, output_image)
    assert output_image.exists()
    assert result == str(output_image)
