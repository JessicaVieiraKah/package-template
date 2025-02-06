import cv2

def is_cat_image(image_path, cascade_path="haarcascade_frontalcatface.xml"):
    """Verifica se a imagem contém um gato usando Haar Cascade."""
    # Baixe o Haar Cascade para gatos: https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalcatface.xml
    cascade = cv2.CascadeClassifier(cascade_path)
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cats = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    return len(cats) > 0  # Retorna True se encontrar gatos
