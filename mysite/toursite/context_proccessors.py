from .models import Page
from .models import Option
from .models import TourCategory


def pages(request):
    return {
        'pages': Page.objects.all()
    }


def options(request):
    return {
        'options': Option.objects.all()
    }

def tour_categories(request):
    return {
        'tour_categories':TourCategory.objects.all()
    }