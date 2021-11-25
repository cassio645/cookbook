from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from .models import Receita, Categoria
from django.urls import reverse_lazy



class IndexView(ListView):
    model = Receita
    context_object_name = 'receitas'
    paginate_by = 9

    # iniciando a categoria com None
    categoria = None

    def get_queryset(self):
        # query set recebendo todas as receitas
        queryset = Receita.objects.all()

        # pegando a categoria selecionada pelo filtro(se houver)
        categoria_slug = self.kwargs.get("slug")
        if categoria_slug:
            # caso haja ele vai filtrar o queryset com a categoria desejada
            self.categoria = get_object_or_404(Categoria, slug=categoria_slug)
            # reescrevendo o queryset
            queryset = queryset.filter(categoria=self.categoria)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # categoria selecionada
        context["categoria"] = self.categoria
        # todas as categorias
        context["categorias"] = Categoria.objects.all()
        return context



class DetalheView(DetailView):
    context_object_name = 'receita'
    queryset = Receita.objects.all()
