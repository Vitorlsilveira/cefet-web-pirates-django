from django.shortcuts import render
from django.views import View
from django.db.models import F,ExpressionWrapper,DecimalField, Sum
from pirates.models import Tesouro
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

class ListaTesourosView(View):
    def get(self, request):
        return render(request, "lista_tesouros.html",{'lista_tesouros': Tesouro.objects.annotate(valor_total=ExpressionWrapper(F('preco')*F('quantidade'),output_field=DecimalField(max_digits=10,decimal_places=2,blank=True))) , "total_geral" : Tesouro.objects.aggregate(total_geral = Sum(ExpressionWrapper(F('preco')*F('quantidade'),output_field=DecimalField(max_digits=10,decimal_places=2,blank=True))))['total_geral']})

class TesouroForm(forms.ModelForm):
    class Meta:
        model = Tesouro
        fields = ['nome', 'quantidade', 'preco', 'img_tesouro' ]
        labels = {"nome": "Nome", "quantidade" : "Quantidade", "preco" : "Preco", "img_tesouro" : "Imagem"}

class SalvarTesouro(View):
    def get(self,request, id=None): #Requisitou a exibição do formulário
        tesouro = Tesouro.objects.get(id=id) if id != None else None
        return render(request,"salvar_tesouro.html",{"tesouro":TesouroForm(instance=tesouro)})

    def post(self,request,id=None):#via post, salva o tesouro
        tesouro = Tesouro.objects.get(id=id) if id != None else None
        form = TesouroForm(request.POST,request.FILES, instance=tesouro)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lista_tesouros') )
        else:
            return render(request,"salvar_tesouro.html",{"tesouro":form})

class RemoverTesouro(View):
    def get(self,request, id):
        Tesouro.objects.filter(id = id).delete()
        return HttpResponseRedirect(reverse('lista_tesouros'))