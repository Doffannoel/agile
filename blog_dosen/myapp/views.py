from django.shortcuts import get_object_or_404, render , redirect
from .models import PKM, Activity, Publikasi, Research, ResearchGallery, Registration , Job, Subject
import json
from .forms import RegistrationForm
from django.contrib import messages

def publikasi_view(request):
    publikasi_list = Publikasi.objects.all()
    
    # Mengelompokkan jumlah kutipan berdasarkan tahun
    citation_data = {year: 0 for year in range(2017, 2025)}
    for publikasi in publikasi_list:
        if publikasi.tahun in citation_data:
            citation_data[publikasi.tahun] += publikasi.dikutip_oleh

    return render(request, 'myapp/publikasi.html', {
        'publikasi_list': publikasi_list,
        'citation_data': json.dumps(citation_data),  # Kirim data sebagai JSON
    })

def page_project(request):
    return render(request, 'myapp/project.html')

def research_detail(request, pk):
    # Mendapatkan proyek riset berdasarkan ID
    research_item = get_object_or_404(Research, pk=pk)
    
    # Mendapatkan gambar-gambar terkait riset dari model ResearchGallery, dibatasi hanya 3 gambar pertama
    gallery_images = ResearchGallery.objects.all()[:3]  # Membatasi hanya 3 gambar pertama
    
    # Render halaman dengan mengirimkan data proyek riset dan gambar-gambar
    return render(request, 'myapp/research_detail.html', {
        'research': research_item,
        'gallery_images': gallery_images,
    })
def landing_page(request):
    recent_activities = Activity.objects.all().order_by('-date')[:3]  # Latest 3 activities
    return render(request, 'myapp/landingpage.html', {'recent_activities': recent_activities})

def pkm_list(request):
    # Ambil status filter dari request (default 'all' jika tidak ada filter)
    status_filter = request.GET.get('status', 'all')

    # Ambil semua PKM
    pkm_list = PKM.objects.all()

    # Filter berdasarkan status jika pengguna memilih filter tertentu
    if status_filter == 'on_progress':
        pkm_list = pkm_list.filter(status='on_progress')
    elif status_filter == 'done':
        pkm_list = pkm_list.filter(status='done')

    return render(request, 'myapp/pkm_list.html', {
        'pkm_list': pkm_list,
        'selected_status': status_filter  # Kirim status terpilih ke template
    })

def pkm_detail(request, pk):
    pkm_item = get_object_or_404(PKM, pk=pk)
    return render(request, 'myapp/pkm_detail.html', {'pkm': pkm_item})


def project_gallery(request, id):
    # Get the specific research project by ID
    research = get_object_or_404(Research, pk=id)

    # Get the related gallery images for the specific research from the ResearchGallery model
    gallery_images = ResearchGallery.objects.filter(research=research)

    # Render the template with the research project and gallery images
    return render(request, 'myapp/project_gallery.html', {
        'research': research,
        'gallery_images': gallery_images,
    })

def teaching(request):
    subjects = Subject.objects.all()
    return render(request, 'myapp/teaching.html', {'subjects': subjects})

def teaching_detail(request, subject_slug):
    subject = get_object_or_404(Subject, slug=subject_slug)
    return render(request, 'myapp/teaching_detail.html', {'subject': subject})

def research_list(request):
    filter_type = request.GET.get('filter', 'all')
    
    # Mulai dengan mengambil semua riset
    researches = Research.objects.all()

    # Filter berdasarkan status
    if filter_type == 'on_progress':
        researches = researches.filter(status='on_progress')
    elif filter_type == 'done':
        researches = researches.filter(status='done')

    return render(request, 'myapp/research_list.html', {'researches': researches})

def job_list(request):
    # Mengambil semua data pekerjaan yang ada di database
    jobs = Job.objects.all().order_by('-posted_date')  # Urutkan berdasarkan tanggal posting
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Menyimpan data pendaftaran ke database
            messages.success(request, "Data has been saved!") 
            return redirect('success')  # Redirect ke halaman sukses setelah form disubmit
        else: 
            messages.error(request, f'Form Invalid: {form.errors}.')
    else:
        form = RegistrationForm()

    # Kirimkan data jobs dan form ke template
    return render(request, 'myapp/job_list.html', {'jobs': jobs, 'form': form})


def registration_success(request):
    return render(request, 'myapp/success.html',{})
