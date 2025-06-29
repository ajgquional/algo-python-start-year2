# Module/Lesson: M4L2 (The Easy Editor App Part 1)
# Description: Displays an "image editor" UI and implements a display of image files as a list (other image editor functionalities are not yet implemented).
# Original code solution by: Algorithmics
# Annotated by: Adrian Josele G. Quional
# Documentation for PyQt5: https://www.riverbankcomputing.com/static/Docs/PyQt5/

# libraries
import os # to interact with the OS
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QFileDialog,  # dialog for selecting directories or files
    QLabel, QPushButton, QListWidget,
    QHBoxLayout, QVBoxLayout
)

# creating the main application
app = QApplication([])  # every PyQt5 app needs one QApplication instance

# creating the main window
win = QWidget() # a simple window widget
win.resize(700, 500) # set initial size of the window
win.setWindowTitle("Easy Editor") # set the window title

# creating GUI components
lb_image = QLabel("Image") # label to later display the image
btn_dir = QPushButton("Folder") # button to open a folder
lw_files = QListWidget() # list widget to display image filenames

# creating buttons for image operations (functionality not yet implemented)
btn_left = QPushButton("Left")
btn_right = QPushButton("Right")
btn_flip = QPushButton("Mirror")
btn_sharp = QPushButton("Sharpness")
btn_bw = QPushButton("B/W")

# ==============================
# layout setup:

# horizontal layout to contain two columns (left: file list, right: image + buttons)
row = QHBoxLayout()

# vertical layouts for each column
col1 = QVBoxLayout() # left column (folder button and list)
col2 = QVBoxLayout() # right column (image view and operation buttons)

# add widgets to the left column
col1.addWidget(btn_dir) # add the folder selection button
col1.addWidget(lw_files) # add the list of image files

# add the image label to the right column
col2.addWidget(lb_image, 95)

# creating a horizontal layout for the image operation buttons
row_tools = QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)

# adding the button row to the right column
col2.addLayout(row_tools)

# adding the two columns to the main horizontal layout (col1 takes 20%, col2 80%)
row.addLayout(col1, 20)
row.addLayout(col2, 80)

# applying the layout to the main window
win.setLayout(row)

# show the window
win.show()

# ==============================
# image folder handling:

workdir = '' # variable to store the selected folder path

def filter(files, extensions):
    """
    Filters a list of filenames to include only those with specified extensions.

    Args:
        files (list of str): List of filenames to filter.
        extensions (list of str): List of allowed file extensions (e.g., ['.jpg', '.png']).

    Returns:
        list of str: Filtered list containing only filenames with allowed extensions.
    """
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result

def chooseWorkdir():
    """
    Opens a dialog for the user to choose a directory.

    Sets the selected directory as the global variable `workdir`.
    """
    global workdir
    workdir = QFileDialog.getExistingDirectory() # get folder path from user

def showFilenamesList():
    """
    Opens a directory chooser, filters image files in the selected directory,
    and displays them in the file list widget (`lw_files`).
    """
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp'] # supported image formats
    chooseWorkdir() # letting the user choose a folder
    filenames = filter(os.listdir(workdir), extensions) # filtering image files
    lw_files.clear() # clear any previous entries
    for filename in filenames: # add each image file to the list
        lw_files.addItem(filename)

# connecting the folder button to showFilenamesList function
btn_dir.clicked.connect(showFilenamesList)

# run the Qt event loop
app.exec()