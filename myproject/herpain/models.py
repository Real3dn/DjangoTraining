from django.db import models
from django.contrib import auth
# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=50,help_text="Enter your publisher name...")
    website = models.URLField(blank=True, help_text="Enter your publisher website...")
    email = models.EmailField(blank=True, help_text="Enter your publisher email...")
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=70,help_text="Enter your book title...")
    publication_date = models.DateField(verbose_name="Date of the publication")
    isbn = models.CharField(blank=True, max_length=20, verbose_name="ISBN Number of the book")
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    contributor = models.ManyToManyField('Contributor', through='BookContributor')
    def __str__(self):
        return self.name

class Contributor(models.Model):
    first_name = models.CharField(max_length=50, help_text="Enter your first name...")
    last_name = models.CharField(max_length=50, help_text="Enter your last name...")
    email = models.EmailField(blank=True, help_text="Enter your email...")
    def __str__(self):
        return self.name


class BookContributor(models.Model):
    class ContributorRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co_Author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="The role of the contributor in this book", choices=ContributorRole.choices,max_length=20)

class Review(models.Model):
    content = models.TextField(help_text="The review context")
    rating = models.IntegerField(help_text="The rating of this book")
    date_created = models.DateTimeField(auto_now_add=True,help_text="Date of the review written")
    date_edited = models.DateTimeField(auto_now_add=True ,help_text="Date of the edit", null=True)
    creator = models.ForeignKey(auth.get_user_model(),on_delete=models.CASCADE)
    book = models.ForeignKey(Book,help_text="The book that is being reviewed",on_delete=models.CASCADE)
    
