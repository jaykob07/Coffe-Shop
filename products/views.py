from django.urls import reverse_lazy
from django.views import generic
from .forms import ProductForm
from products.models import Products


class ProductFormView(generic.FormView):
    template_name = "products/add_products.html"
    form_class = ProductForm
    success_url = reverse_lazy('add_product')

    def form_valid(self, form):    # metodo para guardar el formulario 
        form.save()
        return super().form_valid(form)
    
class ProductListView(generic.ListView):
    model = Products
    template_name = 'products/list_product.html'
    context_object_name = 'products'