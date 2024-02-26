#DICOM IMAGE VIEWER
#USING THE PYDICOM AND MATPLOT LIBRARIES TO CREATEA A GRAPHIC VIEWER.
import pydicom
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import os


#PATH TO THE FOLDER CONTAINING DICOM FILES (REPLACE WITH YOUR FOLDER PATH)
dcm_folder_path = 'dicom_files'

#LIST TO STORE DICOM OBJECTS (DATASET LIST)
ds_list = []

# LOOP TO LOAD DICOM FILES FROM THE FOLDER
for file in os.listdir(dcm_folder_path):
    dcm_file_path = os.path.join(dcm_folder_path, file)
    if os.path.isfile(dcm_file_path) and file.lower().endswith('.dcm'):
        ds = pydicom.dcmread(dcm_file_path)
        ds_list.append(ds)


#FUNCTION TO UPDATE THE VALUE OF THE GRAPH WHEN CHANGING THE SLIDER VALUE
def update_graph(val):
    index = int(slider.val)
    image = ds_list[index].pixel_array
    img_plot.set_array(image)
    ax.set_title("image DICOM - Index {}".format(index))
    fig.canvas.draw_idle()


# CONFIGURE THE GRAPHICAL INTERFACE FOR DISPLAYING IMAGES
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
first_image = ds_list[0].pixel_array
img_plot = ax.imshow(first_image, cmap='gray')
ax.set_title("DICOM Image - Index 0")


# ADD SLIDER TO NAVIGATE BETWEEN IMAGES
ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider = Slider(ax_slider, 'Index', 0, len(ds_list) - 1, valinit=0, valstep=1)
slider.on_changed(update_graph)

# show graph interface.
plt.show()




