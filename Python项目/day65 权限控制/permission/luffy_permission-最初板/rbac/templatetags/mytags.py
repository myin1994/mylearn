from django import template
from django.urls import reverse
register = template.Library()

@register.filter
def tag_auth(request,current_path):
    import re
    allowed_url = request.session.get("allowed_url")
    for url in allowed_url:
        if re.match(f'^{url.get("roles__permissions__url")}$', current_path):
            return 'allow'
    else:
        return 'remove'