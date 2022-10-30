from django.contrib.admin import (
    ModelAdmin,
    display,
    register
)

from api.models import (
    Author,
    Book,
    Consumer,
    Order
)


@register(Author)
class AuthorAdmin(ModelAdmin):
    list_display = (
        'pk',
        'name',
        'birth_date'
    )
    list_display_links = (
        'pk',
        'name'
    )


@register(Book)
class BookAdmin(ModelAdmin):
    list_display = (
        'pk',
        'title',
        'subtitle',
        'author_name'
    )
    list_display_links = (
        'pk',
        'title'
    )

    @display
    def author_name(self, obj: Book) -> str:
        return obj.author.name


@register(Consumer)
class ConsumerAdmin(ModelAdmin):
    list_display = (
        'pk',
        'name',
        'birth_date'
    )
    list_display_links = (
        'pk',
        'name'
    )


@register(Order)
class OrderAdmin(ModelAdmin):
    list_display = (
        'pk',
        'consumer_name',
        'book_title',
        'price'
    )

    @display
    def consumer_name(self, obj: Order) -> str:
        return obj.consumer.name

    @display
    def book_title(self, obj: Order) -> str:
        return obj.book.title
