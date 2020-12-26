from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DeleteView,TemplateView
from .models import Partida
from django.urls import reverse_lazy

# Create your views here.

class InicioView(TemplateView):
    template_name = "inicio.html"


class PartidaListView(ListView):
    model = Partida
    template_name = "partida/lista.html"
    context_object_name = 'lista_partidas'
    paginate_by = 4

class PartidaCreateView(CreateView):
    model = Partida
    template_name = "partida/add.html"
    fields= ('__all__')
    success_url = reverse_lazy('partida_app:lista_partidas')


class PartidaUpdateView(UpdateView):
    model = Partida
    template_name = "partida/update.html"
    fields = ('__all__')
    success_url = reverse_lazy('partida_app:lista_partidas')

    #def post(self, request, *args, **kwargs):
        #self.object = self.get_object()
        #return super().post(request, *args, **kwargs)

class PartidaDeleteView(DeleteView):
    model = Partida
    template_name = "partida/delete.html"
    success_url = reverse_lazy('partida_app:lista_partidas')

    
    