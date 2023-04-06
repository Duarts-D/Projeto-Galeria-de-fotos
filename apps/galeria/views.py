from django.shortcuts import render, get_object_or_404,redirect
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForm
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request,'Usuario nao logado')
        return redirect('login')
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)
    return render(request,'index.html',{'cards': fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request,'imagem.html',{'fotografia': fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request,'Usuario nao logado')
        return redirect('login')
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)
    if 'q' in request.GET:
        nome_a_buscar = request.GET['q']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    return render(request, 'index.html',{'cards': fotografias})

def nova_imagem(request):
    form = FotografiaForm()
    if request.method == 'POST':
        form = FotografiaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Enviado com sucesso')
            return redirect('index')
    return render(request, 'nova_imagem.html',{'form':form})
def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForm(
    instance=fotografia,
    )
    if request.method == 'POST':
        form = FotografiaForm(request.POST,request.FILES,instance=fotografia)
        form.save()
        messages.success(request,'Editado com sucesso')
        return redirect('index')
    return render(request,'editar_imagem.html',{'form':form})

def deletar_imagem(request,foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    messages.success(request,f'Fotografia Deletada com sucesso {fotografia}')
    fotografia.delete()
    return redirect('index')

def filtro(request,categoria):
    categoria = Fotografia.objects.filter(categoria=categoria)
    return render(request,'index.html',{'cards':categoria})