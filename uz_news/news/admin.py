from django.contrib import admin
from .models import News,Category

class NewAdmin(admin.ModelAdmin):
    list_display=('pk',
                  'title',
                  'category',
                  'created_at',
                  'updated_at',
                  'is_published'
                  )
    

admin.site.register(News,NewAdmin)
admin.site.register(Category)      

    

# Register your models here. 