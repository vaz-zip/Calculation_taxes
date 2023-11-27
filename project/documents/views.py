from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import datetime
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, RedirectView
from .models import Document, Image
from .filters import DocFilter
from .forms import DocumentCreateForm, DocumentForm


class DocumentList(LoginRequiredMixin, ListView):
    model = Document
    template_name = 'documents.html'
    context_object_name = 'documents'
    queryset = Document.objects.all()
    filter_class = DocFilter  # вновь
    paginate_by = 4

    def get_queryset(self):
        self.filter = self.filter_class(self.request.GET, super().get_queryset().filter(author_id=self.request.user.id))
        return self.filter.qs.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        context['list_in_page'] = self.paginate_by
        context['filter'] = DocFilter(self.request.GET, queryset=self.get_queryset())
        return context


class DocumentDetail(LoginRequiredMixin, DetailView):
    model = Document
    template_name = 'document.html'
    context_object_name = 'document'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Document.objects.get(pk=id)


class DocumentDeleteView(LoginRequiredMixin, DeleteView):
    model = Document
    template_name = 'doc_delete.html'
    context_object_name = 'document'
    success_url = '/documents/document'


# def doc_filter(request):
#     f = DocFilter(request.GET, queryset=Document.objects.all())
#     return render(request, '_filtr.html', {'filter': f})


class DocumentCreateView(LoginRequiredMixin, CreateView):
    template_name = '_add.html'
    form_class = DocumentCreateForm

    def get_success_url(self) -> str:
        return '/documents/document'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('images')
        if form.is_valid():
            form.cleaned_data.pop('images')
            document = Document.objects.create(**(form.cleaned_data) | {'author': request.user})
            Image.objects.bulk_create(
                [Image(file=file, document=document) for file in files]
            )
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)


class DocumentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = '_edit.html'
    form_class = DocumentForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Document.objects.get(pk=id)


class ImageDeleteView(LoginRequiredMixin, RedirectView):
    def post(self, request, image_id: int, *args, **kwargs):
        document_id = Image.objects.filter(id=image_id).values('document_id').first()['document_id']
        Image.objects.filter(id=image_id).delete()

        return redirect(to=reverse('document', kwargs={
            'pk': document_id,
        }))
