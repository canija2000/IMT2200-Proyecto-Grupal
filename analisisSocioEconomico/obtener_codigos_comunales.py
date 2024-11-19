from PIL import Image
import pytesseract
import pandas as pd

# Load the uploaded image
image_path = "data/codigos_comunales.png"
image = Image.open(image_path)

# Extract text from the image using OCR
extracted_text = pytesseract.image_to_string(image, lang='spa')

# Display the extracted text to understand its structure
extracted_text

# Create dataframe
data_comunas = {"codigo comuna": [], "nombre comuna": []}
for text in extracted_text.split("\n"):
    if text != "":
        codigo, nombre = int(text[0:5]), text[6:]
        data_comunas["codigo comuna"].append(codigo)
        data_comunas["nombre comuna"].append(nombre)

codigos_comunales = pd.DataFrame(data_comunas)
codigos_comunales.to_csv("data/codigos_comunales.csv", index=False)