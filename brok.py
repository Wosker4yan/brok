#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'davo.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import time
from PyQt4 import QtCore, QtGui
from PyQt4 import QtCore, QtGui
import _mysql
import MySQLdb

import datetime
from PyQt4.QtGui import QIntValidator
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    validator = QIntValidator(1, 1000000000)
    floors_length = 26
    districts = ("Բոլորը", "Ավան", "Դավթաշեն", "Արաբկիր")
    # Note: The consequency should be as in 'districts'
    streets_all = (
        ("Բոլորը","Տիգրան Պետրոսյան"),
        ("Բոլորը","Աիմենակ Արմենակյան"),
        ("Բոլորը","Կոմիտաս"),
    )
    currency = ("Բոլորը","AMD","Euro", "$")

    def create_main_canvas(self) :
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

    def create_main_scroll_area(self) :
        self.ScrollAreaMain = QtGui.QScrollArea(self.centralwidget)
        self.ScrollAreaMain.setWidgetResizable(True)
        self.ScrollAreaMain.setObjectName(_fromUtf8("ScrollAreaMain"))
        self.scrollAreaWidgetContents_9 = QtGui.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 1004, 1213))
        self.scrollAreaWidgetContents_9.setObjectName(_fromUtf8("scrollAreaWidgetContents_9"))
        self.gridLayout_3 = QtGui.QGridLayout(self.scrollAreaWidgetContents_9)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))

    def size_policies(self):
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_base_tab.sizePolicy().hasHeightForWidth())
        self.search_base_tab.setSizePolicy(sizePolicy)

    def search_tab(self):
        self.search_base_tab.setObjectName(_fromUtf8("search_to_data_base_tab"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))

    def organize_stuff(self): #stuff that I don't want to touch
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.seacrh_scroll_area = QtGui.QScrollArea(self.tab)
        self.seacrh_scroll_area.setWidgetResizable(True)
        self.seacrh_scroll_area.setObjectName(_fromUtf8("seacrh_scroll_area"))
        self.scrollAreaWidgetContents_8 = QtGui.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 962, 1142))
        self.scrollAreaWidgetContents_8.setObjectName(_fromUtf8("scrollAreaWidgetContents_8"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents_8)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tableView = QtGui.QTableView(self.scrollAreaWidgetContents_8)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.gridLayout_2.addWidget(self.tableView, 0, 1, 1, 1)
        self.seacrh_form_layout = QtGui.QFormLayout()
        self.seacrh_form_layout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.seacrh_form_layout.setObjectName(_fromUtf8("seacrh_form_layout"))
        self.code = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.code.setObjectName(_fromUtf8("code"))
        self.seacrh_form_layout.setWidget(1, QtGui.QFormLayout.LabelRole, self.code)
        self.code_lineedit_search = QtGui.QLineEdit(self.scrollAreaWidgetContents_8)
        self.code_lineedit_search.setObjectName(_fromUtf8("code_lineedit_search"))
        self.code_lineedit_search.setValidator(self.validator)
        self.seacrh_form_layout.setWidget(1, QtGui.QFormLayout.FieldRole, self.code_lineedit_search)
        self.type = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.type.setObjectName(_fromUtf8("type"))
        self.seacrh_form_layout.setWidget(2, QtGui.QFormLayout.LabelRole, self.type)
        self.type_form_layout = QtGui.QVBoxLayout()

    def search_pane(self): #search pane
        self.type_form_layout.setObjectName(_fromUtf8("type_form_layout"))
        self.checkbox_house = QtGui.QCheckBox(self.scrollAreaWidgetContents_8)
        self.checkbox_house.setObjectName(_fromUtf8("checkbox_house"))
        self.type_form_layout.addWidget(self.checkbox_house)
        self.checkbox_appartment = QtGui.QCheckBox(self.scrollAreaWidgetContents_8)
        self.checkbox_appartment.setObjectName(_fromUtf8("checkbox_appartment"))
        self.type_form_layout.addWidget(self.checkbox_appartment)
        self.checkbox_land = QtGui.QCheckBox(self.scrollAreaWidgetContents_8)
        self.checkbox_land.setObjectName(_fromUtf8("checkbox_land"))
        self.type_form_layout.addWidget(self.checkbox_land)
        self.checkbox_other = QtGui.QCheckBox(self.scrollAreaWidgetContents_8)
        self.checkbox_other.setObjectName(_fromUtf8("checkbox_other"))
        self.type_form_layout.addWidget(self.checkbox_other)
        self.seacrh_form_layout.setLayout(2, QtGui.QFormLayout.FieldRole, self.type_form_layout)
        self.provide = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.provide.setObjectName(_fromUtf8("provide"))
        self.seacrh_form_layout.setWidget(3, QtGui.QFormLayout.LabelRole, self.provide)
        self.vertical_layout_provide = QtGui.QVBoxLayout()
        self.vertical_layout_provide.setObjectName(_fromUtf8("vertical_layout_provide"))
        self.checkbox_rent = QtGui.QCheckBox(self.scrollAreaWidgetContents_8)
        self.checkbox_rent.setObjectName(_fromUtf8("checkbox_rent"))
        self.vertical_layout_provide.addWidget(self.checkbox_rent)
        self.checkbox_sell = QtGui.QCheckBox(self.scrollAreaWidgetContents_8)
        self.checkbox_sell.setObjectName(_fromUtf8("checkbox_sell"))
        self.vertical_layout_provide.addWidget(self.checkbox_sell)
        self.seacrh_form_layout.setLayout(3, QtGui.QFormLayout.FieldRole, self.vertical_layout_provide)
        self.district = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.district.setObjectName(_fromUtf8("district"))
        self.seacrh_form_layout.setWidget(4, QtGui.QFormLayout.LabelRole, self.district)
        self.district_dropdown_select = QtGui.QComboBox(self.scrollAreaWidgetContents_8)
        self.district_dropdown_select.setObjectName(_fromUtf8("district_dropdown_select"))
        self.district_dropdown_select.addItem(_fromUtf8(""))
        self.district_dropdown_select.addItem(_fromUtf8(""))
        self.district_dropdown_select.addItem(_fromUtf8(""))
        self.district_dropdown_select.addItem(_fromUtf8(""))
        self.seacrh_form_layout.setWidget(4, QtGui.QFormLayout.FieldRole, self.district_dropdown_select)
        self.street = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.street.setObjectName(_fromUtf8("street"))
        self.seacrh_form_layout.setWidget(5, QtGui.QFormLayout.LabelRole, self.street)
        self.dropdown_search_street = QtGui.QComboBox(self.scrollAreaWidgetContents_8)
        self.seacrh_form_layout.setWidget(5, QtGui.QFormLayout.FieldRole, self.dropdown_search_street)
        self.home = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.home.setObjectName(_fromUtf8("home"))
        self.seacrh_form_layout.setWidget(6, QtGui.QFormLayout.LabelRole, self.home)
        self.format_home_flat_search = QtGui.QLineEdit(self.scrollAreaWidgetContents_8)
        self.format_home_flat_search.setObjectName(_fromUtf8("format_home_flat_search"))
        self.format_home_flat_search.setInputMask("000/000")
        self.seacrh_form_layout.setWidget(6, QtGui.QFormLayout.FieldRole, self.format_home_flat_search)
        self.room = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.room.setObjectName(_fromUtf8("room"))
        self.seacrh_form_layout.setWidget(7, QtGui.QFormLayout.LabelRole, self.room)
        self.rooms_dropdown_search = QtGui.QComboBox(self.scrollAreaWidgetContents_8)
        self.rooms_dropdown_search.setObjectName(_fromUtf8("rooms_dropdown_search"))
        for i in range(1,11):
            self.rooms_dropdown_search.addItem(str(i))
        self.seacrh_form_layout.setWidget(7, QtGui.QFormLayout.FieldRole, self.rooms_dropdown_search)
        self.floors_count = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.floors_count.setObjectName(_fromUtf8("floors_count"))
        self.seacrh_form_layout.setWidget(8, QtGui.QFormLayout.LabelRole, self.floors_count)
        self.floors_count_search = QtGui.QComboBox(self.scrollAreaWidgetContents_8)
        self.floors_count_search.setObjectName(_fromUtf8("floors_count_search"))
        for i in range(1,25):
            self.floors_count_search.addItem(str(i))
        self.seacrh_form_layout.setWidget(8, QtGui.QFormLayout.FieldRole, self.floors_count_search)
        self.floor = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.floor.setObjectName(_fromUtf8("floor"))
        self.seacrh_form_layout.setWidget(9, QtGui.QFormLayout.LabelRole, self.floor)
        self.search_the_floor_dropdown = QtGui.QComboBox(self.scrollAreaWidgetContents_8)
        self.search_the_floor_dropdown.setObjectName(_fromUtf8("search_the_floor_dropdown"))
        for i in range(1,25):
            self.search_the_floor_dropdown.addItem(str(i))
        self.seacrh_form_layout.setWidget(9, QtGui.QFormLayout.FieldRole, self.search_the_floor_dropdown)
        self.square = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.square.setObjectName(_fromUtf8("square"))
        self.seacrh_form_layout.setWidget(10, QtGui.QFormLayout.LabelRole, self.square)
        self.horizontal_square_ranges_search = QtGui.QHBoxLayout()
        self.horizontal_square_ranges_search.setObjectName(_fromUtf8("horizontal_square_ranges_search"))
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontal_square_ranges_search.addWidget(self.label_2)
        self.search_square_from = QtGui.QLineEdit(self.scrollAreaWidgetContents_8)
        self.search_square_from.setObjectName(_fromUtf8("search_square_from"))
        self.search_square_from.setValidator(self.validator)
        self.horizontal_square_ranges_search.addWidget(self.search_square_from)
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontal_square_ranges_search.addWidget(self.label)
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontal_square_ranges_search.addWidget(self.label_3)
        self.search_square_to = QtGui.QLineEdit(self.scrollAreaWidgetContents_8)
        self.search_square_to.setObjectName(_fromUtf8("search_square_to"))
        self.search_square_to.setValidator(self.validator)
        self.horizontal_square_ranges_search.addWidget(self.search_square_to)
        self.seacrh_form_layout.setLayout(10, QtGui.QFormLayout.FieldRole, self.horizontal_square_ranges_search)
        self.price = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.price.setObjectName(_fromUtf8("price"))
        self.seacrh_form_layout.setWidget(11, QtGui.QFormLayout.LabelRole, self.price)
        self.horizontal_layout_search_prices = QtGui.QHBoxLayout()
        self.horizontal_layout_search_prices.setObjectName(_fromUtf8("horizontal_layout_search_prices"))
        self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontal_layout_search_prices.addWidget(self.label_4)
        self.price_from = QtGui.QLineEdit(self.scrollAreaWidgetContents_8)
        self.price_from.setObjectName(_fromUtf8("price_from"))
        self.price_from.setValidator(self.validator)
        self.horizontal_layout_search_prices.addWidget(self.price_from)
        self.label_5 = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontal_layout_search_prices.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontal_layout_search_prices.addWidget(self.label_6)
        self.price_to = QtGui.QLineEdit(self.scrollAreaWidgetContents_8)
        self.price_to.setObjectName(_fromUtf8("price_to"))
        self.price_to.setValidator(self.validator)
#       self.dropdown_search_currency = QtGui.QComboBox()
#       self.dropdown_search_currency.setObjectName(_fromUtf8("dropdown_search_currency"))
#       self.dropdown_search_currency.setItemText(0, _translate("MainWindow", "Բոլորը", None))
#       self.set_currency_search()
#       self.currency_layout_search = QtGui.QHBoxLayout()
#       self.currency_layout_search.addWidget(self.price_to)
#       self.currency_layout_search.addWidget(self.dropdown_search_currency)
#       self.formLayout_add.setLayout(11, QtGui.QFormLayout.FieldRole, self.currency_layout_search)
        self.horizontal_layout_search_prices.addWidget(self.price_to)
        self.seacrh_form_layout.setLayout(11, QtGui.QFormLayout.FieldRole, self.horizontal_layout_search_prices)
        self.gorcakal = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.gorcakal.setObjectName(_fromUtf8("gorcakal"))
        self.seacrh_form_layout.setWidget(12, QtGui.QFormLayout.LabelRole, self.gorcakal)
        self.user_name_of_worker_search = QtGui.QLineEdit(self.scrollAreaWidgetContents_8)
        self.user_name_of_worker_search.setObjectName(_fromUtf8("user_name_of_worker_search"))
        self.seacrh_form_layout.setWidget(12, QtGui.QFormLayout.FieldRole, self.user_name_of_worker_search)
        self.search_horizontal_layout_for_buttons = QtGui.QHBoxLayout()
        self.search_horizontal_layout_for_buttons.setObjectName(_fromUtf8("search_horizontal_layout_for_buttons"))
        self.button_clear = QtGui.QPushButton(self.scrollAreaWidgetContents_8)
        self.button_clear.setObjectName(_fromUtf8("button_clear"))
        self.search_horizontal_layout_for_buttons.addWidget(self.button_clear)
        self.button_find = QtGui.QPushButton(self.scrollAreaWidgetContents_8)
        self.button_find.setObjectName(_fromUtf8("button_find"))
        self.search_horizontal_layout_for_buttons.addWidget(self.button_find)
        self.seacrh_form_layout.setLayout(13, QtGui.QFormLayout.FieldRole, self.search_horizontal_layout_for_buttons)
        self.date = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.date.setObjectName(_fromUtf8("date"))
        self.seacrh_form_layout.setWidget(0, QtGui.QFormLayout.LabelRole, self.date)
        self.horizontal_layout_date = QtGui.QHBoxLayout()
        self.horizontal_layout_date.setObjectName(_fromUtf8("horizontal_layout_date"))
        self.label_13 = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontal_layout_date.addWidget(self.label_13)
        self.date_from = QtGui.QDateEdit(self.scrollAreaWidgetContents_8)
        self.date_from.setObjectName(_fromUtf8("date_from"))
        self.date_from.setDateTime(QtCore.QDateTime.currentDateTime())
        self.date_from.setDisplayFormat("yyyy-MM-dd")
        self.horizontal_layout_date.addWidget(self.date_from)
        self.label_14 = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontal_layout_date.addWidget(self.label_14)
        self.date_to = QtGui.QDateEdit(self.scrollAreaWidgetContents_8)
        self.date_to.setObjectName(_fromUtf8("date_to"))
        self.date_to.setDateTime(QtCore.QDateTime.currentDateTime())
        self.date_to.setDisplayFormat("yyyy-MM-dd")
        self.horizontal_layout_date.addWidget(self.date_to)
        self.seacrh_form_layout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontal_layout_date)
        self.find = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.find.setText(_fromUtf8(""))
        self.find.setObjectName(_fromUtf8("find"))
        self.seacrh_form_layout.setWidget(13, QtGui.QFormLayout.LabelRole, self.find)
        self.gridLayout_2.addLayout(self.seacrh_form_layout, 0, 0, 1, 1)
        self.seacrh_scroll_area.setWidget(self.scrollAreaWidgetContents_8)
        self.horizontalLayout_2.addWidget(self.seacrh_scroll_area)
        self.search_base_tab.addTab(self.tab, _fromUtf8(""))

    def add_pane(self):#add panel part
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.scroll_area_add = QtGui.QScrollArea(self.tab_2)
        self.scroll_area_add.setWidgetResizable(True)
        self.scroll_area_add.setObjectName(_fromUtf8("scroll_area_add"))
        self.scrollAreaWidgetContents_7 = QtGui.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 962, 1142))
        self.scrollAreaWidgetContents_7.setObjectName(_fromUtf8("scrollAreaWidgetContents_7"))
        self.gridLayout_5 = QtGui.QGridLayout(self.scrollAreaWidgetContents_7)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.formLayout_add = QtGui.QFormLayout()
        self.formLayout_add.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_add.setObjectName(_fromUtf8("formLayout_add"))
        self.type_add = QtGui.QLabel(self.scrollAreaWidgetContents_7)
        self.type_add.setObjectName(_fromUtf8("type_add"))
        self.type_add.setFixedWidth(250)
        self.formLayout_add.setWidget(0, QtGui.QFormLayout.LabelRole, self.type_add)
        self.vertical_layout_type = QtGui.QVBoxLayout()
        self.vertical_layout_type.setObjectName(_fromUtf8("vertical_layout_type"))
        self.radio_button_house = QtGui.QRadioButton(self.scrollAreaWidgetContents_7)
        self.radio_button_house.setObjectName(_fromUtf8("radio_button_house"))
        self.vertical_layout_type.addWidget(self.radio_button_house)
        self.radioButton_appartament = QtGui.QRadioButton(self.scrollAreaWidgetContents_7)
        self.radioButton_appartament.setObjectName(_fromUtf8("radioButton_appartament"))
        self.vertical_layout_type.addWidget(self.radioButton_appartament)
        self.radio_button_land = QtGui.QRadioButton(self.scrollAreaWidgetContents_7)
        self.radio_button_land.setObjectName(_fromUtf8("radio_button_land"))
        self.vertical_layout_type.addWidget(self.radio_button_land)
        self.radioButton_other = QtGui.QRadioButton(self.scrollAreaWidgetContents_7)
        self.radioButton_other.setObjectName(_fromUtf8("radioButton_other"))
        self.vertical_layout_type.addWidget(self.radioButton_other)
        self.formLayout_add.setLayout(0, QtGui.QFormLayout.FieldRole, self.vertical_layout_type)
        self.provide_add = QtGui.QLabel(self.scrollAreaWidgetContents_7)
        self.provide_add.setObjectName(_fromUtf8("provide_add"))
        self.formLayout_add.setWidget(1, QtGui.QFormLayout.LabelRole, self.provide_add)
        self.verticalLayout_provide = QtGui.QVBoxLayout()
        self.verticalLayout_provide.setObjectName(_fromUtf8("verticalLayout_provide"))
        self.checkBox_rent = QtGui.QCheckBox(self.scrollAreaWidgetContents_7)
        self.checkBox_rent.setObjectName(_fromUtf8("checkBox_rent"))
        self.verticalLayout_provide.addWidget(self.checkBox_rent)
        self.checkBox_sell = QtGui.QCheckBox(self.scrollAreaWidgetContents_7)
        self.checkBox_sell.setObjectName(_fromUtf8("checkBox_sell"))
        self.verticalLayout_provide.addWidget(self.checkBox_sell)
        self.formLayout_add.setLayout(1, QtGui.QFormLayout.FieldRole, self.verticalLayout_provide)
        self.district_add = QtGui.QLabel(self.scrollAreaWidgetContents_7)
        self.district_add.setObjectName(_fromUtf8("district_add"))
        self.formLayout_add.setWidget(2, QtGui.QFormLayout.LabelRole, self.district_add)
        self.dropdown_add_district = QtGui.QComboBox(self.scrollAreaWidgetContents_7)
        self.dropdown_add_district.setObjectName(_fromUtf8("dropdown_add_district"))
        self.dropdown_add_district.setFixedWidth(100)
        self.dropdown_add_district.addItem(_fromUtf8(""))
        self.dropdown_add_district.addItem(_fromUtf8(""))
        self.dropdown_add_district.addItem(_fromUtf8(""))
        self.dropdown_add_district.addItem(_fromUtf8(""))
        self.formLayout_add.setWidget(2, QtGui.QFormLayout.FieldRole, self.dropdown_add_district)
        self.street_add = QtGui.QLabel(self.scrollAreaWidgetContents_7)
        self.street_add.setObjectName(_fromUtf8("street_add"))
        self.formLayout_add.setWidget(3, QtGui.QFormLayout.LabelRole, self.street_add)
        self.dropdown_add_street = QtGui.QComboBox(self.scrollAreaWidgetContents_7)
        self.formLayout_add.setWidget(3, QtGui.QFormLayout.FieldRole, self.dropdown_add_street)
        self.home_add = QtGui.QLabel(self.scrollAreaWidgetContents_7)
        self.home_add.setObjectName(_fromUtf8("home_add"))
        self.formLayout_add.setWidget(4, QtGui.QFormLayout.LabelRole, self.home_add)
        self.add_format_of_property = QtGui.QLineEdit(self.scrollAreaWidgetContents_7)
        self.add_format_of_property.setObjectName(_fromUtf8("add_format_of_property"))
        self.add_format_of_property.setInputMask("000/000")
        self.formLayout_add.setWidget(4, QtGui.QFormLayout.FieldRole, self.add_format_of_property)
        self.rooms_add = QtGui.QLabel(self.scrollAreaWidgetContents_7)
        self.rooms_add.setObjectName(_fromUtf8("rooms_add"))
        self.formLayout_add.setWidget(5, QtGui.QFormLayout.LabelRole, self.rooms_add)
        self.dropdown_add_rooms = QtGui.QComboBox(self.scrollAreaWidgetContents_7)
        self.dropdown_add_rooms.setObjectName(_fromUtf8("dropdown_add_rooms"))
        for i in range(1,11):
            self.dropdown_add_rooms.addItem(str(i))
        self.formLayout_add.setWidget(5, QtGui.QFormLayout.FieldRole, self.dropdown_add_rooms)
        self.floors_count_2 = QtGui.QLabel(self.scrollAreaWidgetContents_7)
        self.floors_count_2.setObjectName(_fromUtf8("floors_count_2"))
        self.formLayout_add.setWidget(6, QtGui.QFormLayout.LabelRole, self.floors_count_2)
        self.dropdown_add_floors_count = QtGui.QComboBox(self.scrollAreaWidgetContents_7)
        self.dropdown_add_floors_count.setObjectName(_fromUtf8("dropdown_add_floors_count"))
        for i in range(1,25):
            self.dropdown_add_floors_count.addItem(_fromUtf8(str(i)))
        self.formLayout_add.setWidget(6, QtGui.QFormLayout.FieldRole, self.dropdown_add_floors_count)
        self.floors = QtGui.QLabel(self.scrollAreaWidgetContents_7)
        self.floors.setObjectName(_fromUtf8("floors"))
        self.formLayout_add.setWidget(7, QtGui.QFormLayout.LabelRole, self.floors)
        self.dropdown_add_thefloor = QtGui.QComboBox(self.scrollAreaWidgetContents_7)
        self.dropdown_add_thefloor.setObjectName(_fromUtf8("dropdown_add_thefloor"))
        for i in range(1,25):
             self.dropdown_add_thefloor.addItem(str(i))
        self.formLayout_add.setWidget(7, QtGui.QFormLayout.FieldRole, self.dropdown_add_thefloor)
        self.square_add = QtGui.QLabel(self.scrollAreaWidgetContents_7)
        self.square_add.setObjectName(_fromUtf8("square_add"))
        self.formLayout_add.setWidget(8, QtGui.QFormLayout.LabelRole, self.square_add)
        self.lineEdit_add_square = QtGui.QLineEdit(self.scrollAreaWidgetContents_7)
        self.lineEdit_add_square.setObjectName(_fromUtf8("lineEdit_add_square"))
        self.lineEdit_add_square.setValidator(self.validator)
        self.formLayout_add.setWidget(8, QtGui.QFormLayout.FieldRole, self.lineEdit_add_square)
        self.lineEdit_add_square.setValidator(QIntValidator())
        self.price_add = QtGui.QLabel(self.scrollAreaWidgetContents_7)
        self.price_add.setObjectName(_fromUtf8("price_add"))
        #stex mi tex avelacnem
        self.formLayout_add.setWidget(11, QtGui.QFormLayout.LabelRole, self.price_add)
        self.lineEdit_add_price = QtGui.QLineEdit()
        self.lineEdit_add_price.setObjectName(_fromUtf8("lineEdit_add_price"))
        self.lineEdit_add_price.setValidator(self.validator)
        self.label_gorcakal = QtGui.QLabel(self.scrollAreaWidgetContents_7)
        self.label_gorcakal.setObjectName(_fromUtf8("label_gorcakal"))
        self.formLayout_add.setWidget(12, QtGui.QFormLayout.LabelRole, self.label_gorcakal)
        self.user_name_worker_add = QtGui.QLineEdit(self.scrollAreaWidgetContents_7)
        self.user_name_worker_add.setText(_fromUtf8(""))
        self.user_name_worker_add.setObjectName(_fromUtf8("user_name_worker_add"))
        self.formLayout_add.setWidget(12, QtGui.QFormLayout.FieldRole, self.user_name_worker_add)
        self.find_add = QtGui.QLabel(self.scrollAreaWidgetContents_7)
        self.find_add.setText(_fromUtf8(""))
        self.find_add.setObjectName(_fromUtf8("find_add"))
        self.formLayout_add.setWidget(13, QtGui.QFormLayout.LabelRole, self.find_add)
        self.horizontal_buttons_add = QtGui.QHBoxLayout()
        self.horizontal_buttons_add.setObjectName(_fromUtf8("horizontal_buttons_add"))
        self.clear_button_adding = QtGui.QPushButton(self.scrollAreaWidgetContents_7)
        self.clear_button_adding.setObjectName(_fromUtf8("clear_button_adding"))
        self.horizontal_buttons_add.addWidget(self.clear_button_adding)
        self.add_button = QtGui.QPushButton(self.scrollAreaWidgetContents_7)
        self.add_button.setObjectName(_fromUtf8("add_button"))
        self.horizontal_buttons_add.addWidget(self.add_button)
        self.formLayout_add.setLayout(13, QtGui.QFormLayout.FieldRole, self.horizontal_buttons_add)
        self.comment = QtGui.QLabel(self.scrollAreaWidgetContents_7)
        self.comment.setObjectName(_fromUtf8("comment"))
        self.formLayout_add.setWidget(9, QtGui.QFormLayout.LabelRole, self.comment)
        self.textEdit_comment = QtGui.QTextEdit(self.scrollAreaWidgetContents_7)
        self.textEdit_comment.setObjectName(_fromUtf8("textEdit_comment"))
        self.formLayout_add.setWidget(9, QtGui.QFormLayout.FieldRole, self.textEdit_comment)
        self.phonenumber_add = QtGui.QLabel(self.scrollAreaWidgetContents_7)
        self.phonenumber_add.setObjectName(_fromUtf8("phonenumber_add"))
        self.formLayout_add.setWidget(10, QtGui.QFormLayout.LabelRole, self.phonenumber_add)
        self.lineEdit_add_number = QtGui.QLineEdit(self.scrollAreaWidgetContents_7)
        self.lineEdit_add_number.setText(_fromUtf8(""))
        self.lineEdit_add_number.setObjectName(_fromUtf8("lineEdit_add_number"))
        self.formLayout_add.setWidget(10, QtGui.QFormLayout.FieldRole, self.lineEdit_add_number)
        self.dropdown_add_currency = QtGui.QComboBox()
        self.dropdown_add_currency.setObjectName(_fromUtf8("dropdown_add_currency"))
        self.dropdown_add_currency.setItemText(0, _translate("MainWindow", "Բոլորը", None))
        self.set_currency()
        self.currency_layout = QtGui.QHBoxLayout()
        self.currency_layout.addWidget(self.lineEdit_add_price)
        self.currency_layout.addWidget(self.dropdown_add_currency)
        self.formLayout_add.setLayout(11, QtGui.QFormLayout.FieldRole, self.currency_layout)
        self.Label = QtGui.QLabel(self.scrollAreaWidgetContents_7)
        self.Label.setObjectName(_fromUtf8("Label"))
        self.gridLayout_5.addLayout(self.formLayout_add, 0, 0, 1, 1)
        self.scroll_area_add.setWidget(self.scrollAreaWidgetContents_7)
        self.gridLayout_4.addWidget(self.scroll_area_add, 0, 0, 1, 1)
        self.search_base_tab.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.search_base_tab, 0, 0, 1, 1)
        self.ScrollAreaMain.setWidget(self.scrollAreaWidgetContents_9)
        self.gridLayout.addWidget(self.ScrollAreaMain, 0, 0, 1, 1)


    def fixed_sizes(self):
        self.lineEdit_add_number.setFixedWidth(300)
        self.textEdit_comment.setFixedWidth(300)
        self.dropdown_add_district.setFixedWidth(300)
        self.dropdown_add_street.setFixedWidth(300)
        self.dropdown_add_floors_count.setFixedWidth(300)
        self.dropdown_add_rooms.setFixedWidth(300)
        self.dropdown_add_thefloor.setFixedWidth(300)
        self.add_format_of_property.setFixedWidth(300)
        self.lineEdit_add_square.setFixedWidth(300)
        self.lineEdit_add_price.setFixedWidth(300)
        self.user_name_worker_add.setFixedWidth(300)
        self.add_button.setFixedWidth(300)
        self.clear_button_adding.setFixedWidth(300)
        self.dropdown_add_currency.setFixedWidth(150)

    def search_pane_fixed_size(self):
        self.code_lineedit_search.setFixedWidth(400)
        self.district_dropdown_select.setFixedWidth(400)
        self.dropdown_search_street.setFixedWidth(400)
        self.format_home_flat_search.setFixedWidth(400)
        self.rooms_dropdown_search.setFixedWidth(400)
        self.floors_count_search.setFixedWidth(400)
        self.search_the_floor_dropdown.setFixedWidth(400)
        self.user_name_of_worker_search.setFixedWidth(400)
        self.button_clear.setFixedWidth(200)
        self.button_find.setFixedWidth(200)
        self.tableView.setFixedWidth(1200)
        self.price_to.setFixedWidth(100)
        self.price_from.setFixedWidth(100)
        self.search_square_to.setFixedWidth(100)
        self.search_square_from.setFixedWidth(100)
        self.label_13.setFixedWidth(65)
        self.label_14.setFixedWidth(100)
        self.label_3.setFixedWidth(100)
        self.label_6.setFixedWidth(100)




    def status_bar(self):
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

    def clear_add_input(self):
        self.textEdit_comment.clear()
        self.lineEdit_add_square.clear()
        self.lineEdit_add_number.clear()
        self.lineEdit_add_price.clear()
        self.user_name_worker_add.clear()

    def clear_search_input(self):
         self.search_square_to.clear()
         self.search_square_from.clear()
         self.price_to.clear()
         self.price_from.clear()
         self.user_name_of_worker_search.clear()
         self.format_home_flat_search.clear()
         self.code_lineedit_search.clear()

    def alert_error(self, m) :
        msg = QtGui.QMessageBox(MainWindow)
        msg.setIcon(QtGui.QMessageBox.Critical)
        msg.setText(_fromUtf8(m))
        msg.setWindowTitle(_fromUtf8("Սխալ"))
        msg.setDetailedText(_fromUtf8("Մանրամասն"))
        msg.setBaseSize(300,300)
        msg.exec_()
        raise Exception("Պարրտադիր դաշտերը լրացված չէն")

    def alert_info(self, m) :
        msg = QtGui.QMessageBox(MainWindow)
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.setText(_fromUtf8(m))
        msg.setWindowTitle(_fromUtf8("Սխալ"))
        msg.setDetailedText(_fromUtf8("Մանրամասն"))
        msg.setEscapeButton()
        msg.quit()
        msg.exec_() 
    
    def check_values(self) :
        if self.lineEdit_add_price.text().isEmpty() and self:
            self.alert_error("Պարտադիր կետերը լրացված չէն")

    # getting values from check boxes.
    def check_boxes_values(self): 
        if self.checkBox_rent.isChecked() and self.checkBox_sell.isChecked():
            return 3
        elif self.checkBox_rent.isChecked():
            return 1
        elif self.checkBox_sell.isChecked():
            return 2
        else:
            self.check_values()

      # getting values from radio buttons.
    def radio_button_get_values(self):
        if self.radio_button_house.isChecked():
            return 1
        if self.radioButton_appartament.isChecked():
            return  2
        if self.radio_button_land.isChecked():
            return 3
        if self.radioButton_other.isChecked():
            return 4

    #adding to mysqls database into the broker_database and Brok table.
    def add_to_mysql(self) :
        print self.check_boxes_values()
        self.check_values()
        con = _mysql.connect('localhost', 'root', '1991', 'broker_database')
        columns  = "(house_format,comments,phone_number,price,name_worker,type,purpose,district,street,room,floors_how_many,the_floor,square_meter,currency,date)"
        q = "INSERT INTO Brok " \
            + columns \
            + " VALUES" \
            + "(' " + _fromUtf8(self.add_format_of_property.text()) \
            + "', '" + _fromUtf8(self.textEdit_comment.toPlainText()) \
            + "', '" + _fromUtf8(self.lineEdit_add_number.text()) \
            + "', '" + _fromUtf8(self.lineEdit_add_price.text()) \
            + "', '" + _fromUtf8(self.user_name_worker_add.text()) \
            + "', '" + str(self.radio_button_get_values()) \
            + "', '" + str(self.check_boxes_values()) \
            + "', '" + str(self.dropdown_add_district.currentIndex()) \
            + "', '" + str(self.dropdown_add_street.currentIndex()) \
            + "', '" + str(self.dropdown_add_rooms.currentIndex()) \
            + "', '" + str(self.dropdown_add_floors_count.currentIndex()) \
            + "', '" + str(self.dropdown_add_thefloor.currentIndex()) \
            + "', '" + str(self.lineEdit_add_square.text()) \
            + "', '" + str(self.dropdown_add_currency.currentText())\
            + "', '"  + str(time.strftime("%y/%m/%d"))\
            + "');"

        print q
        con.query(str(q))
        result = con.use_result()
        if result == None :
                print ""
                return
        data_list_int = result.fetch_row()
        column_int = result.num_fields()
        row_int = result.num_rows()
        print column_int
        print row_int
        print data_list_int


    def select_from_myslq(self):
        self.check_values()
        con = _mysql.connect('localhost', 'root', '1991', 'broker_database')
        columns = "(house_format,comments,phone_number,price,name_worker,type,purpose,district,street,room,floors_how_many,the_floor,square_meter,currency)"
        q = "SELECT" + \
            + "*"\
            + " FROM Brok"\
            + "Where house_format = " + self.format_home_flat_search.text()\


        print q
        con.query(str(q))
        result = con.use_result()
        if result == None:
            print ""
            return
        data_list_int = result.fetch_row()
        column_int = result.num_fields()
        row_int = result.num_rows()
        print column_int
        print row_int
        print data_list_int





    # setting up the main window.
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(850, 800)
        MainWindow.setWindowState(QtCore.Qt.WindowMaximized)
        self.create_main_canvas()
        self.create_main_scroll_area()
        self.search_base_tab = QtGui.QTabWidget(self.scrollAreaWidgetContents_9)
        self.size_policies()
        self.search_tab()
        self.organize_stuff()
        self.search_pane()
        self.add_pane()
        self.status_bar()
        self.fixed_sizes()
        self.search_pane_fixed_size()
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.search_base_tab.setCurrentIndex(1)
        #signals of the GUI.
        QtCore.QObject.connect(self.clear_button_adding, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clear_add_input)
        QtCore.QObject.connect(self.button_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clear_search_input)
        QtCore.QObject.connect(self.dropdown_add_district, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.set_add_street)
        QtCore.QObject.connect(self.district_dropdown_select, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.set_search_street)
        #QtCore.QObject.connect(self.district_dropdown_select, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.set_search_street)
        #QtCore.QObject.connect(self.district_dropdown_select, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.set_street_default)
        QtCore.QObject.connect(self.add_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.add_to_mysql)
        QtCore.QObject.connect(self.button_find, QtCore.SIGNAL(_fromUtf8("clicked()")), self.search_in_mysql)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

   # setting the floor numbers and the default items.
    def set_floors(self):
        self.floors_count.setText(_translate("MainWindow", "Հարկերի Քանակ", None))
        self.floors_count_2.setText(_translate("MainWindow", "Հարկերի Քանակ", None))
        self.floors_count_search.setItemText(0, _translate("MainWindow", "Բոլորը", None))
        self.dropdown_add_floors_count.setItemText(0, _translate("MainWindow", "Բոլորը", None))
        for i in range(1, self.floors_length) :
            self.floors_count_search.setItemText(i, _translate("MainWindow", str(i), None))
            self.dropdown_add_floors_count.setItemText(i, _translate("MainWindow", str(i), None))

    #setting the floor numbers and the default items.
    def set_floor_number(self): 
        self.floor.setText(_translate("MainWindow", "Հարկ", None))
        self.floors.setText(_translate("MainWindow", "Հարկ", None))
        self.search_the_floor_dropdown.setItemText(0, _translate("MainWindow", "Բոլորը", None))
        self.dropdown_add_thefloor.setItemText(0, _translate("MainWindow", "Բոլորը", None))
        for i in range(1, self.floors_length) :
            self.search_the_floor_dropdown.setItemText(i, _translate("MainWindow", str(i), None))
            self.dropdown_add_thefloor.setItemText(i, _translate("MainWindow", str(i), None))

   # setting the distrcits names.
    def set_district(self):
        self.district.setText(_translate("MainWindow", "Համայնք", None))
        self.district_add.setText(_translate("MainWindow", "Համայնք", None))
        for i in range(0, len(self.districts)) :
            self.district_dropdown_select.setItemText(i, _translate("MainWindow", self.districts[i], None))
            self.dropdown_add_district.setItemText(i, _translate("MainWindow", self.districts[i], None))

   # Default items for the streets.
    def set_street_default(self):
        self.street.setText(_translate("MainWindow", "Փողոց", None))
        self.street_add.setText(_translate("MainWindow", "Փողոց", None))
        self.dropdown_search_street.addItem(_fromUtf8(""))
        self.dropdown_search_street.setItemText(0, _translate("MainWindow", "Բոլորը", None))
        self.dropdown_search_street.setObjectName(_fromUtf8("dropdown_search_street"))
        self.dropdown_add_street.addItem(_fromUtf8(""))
        self.dropdown_add_street.setItemText(0, _translate("MainWindow", "Բոլորը", None))
        self.dropdown_add_street.setObjectName(_fromUtf8("dropdown_add_street"))

    # changing the streets in the add pane depending which district is selected
    def set_add_street(self):
        #self.street_add.setText(_translate("MainWindow", "Փողոց", None))
        i = self.dropdown_add_district.currentIndex()
        self.dropdown_add_street.clear()
        if i == 0:
                self.dropdown_add_street.addItem(_fromUtf8(""))
                self.dropdown_add_street.setItemText(0, _translate("MainWindow", "Բոլորը", None))
                self.dropdown_add_street.setObjectName(_fromUtf8("dropdown_add_street"))
                return
        k = self.streets_all[i - 1]
        for i in range(0, len(k)):
            self.dropdown_add_street.addItem(_fromUtf8(""))
            self.dropdown_add_street.setItemText(i, _translate("MainWindow", k[i], None))

   # changing the streets in the search pane depending which district is selected
    def set_search_street(self):
        i = self.district_dropdown_select.currentIndex()
        self.dropdown_search_street.clear()
        if i == 0:
            self.dropdown_search_street.addItem(_fromUtf8(""))
            self.dropdown_search_street.setItemText(0, _translate("MainWindow", "Բոլորը", None))
            self.dropdown_search_street.setObjectName(_fromUtf8("street_dropdown_search"))
            return
        k = self.streets_all[i - 1]
        for i in range(0, len(k)):
            self.dropdown_search_street.addItem(_fromUtf8(""))
            self.dropdown_search_street.setItemText(i, _translate("MainWindow", k[i], None))

    # setting the rooms in search and an add pane.
    def set_rooms(self):
        self.room.setText(_translate("MainWindow", "Սենյակ", None))
        self.rooms_add.setText(_translate("MainWindow", "Սենյակ", None))
        self.rooms_dropdown_search.setItemText(0, _translate("MainWindow", "Բոլորը", None))
        self.dropdown_add_rooms.setItemText(0, _translate("MainWindow", "Բոլորը", None))
        for i in range(1, 11):
            self.rooms_dropdown_search.setItemText(i, _translate("MainWindow", str(i), None))
            self.dropdown_add_rooms.setItemText(i, _translate("MainWindow", str(i), None))
            
    def set_currency(self):
        self.dropdown_add_currency.setFixedWidth(80)
        for i in range(0,len(self.currency)):
            self.dropdown_add_currency.addItem(_fromUtf8(""))
            self.dropdown_add_currency.setItemText(i, _translate("MainWindow", self.currency[i], None))

    def set_currency_search(self):
        self.dropdown_search_currency.setFixedWidth(80)
        for i in range(0, len(self.currency)):
            self.dropdown_search_currency.addItem(_fromUtf8(""))
            self.dropdown_search_currency.setItemText(i, _translate("MainWindow", self.currency[i], None))

     #retranslateUI for the name and labels. Also we call several functions here.
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.code.setText(_translate("MainWindow", "Կոդ", None))
        self.type.setText(_translate("MainWindow", "Տեսակ", None))
        self.checkbox_house.setText(_translate("MainWindow", "Առանձնատուն", None))
        self.checkbox_appartment.setText(_translate("MainWindow", "Բնակարան", None))
        self.checkbox_land.setText(_translate("MainWindow", "Հողատարածք", None))
        self.checkbox_other.setText(_translate("MainWindow", "Այլ", None))
        self.provide.setText(_translate("MainWindow", "Տրամադրում", None))
        self.checkbox_rent.setText(_translate("MainWindow", "Վարձակալություն", None))
        self.checkbox_sell.setText(_translate("MainWindow", "Վաճառք", None))
        self.home.setText(_translate("MainWindow", "Շենք/Տուն", None))
        self.set_floors()       #call of the function set_floors for looping in the drop down list of the floor and setting the items.
        self.set_floor_number() # call for the floor number : read the above comment.
        self.set_district()     # setting up the districts items.
        self.set_rooms()        # setting the items for rooms.
        self.set_street_default() # call for the dinamic function that changes the streets depending of the districts.
        self.square.setText(_translate("MainWindow", "Մակերես", None))
        self.label_2.setText(_translate("MainWindow", "Սկսած", None))
        self.label.setText(_translate("MainWindow", "-", None))
        self.label_3.setText(_translate("MainWindow", "Վերջացրած", None))
        self.price.setText(_translate("MainWindow", "Արժեք", None))
        self.label_4.setText(_translate("MainWindow", "Սկսած", None))
        self.label_5.setText(_translate("MainWindow", "֊", None))
        self.label_6.setText(_translate("MainWindow", "Վերջացրած", None))
        self.gorcakal.setText(_translate("MainWindow", "Գործակալ", None))
        self.button_clear.setText(_translate("MainWindow", "Մաքրել", None))
        self.button_find.setText(_translate("MainWindow", "Փնտրել", None))
        self.date.setText(_translate("MainWindow", "Ամսաթիվ", None))
        self.label_13.setText(_translate("MainWindow", "Սկսած", None))
        self.label_14.setText(_translate("MainWindow", "Վերջացրած", None))
        self.search_base_tab.setTabText(self.search_base_tab.indexOf(self.tab), _translate("MainWindow", "Բազա", None))
        self.type_add.setText(_translate("MainWindow", "Տեսակ", None))
        self.radio_button_house.setText(_translate("MainWindow", "Առանձնատուն", None))
        self.radioButton_appartament.setText(_translate("MainWindow", "Բնակարան", None))
        self.radio_button_land.setText(_translate("MainWindow", "Հողատարածք", None))
        self.radioButton_other.setText(_translate("MainWindow", "Այլ", None))
        self.provide_add.setText(_translate("MainWindow", "Տրամադրում", None))
        self.checkBox_rent.setText(_translate("MainWindow", "Վարձակալություն", None))
        self.checkBox_sell.setText(_translate("MainWindow", "Վաճառք", None))
        self.home_add.setText(_translate("MainWindow", "Շենք/Տուն", None))
        self.add_format_of_property.setText(_translate("MainWindow", "Ստուգել ֆորմատը", None))
        self.square_add.setText(_translate("MainWindow", "Մակերես", None))
        self.price_add.setText(_translate("MainWindow", "Արժեք", None))
        self.label_gorcakal.setText(_translate("MainWindow", "Գործակալ", None))
        self.clear_button_adding.setText(_translate("MainWindow", "Մաքրել", None))
        self.add_button.setText(_translate("MainWindow", "Ավելացնել", None))
        self.comment.setText(_translate("MainWindow", "Նշումներ", None))
        self.phonenumber_add.setText(_translate("MainWindow", "Հեռախոս ", None))
        self.search_base_tab.setTabText(self.search_base_tab.indexOf(self.tab_2), _translate("MainWindow", "Ավելացնել", None))

    def search_in_mysql(self):
        self.search_query = "SELECT * FROM Brok WHERE "
        #self.get_date()
        self.get_code()
        self.search_type_of_property()
        self.search_provision()
        self.distrcits_search()
        self.streets_search()
        self.format_of_house_search()
        self.room_search()
        self.floors_how_many_search()
        self.the_floor_search()
        self.square_meter()
        self.search_price()
        self.worker_search()
        self.search_query += ";"

        print self.search_query
        con = MySQLdb.connect('localhost', 'root', '1991', 'broker_database')
        #columns = "house_format,comments,phone_number,price,name_worker,type,purpose,district,street,room,floors_how_many,the_floor,square_meter,currency"
        #cursor = con.cursor()
        #cursor.execute(str(self.search_query))
        #cursor.execute("Select * from Brok where code=755")
        #cursor.execute("SELECT * FROM Brok WHERE code and district and street and house_format and room and floors_how_many and the_floor and square_meter and price and name_worker")
        #data = cursor.fetchall()
        #cursor.execute("SELECT * FROM Brok WHERE code and district and street and name_worker")
        #con.query(_fromUtf8(self.search_query))
        con.query(str(self.search_query))
        result = con.use_result()
        if result == None:
            print "Error: Failed to process query"
            return
        #data = result.fetch_row(maxrows=0)
        data = result.fetch_row(maxrows = 0)
        column_int = result.num_fields()
        row_int = result.num_rows()
        print column_int
        print row_int
        print data

    #def get_date(self):
     #  if self.date_from.text().isEmpty():
     #       self.search_query += " date "
     #   else:
     #       self.search_query += "date >='" + self.date_from.text() + "' AND date <='" + self.date_to.text() + " '"

    def get_code(self):
        if self.code_lineedit_search.text().isEmpty():
            self.search_query += " code "
        else:
            self.search_query += " code = " + self.code_lineedit_search.text()

    def search_type_of_property(self):
        k = [self.checkbox_house, self.checkbox_appartment, self.checkbox_land, self.checkbox_other]
        p = 0
        for i in k:
            if i.isChecked():
                p += 1
        if p == 0 :
            print "Info: Type was not selected"
            return
        if p == 4 :
            self.search_query += " and type "
            return
        self.search_query += " and ("
        o = 1
        for i in k:
            if i.isChecked() :
                self.search_query += " type = " + str(o)
                if o != p :
                    self.search_query += " or"
                o += 1
        self.search_query += " ) "

    def search_provision(self):
        if self.checkbox_rent.isChecked() and self.checkbox_sell.isChecked():
            self.search_query += " and purpose "
            return
        if self.checkbox_rent.isChecked():
            self.search_query += " and purpose = 1"
        if self.checkbox_sell.isChecked():
            self.search_query += " and purpose = 2"
        else:
            print "nothing has been selected"

    def distrcits_search(self):
        if self.district_dropdown_select.currentIndex() == 0:
            self.search_query += " and district  "
        else:
            self.search_query += " and district =" + str(self.district_dropdown_select.currentIndex())

    def streets_search(self):
        if self.dropdown_search_street.currentIndex() == 0:
            self.search_query += " and street  "
        else:
            self.search_query += " and street =" + str(self.dropdown_search_street.currentIndex())

    def format_of_house_search(self):
        if str(self.format_home_flat_search.text()) == '/':
            self.search_query += " and house_format  "
        else:
            self.search_query += " and house_format ='" + _fromUtf8(self.format_home_flat_search.text()) + "'"

    def room_search(self):
        #if type(self.rooms_dropdown_search.currentText() is str:
        if self.rooms_dropdown_search.currentIndex() == 0:
            self.search_query += " and room"
        else:
            self.search_query += " and room =" + str(self.rooms_dropdown_search.currentIndex())
            #self.search_query += " and room = " + str(6)

    def floors_how_many_search(self):
        if self.floors_count_search.currentIndex() == 0:
            self.search_query += " and floors_how_many  "
        else:
            self.search_query += " and floors_how_many ="+ str(self.floors_count_search.currentIndex())

    def the_floor_search(self):
        if self.search_the_floor_dropdown.currentIndex() == 0:
            self.search_query += " and the_floor  "
        else:
            self.search_query += " and the_floor =" + str(self.search_the_floor_dropdown.currentIndex())

    def square_meter(self):
        if self.search_square_from.text().isEmpty() and  self.search_square_to.text().isEmpty():
            self.search_query += " and square_meter "
        else:
            self.search_query += " and square_meter >=" + str(self.search_square_from.text()) + " and square_meter  <= " + str(self.search_square_to.text())

    def search_price(self):
        if self.price_from.text().isEmpty() and self.price_to.text().isEmpty():
            self.search_query += " and price "
        else:
            self.search_query += " and price >=" + str(self.price_from.text()) + " and price  <=" +str(self.price_to.text())

    def worker_search(self):
        if self.user_name_of_worker_search.text().isEmpty():
            self.search_query += " and name_worker "
        else:
            self.search_query += " and name_worker ='" + str(self.user_name_of_worker_search.text()) + "'"


# executing the GUI and calling the main window.
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

