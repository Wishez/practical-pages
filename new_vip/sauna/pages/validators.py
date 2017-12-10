# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def validate_slug_field(value):
    pattern = re.compile('^([a-z_]+)$')
    pattern.match(value)
    if pattern.match(value) is None:
        raise ValidationError(
            _('Значение "%(value)s" должно состоять из латинских букв и нижних подчёркиваний.'),
            params={'value': value},
        )