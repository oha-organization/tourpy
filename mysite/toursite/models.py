from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
# Create your models here.
class Page(models.Model):
    """A model of a post."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(default='', max_length=200, blank=True)
    link = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField()
    content = RichTextField()
    status = models.CharField(choices=(
            ('y', "Yayinda"),
            ('t', "Taslak"),
        ),
        max_length=1
    )
    page_type = models.CharField(choices=(
            ('u', "Üst menü"), 
            ('y', "Yan Menü"),
            ('a', "Alt Menü"),
        ),
        max_length=1
    )
    order = models.IntegerField()
    parent = models.ForeignKey("Page", on_delete=models.SET_NULL, null=True, blank=True)

    def get_absolute_url(self):
        """Returns the url to access a particular post instance."""
        # return reverse('post-detail', kwargs={'slug': self.slug})
        if self.link:
            return self.link
        else:
            return reverse('page-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title+"-"+self.page_type


class Option(models.Model):
    """A model of options """
    name = models.CharField(max_length=200)
    description = models.TextField()
    content = RichTextField()

    def __str__(self):
        return self.name

class Slide(models.Model):
    title = models.CharField(max_length=500)
    Description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class TourCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(default='', max_length=200, blank=True)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        """Returns the url to access a particular post instance."""
        # return reverse('post-detail', kwargs={'slug': self.slug})
        return reverse('category-detail', kwargs={'slug': self.slug})

class Tour(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(default='', max_length=200, blank=True)
    Description = models.TextField()
    tour_program = RichTextField()
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a particular post instance."""
        # return reverse('post-detail', kwargs={'slug': self.slug})
        return reverse('tour-detail', kwargs={'slug': self.slug})

class TourPhotos(models.Model):
    tour= models.ForeignKey("Tour", on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title

class CategoryTour(models.Model):
    class Meta:
        # Add verbose name
        verbose_name = 'Category-Tour Relations'
    category=models.ForeignKey("TourCategory", on_delete=models.CASCADE, null=False, blank=False)
    tour=models.ForeignKey("Tour", on_delete=models.CASCADE, null=False, blank=False)
    def __str__(self):
        return self.category.title+"-"+self.tour.title

class TourPrices(models.Model):
    tour= models.ForeignKey("Tour", on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(max_length=200)
    begin_date=models.DateField()
    end_date=models.DateField()
    price_dollar_for_single=models.FloatField()
    price_dollar_for_double=models.FloatField()
    price_dollar_for_with_child=models.FloatField()
