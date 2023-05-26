from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    #Create groups of selections avaialble for favourite flower.
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
    
    fav_flower_family = models.CharField(choices=flower_family, max_length=35, default="bellflower")
    profile_pic = models.ImageField(
        upload_to='images/', default="https://res.cloudinary.com/dz1h0duk6/image/upload/v1683569094/default_rqwgw0.png"
    )
    
    class Meta():
        ordering = ['-created_at']

        def __str__(self):
            return f'{self.owners} profile'

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)