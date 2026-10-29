import easyocr
import torch

torch.backends.nnpack.set_flags(False)

# Initialize the reader (downloads the language model on first run)
reader = easyocr.Reader(['en']) 

# Read the text from your nameplate image
result = reader.readtext('Nameplate_image/images2.jpg', detail=0)

# Print the detected text strings
print(result)
