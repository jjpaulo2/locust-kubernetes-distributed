from django.db.models import (
    Model,
    CharField,
    DateField,
    ForeignKey,
    FloatField,
    CASCADE
)


class Author(Model):
    name = CharField(max_length=100)
    birth_date = DateField()

    def __str__(self) -> str:
        return f"#{self.pk} - {self.name}"


class Book(Model):
    title = CharField(max_length=100)
    subtitle = CharField(max_length=255)
    author = ForeignKey(
        Author,
        on_delete=CASCADE
    )

    def __str__(self) -> str:
        return f"#{self.pk} - {self.title} - {self.author.name}"


class Consumer(Model):
    name = CharField(max_length=100)
    birth_date = DateField()
    document_cpf = CharField(max_length=11)

    def __str__(self) -> str:
        return f"#{self.pk} - {self.name} - {self.document_cpf}"


class Order(Model):
    consumer = ForeignKey(
        Consumer,
        on_delete=CASCADE
    )
    book = ForeignKey(
        Book,
        on_delete=CASCADE
    )
    price = FloatField()
    
    def __str__(self) -> str:
        return f"#{self.pk} - {self.consumer.name} - {self.price}"
