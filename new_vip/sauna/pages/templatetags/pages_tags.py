from django import template
from album.models import AlbumImage

register = template.Library()

def get_responsive_height(height, width):
    return height / widht * 100

def get_array(model):
    return model.all()
def get_photo(id):
    return AlbumImage.objects.filter(album=id)

register.filter('get_responsive_height', get_responsive_height)
register.filter('get_array', get_array)
register.filter('get_photo', get_photo)