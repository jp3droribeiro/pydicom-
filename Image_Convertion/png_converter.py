
#pip install numpy pydicom Pillow

import numpy as np  
import pydicom
from PIL import Image
import os


# CONVERTER IMAGENS EM FORMATO DICOM PARA PNG/JPG
file_dicom = "dicom_files\IM-0001-0006.dcm"
file_name = os.path.basename(file_dicom)
converted_image_name = (f"new_images_png/{file_name[:-4]}.png")
image = pydicom.dcmread(file_dicom)

#pegar apenas ass arrays dos pixels
#converter em pixels flutuantes dividindo os pixels por 255

image = image.pixel_array.astype(float)

rescaled_image = (np.maximum(image,0)/image.max())*255 #float pixels

final_image = np.uint8(rescaled_image) # integers pixels

final_image = Image.fromarray(final_image)

final_image.show()

final_image.save(converted_image_name)
