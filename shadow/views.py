from django.shortcuts import render

def index(request):
    data = [{'name':'amir',"age":26},
            {'name':'ami',"age":2},
            {'name':'amr',"age":6},
            {'name':'mir',"age":30}]
    text = """;fehgikdfngjkdfngkd
    sfmgdgmd
    fg
    ;'ghghfg[h,f[jh,fg,h]]
        """

    return render(request, "practice.html", context={'peoples':data, 'text': text})


