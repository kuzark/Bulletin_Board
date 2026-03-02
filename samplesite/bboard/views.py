from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Bb, Rubric
from .forms import BbForm

def index(request):
    # А здесь сначала загрузка шаблона
    template = loader.get_template('bboard/index.html') 
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {
        'bbs': bbs,
        'rubrics': rubrics,
    }
    return HttpResponse(template.render(context=context, request=request))


def rubric_bbs(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id) # pk - Primary Key
    context = { # Связь переменных представления с переменными шаблона
        'bbs': bbs,
        'rubrics': rubrics,
        'current_rubric': current_rubric,
    }
    # Более краткая функция рендеринга шаблона
    return render(request, 'bboard/rubric_bbs.html', context) 


class BbCreateView(CreateView):
    '''Обработчик формы для внесения новых объявлений '''
    template_name = 'bboard/bb_create.html'
    form_class = BbForm
    success_url = reverse_lazy('index') # Подставляет url главной страницы

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context