from django.contrib import admin

# Register your models here.
from django.contrib.admin import display

from manager_shop.models import Author, Publisher, \
    Book, Pageee, Shoe, Brand, MobilePhone, Memory, \
    Producer, Laptop, CPU, RAM, Electronic, Size, Vendor, Cloth


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['abbrev', 'firstName', 'lastName']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'publicationDate', 'print_authors', 'print_publisher', 'get_author', 'page']
    search_fields = ['title']

    @display(ordering='book__publisher', description='Publisher')
    def get_author(self, obj):
        return obj.publisher.name


@admin.register(Pageee)
class PageeeAdmin(admin.ModelAdmin):
    list_display = ['body']

# clothes
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'address']


@admin.register(Cloth)
class ClothAdmin(admin.ModelAdmin):
    list_display = ['color', 'style', 'size', 'str_vendor', 'price']

# electronics
@admin.register(Electronic)
class ElectronicAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'wattage', 'size', 'brand']


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['width', 'height', 'deep', 'weight']

#laptop
@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ['name', 'str_cpu', 'str_ram', 'drive']


@admin.register(CPU)
class CPUAdmin(admin.ModelAdmin):
    list_display = ['model', 'family', 'core', 'thread', 'frequency', 'brand']


@admin.register(RAM)
class RAMAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'bus', 'capacity']

#mobile
@admin.register(MobilePhone)
class MobileAdmin(admin.ModelAdmin):
    list_display = ['name', 'display', 'platform', 'str_memories', 'str_producer']


@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    list_display = ['ram', 'rom', 'cardSlot']


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']

#shoe
@admin.register(Shoe)
class ShoeAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'color', 'size', 'brand']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']

