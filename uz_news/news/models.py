from django.db import models
class Category(models.Model):
     title=models.CharField(max_length=150,verbose_name="Kategorya nomi")
     def __str__(self):
         return self.title
     
     class Meta:
        verbose_name="Kategoriya"
        verbose_name_plural="Kategoriyalar"
        
class News(models.Model):
    title=models.CharField(max_length=150,verbose_name="Sarlavha")
    description=models.TextField(verbose_name="Malumotlar")
    created_at=models.DateTimeField(verbose_name="Yaratilgan vaqt",auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True,verbose_name="Yangilangan vaqt")
    photo=models.ImageField(upload_to='photos/',blank=True,null=True,verbose_name='Rasmlar')
    is_published=models.BooleanField(default=True,verbose_name="Nashr etilganlik")
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Kategoria')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Yangilik"
        verbose_name_plural='Yangiliklar'