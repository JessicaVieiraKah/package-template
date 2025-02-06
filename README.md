🐱 Cat Image Processor
Pacote Python para processamento de imagens de gatos, com funcionalidades para aplicar filtros e detectar se uma imagem contém gatos usando o OpenCV.

📖 Índice
Funcionalidades
Instalação
Exemplos de Uso
Filtros de Imagem
Detecção de Gatos
Testes
Como Criar o Pacote
Licença

✨ Funcionalidades
Aplicar filtros a imagens (tons de cinza e desfoque).
Detectar gatos em imagens usando Haar Cascades.

⚙️ Instalação
Clone o repositório e instale as dependências:

bash
Copy
Edit
git clone https://github.com/JessicaVieiraKah/cat-image-processor.git
cd cat_image_processor
pip install -r requirements.txt

🛠️ Exemplos de Uso

🔳 Filtros de Imagem
1. Converter uma imagem para tons de cinza
python
Copy
Edit
from cat_processor.filters import apply_grayscale

input_image = "imagens/gato.jpg"
output_image = "imagens/gato_grayscale.jpg"

apply_grayscale(input_image, output_image)
print(f"Imagem em tons de cinza salva em {output_image}")
2. Aplicar desfoque na imagem
python
Copy
Edit
from cat_processor.filters import blur_image

input_image = "imagens/gato.jpg"
output_image = "imagens/gato_blurred.jpg"

blur_image(input_image, output_image)
print(f"Imagem com desfoque salva em {output_image}")

🧠 Detecção de Gatos
Certifique-se de baixar o Haar Cascade:
👉 Clique aqui para baixar o classificador

Exemplo de uso:

python
Copy
Edit
from cat_processor.utils import is_cat_image

image_path = "imagens/gato.jpg"
cascade_path = "haarcascade_frontalcatface.xml"

if is_cat_image(image_path, cascade_path):
    print("A imagem contém um gato!")
else:
    print("Nenhum gato detectado.")
✅ Testes
Certifique-se de ter o pytest instalado:

bash
Copy
Edit
pip install pytest
Execute os testes com:

bash
Copy
Edit
pytest tests/

📦 Como Criar o Pacote
Gere o pacote executando:

bash
Copy
Edit
python setup.py sdist

Instale localmente com:

bash
Copy
Edit
pip install dist/cat_processor-0.1.0.tar.gz
📝 Licença
Este projeto está licenciado sob a Licença MIT.