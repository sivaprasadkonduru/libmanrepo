# built-in imports
import os
from datetime import datetime

#third-party imports
import xlrd
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.decorators.cache import cache_page

#project-specific imports
from .models import Book
from .forms import BookForm


def create_books(request):

    books_file = r'C:\\Users\\User\\workspace\\libmanrepo\\libman\\Book1.xlsx'
    if os.path.exists(books_file):
        xl_workbook = xlrd.open_workbook(books_file)
        sheet_names = xl_workbook.sheet_names()
        xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])

        for row_idx in range(1, xl_sheet.nrows):
            data = xl_sheet.row_values(row_idx)
            year, month, day, hour, minute, second = xlrd.xldate_as_tuple(data[7], xl_workbook.datemode)
            issued_date = datetime(year, month, day).strftime('%Y-%m-%d')
            y, m, d, h, mn, s = xlrd.xldate_as_tuple(data[8], xl_workbook.datemode)
            return_date = datetime(y, m, d).strftime('%Y-%m-%d')
            #import pdb;pdb.set_trace()
            b, created = Book.objects.get_or_create(name=data[0], author=data[1], edition=data[2],
                                           category=data[3], publisher=data[4], reviews=data[5],
                                           available=data[6], issued_date=issued_date, return_date=return_date)
        return HttpResponse("Book details were added Successfully.")
    else:
        raise AttributeError("File path doesn't exist")


def add_book(request):

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise form.ValidationErrors('Enter valid data.')

        return HttpResponseRedirect('/book/all_books/')

    else:
        form = BookForm()

    return render(request, 'book_form.html', {'book_form': form})


@cache_page(3*60)
def get_books(request):
    data = Book.objects.all().order_by('-edition', 'reviews')
    return render(request, 'get_books.html', {'book_data': data})


class BookView(ListView):

    model = Book
    queryset = Book.objects.all()
    template_name = 'get_books.html'
    #context_object_name = 'books_data'


class BookFormView(FormView):

    form_class = BookForm
    success_url = '/book/list_books'
    template_name = 'book_form.html'

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)









