from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Note
from .forms import NoteForm

# User k notes ki list dikhane ka view
@login_required
def note_list(request):
    query = request.GET.get('q', '')                    # Search query
    notes = Note.objects.filter(owner=request.user)     # Sirf current user k notes

    if query:
        notes = notes.filter(title__icontains=query) | notes.filter(content__icontains=query)

    notes = notes.order_by('-updated_at')
    return render(request, 'notes/note_list.html', {
        'notes': notes,
        'query': query
    })


# Naya note banane ka view
@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user                   # Owner set karna
            note.save()
            messages.success(request, 'Note successfully created!')
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form, 'title': 'New Note'})


# Note edit karne ka view
@login_required
def note_edit(request, id):
    note = get_object_or_404(Note, id=id, owner=request.user)  # Sirf apnay note
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note updated successfully!')
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form, 'title': 'Edit note'})


# Note delete confirmation view
@login_required
def note_delete(request, id):
    note = get_object_or_404(Note, id=id, owner=request.user)
    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Note deleted successfully!')
        return redirect('note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})


# User registration view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created succesfully! Login now!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'notes/register.html', {'form': form})