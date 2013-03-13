from django.core.context_processors import csrf


def CSRF_Token(request):
    """
    Function to get the csrf_token to be passed to the forms.
    """
    csrf_token = csrf(request)
    csrf_token_value = csrf_token.get('csrf_token', '')
    if csrf_token_value == 'NOTPROVIDED':
        return ''
    return u'<div style="display:none"><input type="hidden" name="csrfmiddlewaretoken" value="%s" /></div>' % csrf_token_value
