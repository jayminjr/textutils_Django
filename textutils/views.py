# I have created this file - Jaymin
from django.http import HttpResponse
from django.shortcuts import render
import re


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.GET.get('text', 'defaulttext')
    radiovalue = request.GET.get('strop', 'defaultvalue')

    if radiovalue == 'removepunc':
        analyze_text = ""
        punclist = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punclist:
                analyze_text = analyze_text+char
        params = {'purpose': 'Removed Punctuations',
                  'analyzed_text': analyze_text}
        return render(request, 'analyze.html', params)
    elif radiovalue == 'uppercase':
        analyze_text = ""
        for char in djtext:
            analyze_text = analyze_text+char.upper()
        params = {'purpose': 'UPPERCASE', 'analyzed_text': analyze_text}
        return render(request, 'analyze.html', params)
    elif radiovalue == 'lowercase':
        analyze_text = ""
        for char in djtext:
            analyze_text = analyze_text+char.lower()
        params = {'purpose': 'lowercase', 'analyzed_text': analyze_text}
        return render(request, 'analyze.html', params)
    elif radiovalue == 'newlineremover':
        # print(djtext) before remove print in terminal
        analyze_text = ''.join(djtext.splitlines())
        # print(analyze_text) after remove print in terminal
        params = {'purpose': 'New Line Remove', 'analyzed_text': analyze_text}
        return render(request, 'analyze.html', params)
    elif radiovalue == 'extraspaceremover':
        print(djtext)
        # remove extra space using re import re fot that
        analyze_text = re.sub(' +', ' ', djtext)
        print(analyze_text)
        params = {'purpose': 'Extra Spaces remove',
                  'analyzed_text': analyze_text}
        return render(request, 'analyze.html', params)
    elif radiovalue == 'charcount':
        analyze_text = len(djtext)
        params = {'purpose': 'Extra Spaces remove',
                  'analyzed_text': analyze_text}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("error")
