from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Publikasi, PKM, Research, ResearchGallery , Registration, Subject,  LearningOutcome, Job


# Registering the Publikasi model
admin.site.register(Publikasi)

# PKM model admin
class PKMAdmin(admin.ModelAdmin):
    list_display = ('judul', 'tanggal', 'deskripsi')  # Display these fields in the list
    search_fields = ('judul', 'deskripsi')  # Make these fields searchable
    list_filter = ('tanggal',)  # Allow filtering by 'tanggal'

    def gambar_tag(self, obj):
        return mark_safe(f'<img src="{obj.gambar.url}" width="100" height="100" />')
    gambar_tag.short_description = 'Image'
    
admin.site.register(PKM, PKMAdmin)


# ResearchGallery Inline
class ResearchGalleryInline(admin.TabularInline):
    model = ResearchGallery
    extra = 1

# Research model admin
class ResearchAdmin(admin.ModelAdmin):
    # Menambahkan 'status' ke dalam list_display untuk menampilkan status di daftar
    list_display = ('judul', 'tanggal', 'deskripsi', 'metodologi', 'hasil', 'status', 'gambar_tag')
    
    # Menambahkan 'status' ke dalam search_fields untuk memungkinkan pencarian berdasarkan status
    search_fields = ('judul', 'deskripsi', 'status')  # Mengizinkan pencarian berdasarkan judul, deskripsi, dan status
    
    # Menambahkan 'status' ke dalam list_filter untuk memungkinkan filter berdasarkan status
    list_filter = ('tanggal', 'status')  # Mengizinkan filter berdasarkan tanggal dan status
    
    # Menambahkan ResearchGalleryInline untuk gambar
    inlines = [ResearchGalleryInline]
    
    # Menambahkan fieldsets untuk memilih status ketika menambah atau mengedit riset
    fieldsets = (
        (None, {
            'fields': ('judul', 'deskripsi', 'gambar', 'tanggal', 'metodologi', 'hasil', 'status')
        }),
    )
    
    # Menambahkan method untuk menampilkan gambar di admin interface
    def gambar_tag(self, obj):
        return mark_safe(f'<img src="{obj.gambar.url}" width="100" height="100" />')
    gambar_tag.short_description = 'Image'

# Mendaftarkan ResearchAdmin ke model Research
admin.site.register(Research, ResearchAdmin)
admin.site.register(ResearchGallery)
admin.site.register(Registration)

class LearningOutcomeInline(admin.TabularInline):
    model = LearningOutcome
    extra = 1  

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = (
        'title', 'description', 'course_description', 
        'course_delivery', 'forms_of_learning', 'learning_methods',
        'rps_file', 'slug', 'image',
    )
    prepopulated_fields = {"slug": ("title",)}
    inlines = [LearningOutcomeInline]

# Oprec Job Admin
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'posted_date', 'image_tag')  # Add image_tag here
    search_fields = ('title', 'company', 'location')
    list_filter = ('posted_date',)
    
    # Add a method to display the image in the admin
    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
        return "No Image"
    image_tag.short_description = 'Image'

admin.site.register(Job, JobAdmin)