# -*- encoding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

if not settings.DEBUG:
    encoding = 'utf-8'
    import sys
    reload(sys)
    sys.setdefaultencoding(encoding)

# Create your models here.
