from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    title = models.CharField(max_length=60)
    image = models.ImageField(
        upload_to='images/'
    )
    flower_family =[ 
        ('peruvian_lily','Peruvian Lily'),
        ('colchicum','Colchicum'),
        ('lily','Lily'),
        ('orchid','Orchid'),
        ('iris','Iris'),
        ('asphodel','Asphodel'),
        ('daffodil','Daffodil'),
        ('asparagus','Asparagus'),
        ('poppy','Poppy'),
        ('buttercup','Buttercup'),
        ('saxifrage','Saxifrage'),
        ('stonecrop','Stonecrop'),
        ('pea','Pea'),
        ('rose','Rose'),
        ('spurge','Spurge'),
        ('violet','Violet'),
        ('st_johns_wort','St Johns Wort'),
        ('geranium','Geranium'),
        ('loosestrife','Loosestrife'),
        ('willow_herb','Willow-herb'),
        ('mallow','Mallow'),
        ('rock_rose','Rock Rose'),
        ('cabbage','Cabbage'),
        ('sea_lavender','Sea Lavender'),
        ('pink','Pink'),
        ('phlox','Phlox'),
        ('primrose','Primrose',),
        ('heath','Heath'),
        ('periwinkle','Periwinkle'),
        ('borage','Borage'),
        ('convolvulus','Convolvulus'),
        ('nightshade','Nightshade'),
        ('olive','Olive'),
        ('plantain','Plantain'),
        ('figwort','Figwort'),
        ('mint','Mint'),
        ('acanthus','Acanthus'),
        ('verbena','Verbena'),
        ('bellflower','Bellflower'),
        ('daisy','Daisy'),
        ('umbellifer','Umbellifer'),
        ('honeysuckle','Honeysuckle'),
        ]
    flower_tag = models.CharField(max_length=20, choices=flower_family)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} by {self.owner}'