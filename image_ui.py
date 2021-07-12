from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtGui import QImageReader
from PyQt5.QtWidgets import QFileDialog, QWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from matplotlib import pyplot as plt
from numpy import histogram
from numpy.random.mtrand import random 
from opencv_back import *
import sys, os    
import io
from PIL import Image, ImageCms
from custom_filters import *

### Global vars ###
# Image Path

class Ui_MainWindow(object):

    ## INIT ##
    def __init__(self):
        self.IMG_PATH = ""
        self.MAX_BRIGHTNESS = 510
        self.MAX_CONTRAST = 254

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 939)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.import_image_box = QtWidgets.QGroupBox(self.centralwidget)
        self.import_image_box.setGeometry(QtCore.QRect(30, 30, 231, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.import_image_box.setFont(font)
        self.import_image_box.setObjectName("import_image_box")
        self.add_image_button = QtWidgets.QPushButton(self.import_image_box)
        self.add_image_button.setGeometry(QtCore.QRect(20, 31, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_image_button.setFont(font)
        self.add_image_button.setObjectName("add_image_button")
        self.convert_image_box = QtWidgets.QGroupBox(self.centralwidget)
        self.convert_image_box.setGeometry(QtCore.QRect(290, 30, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.convert_image_box.setFont(font)
        self.convert_image_box.setObjectName("convert_image_box")
        self.default_color_radio = QtWidgets.QRadioButton(self.convert_image_box)
        self.default_color_radio.setGeometry(QtCore.QRect(10, 30, 99, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.default_color_radio.setFont(font)
        self.default_color_radio.setObjectName("default_color_radio")
        self.grey_color_radio = QtWidgets.QRadioButton(self.convert_image_box)
        self.grey_color_radio.setGeometry(QtCore.QRect(10, 50, 99, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.grey_color_radio.setFont(font)
        self.grey_color_radio.setObjectName("grey_color_radio")
        self.add_noise_box = QtWidgets.QGroupBox(self.centralwidget)
        self.add_noise_box.setGeometry(QtCore.QRect(550, 30, 281, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_noise_box.setFont(font)
        self.add_noise_box.setObjectName("add_noise_box")
        self.salt_pepper_radio = QtWidgets.QRadioButton(self.add_noise_box)
        self.salt_pepper_radio.setGeometry(QtCore.QRect(10, 30, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.salt_pepper_radio.setFont(font)
        self.salt_pepper_radio.setObjectName("salt_pepper_radio")
        self.gaussian_noise_radio = QtWidgets.QRadioButton(self.add_noise_box)
        self.gaussian_noise_radio.setGeometry(QtCore.QRect(10, 50, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gaussian_noise_radio.setFont(font)
        self.gaussian_noise_radio.setObjectName("gaussian_noise_radio")
        self.poisson_radio = QtWidgets.QRadioButton(self.add_noise_box)
        self.poisson_radio.setGeometry(QtCore.QRect(10, 70, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.poisson_radio.setFont(font)
        self.poisson_radio.setObjectName("poisson_radio")
        self.point_transform_box = QtWidgets.QGroupBox(self.centralwidget)
        self.point_transform_box.setGeometry(QtCore.QRect(30, 140, 331, 191))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.point_transform_box.setFont(font)
        self.point_transform_box.setObjectName("point_transform_box")
        self.brightness_slider = QtWidgets.QSlider(self.point_transform_box)
        self.brightness_slider.setGeometry(QtCore.QRect(200, 30, 111, 20))

        # Setting the Slider max and min values
        self.brightness_slider.setMinimum(0)
        self.brightness_slider.setMaximum(self.MAX_BRIGHTNESS)
        
        font = QtGui.QFont()
        font.setPointSize(10)
        self.brightness_slider.setFont(font)
        self.brightness_slider.setOrientation(QtCore.Qt.Horizontal)
        self.brightness_slider.setObjectName("brightness_slider")
        self.brightness_label = QtWidgets.QLabel(self.point_transform_box)
        self.brightness_label.setGeometry(QtCore.QRect(10, 30, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.brightness_label.setFont(font)
        self.brightness_label.setObjectName("brightness_label")
        self.contrast_slider = QtWidgets.QSlider(self.point_transform_box)
        self.contrast_slider.setGeometry(QtCore.QRect(200, 60, 111, 20))

        # Setting up contrast max and min values
        self.contrast_slider.setMinimum(0)
        self.contrast_slider.setMaximum(self.MAX_CONTRAST)



        # Checking for the sliders 
        self.brightness_slider.valueChanged.connect(self.brightness_contrast)
        self.contrast_slider.valueChanged.connect(self.brightness_contrast)


        font = QtGui.QFont()
        font.setPointSize(10)
        self.contrast_slider.setFont(font)
        self.contrast_slider.setOrientation(QtCore.Qt.Horizontal)
        self.contrast_slider.setObjectName("contrast_slider")
        self.contrast_label = QtWidgets.QLabel(self.point_transform_box)
        self.contrast_label.setGeometry(QtCore.QRect(10, 60, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contrast_label.setFont(font)
        self.contrast_label.setObjectName("contrast_label")
        self.draw_histo_button = QtWidgets.QPushButton(self.point_transform_box)
        self.draw_histo_button.setGeometry(QtCore.QRect(10, 90, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.draw_histo_button.setFont(font)
        self.draw_histo_button.setObjectName("draw_histo_button")
        self.histo_equalization_button = QtWidgets.QPushButton(self.point_transform_box)
        self.histo_equalization_button.setGeometry(QtCore.QRect(10, 140, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.histo_equalization_button.setFont(font)
        self.histo_equalization_button.setObjectName("histo_equalization_button")
        self.local_transform_box = QtWidgets.QGroupBox(self.centralwidget)
        self.local_transform_box.setGeometry(QtCore.QRect(380, 140, 721, 241))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.local_transform_box.setFont(font)
        self.local_transform_box.setObjectName("local_transform_box")
        self.hp_filter_button = QtWidgets.QPushButton(self.local_transform_box)
        self.hp_filter_button.setGeometry(QtCore.QRect(10, 80, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hp_filter_button.setFont(font)
        self.hp_filter_button.setObjectName("hp_filter_button")
        self.median_filter_button = QtWidgets.QPushButton(self.local_transform_box)
        self.median_filter_button.setGeometry(QtCore.QRect(10, 130, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.median_filter_button.setFont(font)
        self.median_filter_button.setObjectName("median_filter_button")
        self.lp_filter_button = QtWidgets.QPushButton(self.local_transform_box)
        self.lp_filter_button.setGeometry(QtCore.QRect(10, 30, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lp_filter_button.setFont(font)
        self.lp_filter_button.setObjectName("lp_filter_button")
        self.avg_filter_button = QtWidgets.QPushButton(self.local_transform_box)
        self.avg_filter_button.setGeometry(QtCore.QRect(10, 180, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.avg_filter_button.setFont(font)
        self.avg_filter_button.setObjectName("avg_filter_button")
        self.edge_filter_box = QtWidgets.QGroupBox(self.local_transform_box)
        self.edge_filter_box.setGeometry(QtCore.QRect(210, 20, 491, 181))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edge_filter_box.setFont(font)
        self.edge_filter_box.setObjectName("edge_filter_box")
        self.lap_filter_radio = QtWidgets.QRadioButton(self.edge_filter_box)
        self.lap_filter_radio.setGeometry(QtCore.QRect(20, 30, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lap_filter_radio.setFont(font)
        self.lap_filter_radio.setObjectName("lap_filter_radio")
        # self.gaussian_filter_radio = QtWidgets.QRadioButton(self.edge_filter_box)
        # self.gaussian_filter_radio.setGeometry(QtCore.QRect(20, 50, 111, 20))
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.gaussian_filter_radio.setFont(font)
        # self.gaussian_filter_radio.setObjectName("gaussian_filter_radio")
        self.vert_sobel_radio = QtWidgets.QRadioButton(self.edge_filter_box)
        self.vert_sobel_radio.setGeometry(QtCore.QRect(20, 70, 99, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vert_sobel_radio.setFont(font)
        self.vert_sobel_radio.setObjectName("vert_sobel_radio")
        self.hor_sobel_radio = QtWidgets.QRadioButton(self.edge_filter_box)
        self.hor_sobel_radio.setGeometry(QtCore.QRect(20, 110, 99, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hor_sobel_radio.setFont(font)
        self.hor_sobel_radio.setObjectName("hor_sobel_radio")
        self.vert_prewitt_radio = QtWidgets.QRadioButton(self.edge_filter_box)
        self.vert_prewitt_radio.setGeometry(QtCore.QRect(20, 90, 99, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vert_prewitt_radio.setFont(font)
        self.vert_prewitt_radio.setObjectName("vert_prewitt_radio")
        self.log_radio = QtWidgets.QRadioButton(self.edge_filter_box)
        self.log_radio.setGeometry(QtCore.QRect(290, 30, 99, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.log_radio.setFont(font)
        self.log_radio.setObjectName("log_radio")
        self.hor_prewitt_radio = QtWidgets.QRadioButton(self.edge_filter_box)
        self.hor_prewitt_radio.setGeometry(QtCore.QRect(20, 130, 99, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hor_prewitt_radio.setFont(font)
        self.hor_prewitt_radio.setObjectName("hor_prewitt_radio")
        self.canny_radio = QtWidgets.QRadioButton(self.edge_filter_box)
        self.canny_radio.setGeometry(QtCore.QRect(290, 50, 99, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.canny_radio.setFont(font)
        self.canny_radio.setObjectName("canny_radio")
        # self.zero_cross_radio = QtWidgets.QRadioButton(self.edge_filter_box)
        # self.zero_cross_radio.setGeometry(QtCore.QRect(290, 70, 99, 20))
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.zero_cross_radio.setFont(font)
        # self.zero_cross_radio.setObjectName("zero_cross_radio")
        self.thicken_radio = QtWidgets.QRadioButton(self.edge_filter_box)
        self.thicken_radio.setGeometry(QtCore.QRect(290, 90, 99, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.thicken_radio.setFont(font)
        self.thicken_radio.setObjectName("thicken_radio")
        self.skeleton_radio = QtWidgets.QRadioButton(self.edge_filter_box)
        self.skeleton_radio.setGeometry(QtCore.QRect(290, 130, 99, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.skeleton_radio.setFont(font)
        self.skeleton_radio.setObjectName("skeleton_radio")
        self.thining_radio = QtWidgets.QRadioButton(self.edge_filter_box)
        self.thining_radio.setGeometry(QtCore.QRect(290, 110, 99, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.thining_radio.setFont(font)
        self.thining_radio.setObjectName("thining_radio")
        self.global_transform_box = QtWidgets.QGroupBox(self.centralwidget)
        self.global_transform_box.setGeometry(QtCore.QRect(30, 360, 201, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.global_transform_box.setFont(font)
        self.global_transform_box.setObjectName("global_transform_box")
        self.hough_line_button = QtWidgets.QPushButton(self.global_transform_box)
        self.hough_line_button.setGeometry(QtCore.QRect(10, 30, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hough_line_button.setFont(font)
        self.hough_line_button.setObjectName("hough_line_button")
        self.hough_circle_button = QtWidgets.QPushButton(self.global_transform_box)
        self.hough_circle_button.setGeometry(QtCore.QRect(10, 80, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hough_circle_button.setFont(font)
        self.hough_circle_button.setObjectName("hough_circle_button")
        self.export_image_button = QtWidgets.QPushButton(self.centralwidget)
        self.export_image_button.setGeometry(QtCore.QRect(910, 860, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.export_image_button.setFont(font)
        self.export_image_button.setObjectName("export_image_button")
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(1010, 860, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exit_button.setFont(font)
        self.exit_button.setObjectName("exit_button")
        self.morpho_box = QtWidgets.QGroupBox(self.centralwidget)
        self.morpho_box.setGeometry(QtCore.QRect(250, 370, 831, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.morpho_box.setFont(font)
        self.morpho_box.setObjectName("morpho_box")
        self.dilation_button = QtWidgets.QPushButton(self.morpho_box)
        self.dilation_button.setGeometry(QtCore.QRect(10, 40, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dilation_button.setFont(font)
        self.dilation_button.setObjectName("dilation_button")
        self.erosion_button = QtWidgets.QPushButton(self.morpho_box)
        self.erosion_button.setGeometry(QtCore.QRect(10, 80, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.erosion_button.setFont(font)
        self.erosion_button.setObjectName("erosion_button")
        self.close_button = QtWidgets.QPushButton(self.morpho_box)
        self.close_button.setGeometry(QtCore.QRect(190, 40, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.close_button.setFont(font)
        self.close_button.setObjectName("close_button")
        self.open_button = QtWidgets.QPushButton(self.morpho_box)
        self.open_button.setGeometry(QtCore.QRect(190, 80, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.open_button.setFont(font)
        self.open_button.setObjectName("open_button")
        self.kernels_box = QtWidgets.QGroupBox(self.morpho_box)
        self.kernels_box.setGeometry(QtCore.QRect(370, 30, 131, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.kernels_box.setFont(font)
        self.kernels_box.setObjectName("kernels_box")
        self.kernel1 = QtWidgets.QRadioButton(self.kernels_box)
        self.kernel1.setGeometry(QtCore.QRect(10, 30, 99, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.kernel1.setFont(font)
        self.kernel1.setObjectName("kernel1")
        self.kernel2 = QtWidgets.QRadioButton(self.kernels_box)
        self.kernel2.setGeometry(QtCore.QRect(10, 50, 99, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.kernel2.setFont(font)
        self.kernel2.setObjectName("kernel2")
        self.imported_box = QtWidgets.QGroupBox(self.centralwidget)
        self.imported_box.setGeometry(QtCore.QRect(30, 560, 331, 271))
        self.imported_box.setObjectName("imported_box")

        ### IMAGES PlaceHolder ###
        self.imported_label = QtWidgets.QLabel(self.imported_box)
        self.imported_label.setGeometry(QtCore.QRect(6, 23, 321, 241))
        self.imported_label.setText("")
        self.imported_label.setPixmap(QtGui.QPixmap(""))
        self.imported_label.setScaledContents(True)
        self.imported_label.setObjectName("imported_label")

        self.noise_box = QtWidgets.QGroupBox(self.centralwidget)
        self.noise_box.setGeometry(QtCore.QRect(390, 560, 341, 271))
        self.noise_box.setObjectName("noise_box")

        self.noise_label = QtWidgets.QLabel(self.noise_box)
        self.noise_label.setGeometry(QtCore.QRect(6, 23, 331, 241))
        self.noise_label.setText("")
        self.noise_label.setScaledContents(True)
        self.noise_label.setObjectName("noise_label")

        self.result_box = QtWidgets.QGroupBox(self.centralwidget)
        self.result_box.setGeometry(QtCore.QRect(760, 560, 341, 271))
        self.result_box.setObjectName("result_box")

        self.result_label = QtWidgets.QLabel(self.result_box)
        self.result_label.setGeometry(QtCore.QRect(6, 23, 331, 241))
        self.result_label.setText("")
        self.result_label.setScaledContents(True)
        self.result_label.setObjectName("result_label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ### Import Button ###
        self.add_image_button.clicked.connect(self.import_image)

        ### Default RGB ###
        self.default_color_radio.clicked.connect(self.display_default)

        ### Grey Scale ###
        self.grey_color_radio.clicked.connect(self.display_grey)

        ### Histogram ###
        self.draw_histo_button.clicked.connect(self.draw_histogram)

        ### Histogram Equalization ###
        self.histo_equalization_button.clicked.connect(self.histogram_equalization)

        ### Filters ###

        ### Low Pass filter ###
        self.lp_filter_button.clicked.connect(self.show_lp)

        ### High Pass filter ###
        self.hp_filter_button.clicked.connect(self.show_hp)
        
        ### Median Filter ###
        self.median_filter_button.clicked.connect(self.show_median)
        
        ### Averaging Filter ###
        self.avg_filter_button.clicked.connect(self.show_avg)

        ### Noise ###
        self.gaussian_noise_radio.clicked.connect(self.add_gaussian)
        self.salt_pepper_radio.clicked.connect(self.add_salt_and_pep)
        self.poisson_radio.clicked.connect(self.add_poisson)
        
        ### Edge Detection ###
        self.canny_radio.clicked.connect(self.do_canny)
        self.log_radio.clicked.connect(self.do_log)
        self.vert_prewitt_radio.clicked.connect(self.do_vert_prewitt)
        self.hor_prewitt_radio.clicked.connect(self.do_hor_prewitt)
        self.vert_sobel_radio.clicked.connect(self.do_vert_sobel)
        self.hor_sobel_radio.clicked.connect(self.do_hor_sobel)
        self.lap_filter_radio.clicked.connect(self.do_laplacian)


        ### Global Tranformation ###
        self.hough_line_button.clicked.connect(self.do_line_hough)
        self.hough_circle_button.clicked.connect(self.do_circle_hough)

        ### Mono shit ###
        self.dilation_button.clicked.connect(self.do_dilation)
        self.erosion_button.clicked.connect(self.do_erosion)
        self.open_button.clicked.connect(self.do_opening)
        self.close_button.clicked.connect(self.do_closing)

        ### Exit Button ###
        self.exit_button.clicked.connect(self.exit_program)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.import_image_box.setTitle(_translate("MainWindow", "Import Image"))
        self.add_image_button.setText(_translate("MainWindow", "add"))
        self.convert_image_box.setTitle(_translate("MainWindow", "Color Conversion"))
        self.default_color_radio.setText(_translate("MainWindow", "Default"))
        self.grey_color_radio.setText(_translate("MainWindow", "Grey"))
        self.add_noise_box.setTitle(_translate("MainWindow", "Add Noise"))
        self.salt_pepper_radio.setText(_translate("MainWindow", "Salt and Pepper"))
        self.gaussian_noise_radio.setText(_translate("MainWindow", "Gaussian noise"))
        self.poisson_radio.setText(_translate("MainWindow", "Poisson noise"))
        self.point_transform_box.setTitle(_translate("MainWindow", "Point Transformation"))
        self.brightness_label.setText(_translate("MainWindow", "Brightness Adjustment"))
        self.contrast_label.setText(_translate("MainWindow", "Contrast Adjustment"))
        self.draw_histo_button.setText(_translate("MainWindow", "Draw Histrogram"))
        self.histo_equalization_button.setText(_translate("MainWindow", "Histogram Equalization"))
        self.local_transform_box.setTitle(_translate("MainWindow", "Local Transformation"))
        self.hp_filter_button.setText(_translate("MainWindow", "HP Filter"))
        self.median_filter_button.setText(_translate("MainWindow", "Median Filter"))
        self.lp_filter_button.setText(_translate("MainWindow", "LP Filter"))
        self.avg_filter_button.setText(_translate("MainWindow", "Averaging Filter"))
        self.edge_filter_box.setTitle(_translate("MainWindow", "Edge Detection Filters"))
        self.lap_filter_radio.setText(_translate("MainWindow", "Laplacian Filter"))

        self.vert_sobel_radio.setText(_translate("MainWindow", "Vert Sobel"))
        self.hor_sobel_radio.setText(_translate("MainWindow", "Hor Sobel"))
        self.vert_prewitt_radio.setText(_translate("MainWindow", "Vert Prewitt"))
        self.log_radio.setText(_translate("MainWindow", "LoG"))
        self.hor_prewitt_radio.setText(_translate("MainWindow", "Hor Prewitt"))
        self.canny_radio.setText(_translate("MainWindow", "Canny"))

        self.thicken_radio.setText(_translate("MainWindow", "Thicken"))
        self.skeleton_radio.setText(_translate("MainWindow", "Skeleton"))
        self.thining_radio.setText(_translate("MainWindow", "Thining"))
        self.global_transform_box.setTitle(_translate("MainWindow", "Global Transformation"))
        self.hough_line_button.setText(_translate("MainWindow", "Hough Line Detection"))
        self.hough_circle_button.setText(_translate("MainWindow", "Hough Circle Detection"))
        self.export_image_button.setText(_translate("MainWindow", "Export"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))
        self.morpho_box.setTitle(_translate("MainWindow", "Morphological "))
        self.dilation_button.setText(_translate("MainWindow", "Dilation"))
        self.erosion_button.setText(_translate("MainWindow", "Erosion"))
        self.close_button.setText(_translate("MainWindow", "Close"))
        self.open_button.setText(_translate("MainWindow", "Open"))
        self.kernels_box.setTitle(_translate("MainWindow", "Kernels"))
        self.kernel1.setText(_translate("MainWindow", "kernel1"))
        self.kernel2.setText(_translate("MainWindow", "kernel2"))
        self.imported_box.setTitle(_translate("MainWindow", "Imported"))
        self.noise_box.setTitle(_translate("MainWindow", "Noise"))
        self.result_box.setTitle(_translate("MainWindow", "Result"))

    def exit_program(self): 
        """Exit when exit button is pressed"""
        sys.exit()

    def display_default(self):
        """Display the defualt imported image"""

        # getting the path 
        if len(self.IMG_PATH) == 0:
            return

        # Converting the image to srgb to avoid errors
        self.convert_to_srgb(self.IMG_PATH)
        self.show_img_in_label(self.imported_label, self.IMG_PATH)

    def get_QImg_grey(self, img):
        """Getting the QImage back if img is grey scale,, idk why this happens"""

        rows, columns = img.shape
        bytesPerLine = columns

        # QImage is the best way to do it 
        QImg = QImage(img.data, columns, rows, bytesPerLine, QImage.Format_Indexed8)

        return QImg

    def get_Qimg_mod_contrast_brightness(self, img):
        """get the QImage back to show the image in the qlabel"""
        
        if img is None:
            return

        height, width, channel = img.shape
        bytesPerLine = 3 * width
        QImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        
        return QImg

    def display_grey(self):
        """Show the grey scale img"""

        if len(self.IMG_PATH) == 0:
            return

        img = conv_grey(self.IMG_PATH)

        QImg = self.get_QImg_grey(img)

        # Showing the img
        self.show_img_in_label(self.result_label, QImg)

    def add_gaussian(self):

        if len(self.IMG_PATH) == 0:
            return

        noise = random_noise(self.IMG_PATH)

        QImg = self.get_Qimg_mod_contrast_brightness(noise)

        # Showing the img
        self.show_img_in_label(self.noise_label, QImg)

    def add_salt_and_pep(self):
        if len(self.IMG_PATH) == 0:
            return

        noise = s_and_p(self.IMG_PATH)

        QImg = self.get_Qimg_mod_contrast_brightness(noise)

        # Showing the img
        self.show_img_in_label(self.noise_label, QImg)

  
    def add_poisson(self):
        if len(self.IMG_PATH) == 0:
            return

        noise = poisson(self.IMG_PATH)

        QImg = self.get_Qimg_mod_contrast_brightness(noise)

        # Showing the img
        self.show_img_in_label(self.noise_label, QImg)

      
 
    def import_image(self):
        """Import an image using: getOpenFileName in QFileDialog and return its path"""

        # get all supported image formats
        supportedFormats = QImageReader.supportedImageFormats()
        text_filter = "Images ({})".format(" ".join(["*.{}".format(fo.data().decode()) for fo in supportedFormats]))

        res = QFileDialog.getOpenFileName(
            # parent could be None, i don't understand what the heck is going on,,, but it works
            parent = None,
            caption = "Select an Image",
            directory = os.getcwd(),
            filter = text_filter
        )

        # Setting the global var
        self.IMG_PATH = res[0]

    def convert_to_srgb(self, file_path):
        '''Convert PIL image to sRGB color space (if possible)'''

        img = Image.open(file_path)
        icc = img.info.get('icc_profile', '')
        if icc:
            io_handle = io.BytesIO(icc)     # virtual file
            src_profile = ImageCms.ImageCmsProfile(io_handle)
            dst_profile = ImageCms.createProfile('sRGB')
            img_conv = ImageCms.profileToProfile(img, src_profile, dst_profile)
            icc_conv = img_conv.info.get('icc_profile','')
            if icc != icc_conv:
                # ICC profile was changed -> save converted file
                img_conv.save(file_path,
                            format = 'JPEG',
                            quality = 50,
                            icc_profile = icc_conv)

    def show_img_in_label(self, label, img_path):
        """Displays the image in the given label"""

        label.setPixmap(QtGui.QPixmap(img_path))


    def valuechange_brightness(self):
        """get the value from the brightness slider"""

        modified_brightness = self.brightness_slider.value()
        
        return modified_brightness

    def valuechange_contrast(self):
        """get the value from the contrast slider"""

        modified_contrast = self.contrast_slider.value()
        
        return modified_contrast

    def brightness_contrast(self):
        """Change brightness and contrast"""

        bright = self.valuechange_brightness()
        con = self.valuechange_contrast()

        img = read_img(self.IMG_PATH)
        effect = controller(img, bright, con)

        # getting the QImage 
        QImg = self.get_Qimg_mod_contrast_brightness(effect)

        # Showing the img
        self.show_img_in_label(self.noise_label, QImg)

    def draw_histogram(self):
        """Draw the histogram and return the img"""

        if not self.IMG_PATH:
            return

        img = read_img(self.IMG_PATH)

        plt.hist(img.ravel(), 256, [0,256])

        plt.show()
    
    def histogram_equalization(self):
        """Draw a simple hitogram equalization chart"""
    
        if not self.IMG_PATH:
            return

        eq = histogram_eq(self.IMG_PATH)

        QImg = self.get_QImg_grey(eq)

        # showing the img

        self.show_img_in_label(self.result_label, QImg)

    def show_lp(self):

        if not self.IMG_PATH:
            return

        lp = lp_filter(self.IMG_PATH)

        QImg = self.get_Qimg_mod_contrast_brightness(lp)

        # showing 
        self.show_img_in_label(self.result_label, QImg)

 
    def show_hp(self):

        if not self.IMG_PATH:
            return

        hp = hp_filter(self.IMG_PATH)

        QImg = self.get_Qimg_mod_contrast_brightness(hp)

        # showing 
        self.show_img_in_label(self.result_label, QImg)


    def show_median(self):

        if not self.IMG_PATH:
            return

        hp = median_filter(self.IMG_PATH)

        QImg = self.get_Qimg_mod_contrast_brightness(hp)

        # showing 
        self.show_img_in_label(self.result_label, QImg)

    def show_avg(self):

        if not self.IMG_PATH:
            return

        avg = avg_filter(self.IMG_PATH)

        QImg = self.get_Qimg_mod_contrast_brightness(avg)

        # showing 
        self.show_img_in_label(self.result_label, QImg)

    def do_canny(self):

        if not self.IMG_PATH:
           return
        
        canny_img = canny(self.IMG_PATH)

        # showing 

        QImg = self.get_QImg_grey(canny_img)

        # showing 
        self.show_img_in_label(self.result_label, QImg)
    
    def do_laplacian(self):
        
        if not self.IMG_PATH:
           return
        
        lap_img = laplacian(self.IMG_PATH)

        # showing 

        QImg = self.get_QImg_grey(lap_img)

        # showing 
        self.show_img_in_label(self.result_label, QImg)    

    def do_log(self):

  
        if not self.IMG_PATH:
           return
        
        log_img = log_filter(self.IMG_PATH)

        # showing 

        QImg = self.get_Qimg_mod_contrast_brightness(log_img)

        # showing 
        self.show_img_in_label(self.result_label, QImg)    
  
    def do_hor_prewitt(self):

        if not self.IMG_PATH:
           return
        
        prw_y_img = prewitt_y(self.IMG_PATH)

        # showing 

        QImg = self.get_QImg_grey(prw_y_img)

        # showing 
        self.show_img_in_label(self.result_label, QImg)    

    def do_vert_prewitt(self):

        if not self.IMG_PATH:
           return
        
        prw_x_img = prewitt_x(self.IMG_PATH)

        # showing 

        QImg = self.get_QImg_grey(prw_x_img)

        # showing 
        self.show_img_in_label(self.result_label, QImg)    

    def do_hor_sobel(self):

        if not self.IMG_PATH:
           return
        
        sobel_y_img = sobel_y(self.IMG_PATH)

        # showing 

        QImg = self.get_QImg_grey(sobel_y_img)

        # showing 
        self.show_img_in_label(self.result_label, QImg)  

    def do_vert_sobel(self):

        if not self.IMG_PATH:
           return
        
        sobel_x_img = sobel_x(self.IMG_PATH)

        # showing 

        QImg = self.get_QImg_grey(sobel_x_img)

        # showing 
        self.show_img_in_label(self.result_label, QImg)    

    def do_line_hough(self):
        
        if not self.IMG_PATH:
           return
        
        line = line_hough(self.IMG_PATH)

        # showing 

        QImg = self.get_Qimg_mod_contrast_brightness(line)

        # showing 
        self.show_img_in_label(self.result_label, QImg)    
    
    def do_circle_hough(self):
        
        if not self.IMG_PATH:
           return
        
        circle = circle_hough(self.IMG_PATH)

        # showing 

        QImg = self.get_Qimg_mod_contrast_brightness(circle)

        # showing 
        self.show_img_in_label(self.result_label, QImg)


    def do_dilation(self):

        if not self.IMG_PATH:
           return
        
        dil = dilation(self.IMG_PATH)

        # showing 

        QImg = self.get_Qimg_mod_contrast_brightness(dil)

        # showing 
        self.show_img_in_label(self.result_label, QImg)

    def do_erosion(self):

        if not self.IMG_PATH:
           return
        
        ero = erosion(self.IMG_PATH)

        # showing 

        QImg = self.get_Qimg_mod_contrast_brightness(ero)

        # showing 
        self.show_img_in_label(self.result_label, QImg)

    def do_opening(self):
        
        if not self.IMG_PATH:
           return
        
        opn = open_(self.IMG_PATH)

        # showing 

        QImg = self.get_QImg_grey(opn)

        # showing 
        self.show_img_in_label(self.result_label, QImg)      

    def do_closing(self):
        
        if not self.IMG_PATH:
           return
        
        cls = close_(self.IMG_PATH)

        # showing 

        QImg = self.get_QImg_grey(cls)

        # showing 
        self.show_img_in_label(self.result_label, QImg)      
      
