from django.shortcuts import render

def main_page(request):
    return render(request, 'main/index.html')


def error404(request, exception):
    return render(request, '../templates/error_404.html', status = 404)

def error500(request,  *args, **argv):
    return render(request, '../templates/error_500.html', status = 500)
