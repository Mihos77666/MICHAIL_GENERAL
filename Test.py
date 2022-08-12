from tkinter import Tk, filedialog
import os
from tabula import read_pdf
import openpyxl
from openpyxl.styles import Font, Color
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.styles import Font
from openpyxl.styles import Color, PatternFill, Font, Border
from openpyxl.styles import colors
from openpyxl.cell import Cell
from openpyxl.styles import Alignment
from openpyxl.utils import quote_sheetname
from openpyxl import Workbook
from openpyxl.styles import Color, PatternFill, Font, Border
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.formatting.rule import ColorScaleRule, CellIsRule, FormulaRule, Rule
import glob
import pandas as pd
import fitz
import constants as cs
