import helpers
from cloudinary import CloudinaryImage
from django.contrib import admin
from django.utils.html import format_html
from django.contrib import admin
from .models import Course
# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # inlines = [LessonInline]
    list_display = ['title', 'status', 'access']
    list_filter = ['status', 'access']
    fields = ['title', 'description', 'status', 'image', 'access', 'display_image']
    readonly_fields = ['display_image']

    def display_image(self, obj, *args, **kwargs):
        url = obj.image_admin_url
        # url = helpers.get_cloudinary_image_object(
        #     obj, 
        #     field_name='image',
        #     width=200
        # )
        return format_html(f"<img src={url} />")

    display_image.short_description = "Current Image"
# admin.site.register(Course)
