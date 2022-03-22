from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Note
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    if request.method == "POST":
        title = request.POST.get("titulo")
        content = request.POST.get("detalhes")
        # Criando um note com os argumentos
        note = Note(title=title, content=content)
        note.save()
        return redirect("index")
    else:
        all_notes = Note.objects.order_by("id").all()
        return render(request, "notes/index.html", {"notes": all_notes})


def update(request):
    id = request.POST.get("id")
    title = request.POST.get("titulo")
    content = request.POST.get("detalhes")
    note = Note.objects.get(id=id)
    note.title = title
    note.content = content
    note.save()
    return redirect("index")


@csrf_exempt
def delete(request, id):
    # Remove o item do banco de dados
    Note.objects.filter(id=id).delete()
    # Monta a resposta 303 See other apontando para o index
    response = HttpResponse(content="", status=303)
    response["Location"] = "../"
    return response
