from django.contrib import admin

# Register your models here.

from .models import City
from .models import Post
from .models import Language
from .models import Rtype
from .models import BTL
from .models import item
from .models import specs
from .models import Upost



admin.site.register(City)
admin.site.register(Post)
admin.site.register(Language)
admin.site.register(Rtype)
admin.site.register(BTL)
admin.site.register(item)
admin.site.register(specs)
admin.site.register(Upost)
