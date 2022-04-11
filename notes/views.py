from django.shortcuts import redirect, render
from django.template import RequestContext
from django.http import HttpResponse
from .models import Note, Tag
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    if request.method == "POST":
        title = request.POST.get("titulo")
        content = request.POST.get("detalhes")
        # Cria a anotacao
        note = Note(title=title, content=content)
        note.save()
        # Adiciona as tags
        tag = request.POST.get("tag")
        tags = tag.split(",")
        # Criando um note com os argumentos
        # Primeiro ve se essa tag ja existe -> evitar tags diferentes com o mesmo conteudo.
        for tag in tags:
            tag = tag.strip().capitalize()
            if tag != "":
                if not Tag.objects.filter(title=tag).exists():
                    tag = Tag(title=tag)
                    tag.save()
                else:
                    tag = Tag.objects.get(title=tag)
                note.tag.add(tag)
        return redirect("index")
    else:
        all_notes = Note.objects.order_by("id").all()
        return render(request, "notes/index.html", {"notes": all_notes})


def update(request):
    # TODO: Fazer o update funcionar com o manyToMany das tags.
    id = request.POST.get("id")
    title = request.POST.get("titulo")
    content = request.POST.get("detalhes")
    tag = request.POST.get("tag").strip()
    tags = tag.split(",")
    note = Note.objects.get(id=id)
    note.title = title
    note.content = content
    # Para remover as tag que foram possivelmente retiradas no update.
    note.tag.clear()
    # Se certifica que não é o placeholder ou uma tag vazia.
    for tag in tags:
        tag = tag.strip().capitalize()
        if tag != "Insira uma tag!" and tag != "":
            if not Tag.objects.filter(title=tag).exists():
                tag = Tag(title=tag)
                tag.save()
            else:
                tag = Tag.objects.get(title=tag)
            note.tag.add(tag)
    note.save()
    # Para updates chamados na tela de tags.
    if "tag" in request.path:
        return redirect(f"/tag/{tag.id}")
    return redirect("index")


@csrf_exempt
def delete(request, id):
    # Remove o item do banco de dados
    Note.objects.filter(id=id).delete()
    # Monta a resposta 303 See other apontando para o index
    response = HttpResponse(content="", status=303)
    response["Location"] = "../"
    return response


def tags(request):
    # Pega todas as tags únicas.
    all_tags = Note.objects.values("tag").distinct()
    tag_list = []
    for valor in all_tags:
        if valor["tag"] is not None:
            tag_list.append(Tag.objects.get(id=valor["tag"]))
    return render(request, "notes/alltags.html", {"tags": tag_list})


def tag(request, id):
    given_tag = Tag.objects.get(id=id)
    notes_with_tag = Note.objects.all().filter(tag=given_tag)
    return render(
        request, "notes/onetag.html", {"notes": notes_with_tag, "tag": given_tag}
    )
