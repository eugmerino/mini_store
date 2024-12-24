from django.contrib import admin
from .models import Product

#-------- Admin site --------
admin.site.index_title = "MiniStore"
admin.site.site_header = "MiniStore"
admin.site.site_title = "MiniStore"
# ---------------------------

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name', 'code')

# Registro de modelos en el admin
#admin.site.register(Product)