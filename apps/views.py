from math import ceil

from django.shortcuts import render

from apps.models import Employee


def index_view(request):
    employees = Employee.objects.order_by('-joined_at')

    page = int(request.GET.get('page', 1))
    last_page_number = -1

    search = request.GET.get('search')
    if search:
        employees = employees.filter(job__name__icontains=search)
    elif page:
        page_size = 2
        employees = employees[page_size * (page - 1): page_size * page]
        last_page_number = ceil(Employee.objects.count() / page_size)

    context = {
        'employees': employees,
        'last_page_number': last_page_number
    }
    return render(request, 'apps/index.html', context)


