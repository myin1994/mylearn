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


@register.simple_tag
def url_encode(requset, target_url, cid=''):
    from django.http import QueryDict

    transfer_qdict = QueryDict(mutable=True)
    obj = requset.GET.copy()
    if cid == '':
        target_url = reverse(target_url)
        transfer_qdict['next_url'] = requset.get_full_path()
    else:
        target_url = reverse(target_url, args=(cid,))
        transfer_qdict['next_url'] = requset.path + '?'+obj.urlencode()
    next_url = transfer_qdict.urlencode()
    fullpath = target_url + "?" + next_url
    return fullpath