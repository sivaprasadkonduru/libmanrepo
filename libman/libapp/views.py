# built-in imports
import os

#third-party imports
import xlrd
from django.shortcuts import render

#project-specific imports
from .models import Book


def create_books(request):

    books_file = r'C:\\Users\\User\\workspace\\libmanrepo\\libman\\Book1.xlsx'
    if os.path.exists(books_file):
        xl_workbook = xlrd.open_workbook(books_file)
        sheet_names = xl_workbook.sheet_names()
        xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])
        for row_idx in range(1, xl_sheet.nrows):
            data = xl_sheet.row_values(row_idx)
            b = Book.objects.get_or_create(name=data[0], author=data[1], edition=data[2],
                                           category=data[3], publisher=data[4], reviews=data[5],
                                           available=data[6], issued_date=data[7], return_date=data[8])
    else:
        raise AttributeError("File path doesn't exist")
