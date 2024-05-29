from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from ticket.models import TicketModel
from .forms import ProfileimageForm


# Create your views here.
def upload_document(request):
    if request.method == 'POST' and request.FILES.get('documents'):
        uploaded_file = request.FILES['documents']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        # Optionally, save the file path to a model or perform other actions
        return redirect('upload_success')  # Redirect to a success page
    return render(request, 'documents/upload_document.html')


def my_view(request):
    if request.method == 'POST':
        form = ProfileimageForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the uploaded document here
            document = form.cleaned_data['document']
            # Save or handle the document as needed
    else:
        form = ProfileimageForm()
    return render(request, 'documents/upload_document.html', {'form': form})