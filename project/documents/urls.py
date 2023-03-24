from django.urls import path
from .views import DocumentList, DocumentDetail, DocumentDeleteView, doc_filter, DocumentCreateView, DocumentUpdateView, ImageDeleteView

from .models import Document

urlpatterns = [
    path('document',
         DocumentList.as_view(queryset=Document.objects.all().order_by('dateCreate'), template_name='documents.html'),
         name='docs'),
    path('<int:pk>', DocumentDetail.as_view(), name='document'),
    path('delete/<int:pk>', DocumentDeleteView.as_view(), name='doc_delete'),
    path('edit/<int:pk>', DocumentUpdateView.as_view(), name='_edit'),
    path('search', doc_filter, name='doc_filter'),
    path('create', DocumentCreateView.as_view(), name='_add'),
    path('delete-image/<int:image_id>', ImageDeleteView.as_view(), name='delete-image'),
]