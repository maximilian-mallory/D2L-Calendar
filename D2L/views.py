import os
from django.http import HttpResponse
from django.shortcuts import render

from D2L.models import Assignment
from combo_calendar import settings
from .Controller.getContent import regex_search_in_file

def Calendar( request ):

    context = {}
    context['message'] = "Welcome!"

    if request.method == 'POST':
        coursename = request.POST.get('coursename')
        file_name = f'{coursename}.txt'
        text_content = request.POST.get('htmltext')
        file_path = os.path.join(settings.BASE_DIR, 'D2L/HtmlText', file_name)
        print(file_path)
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(text_content)
        except Exception as e:
                    return HttpResponse(f'Error saving file: {str(e)}')
        
        pattern = r'd2l_1_143_936"[\s\S]+?">(.+?)<[\s\S]+?d2l_1_90_96 d2l_1_145_398">(.+?)<'
        regex_search_in_file(file_path, pattern)

        assignments = Assignment.objects.all()
        
        context['assignments'] = assignments

        return render(request, 'calendar.html', context)
    
    #file_path = os.path.join(settings.BASE_DIR, 'D2L/envsci.txt')
    
    

    return render(request, 'calendar.html', context)

def AddClass( request ):
    context = {}

    return render(request, 'addFile.html', context)

