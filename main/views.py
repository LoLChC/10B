from django.shortcuts import render
from .models import VisitorLog

def log_visitor(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        
        VisitorLog.objects.create(
            ip_address=ip,
            path=request.path,
            method=request.method,
            host=request.get_host(),
            user_agent=request.META.get('HTTP_USER_AGENT', ''),
            accept_language=request.META.get('HTTP_ACCEPT_LANGUAGE', ''),
            referer=request.META.get('HTTP_REFERER', ''),
            is_secure=request.is_secure(),
            session_key=request.session.session_key if hasattr(request, 'session') else None,
        )
    except Exception:
        pass

def index(request):
    log_visitor(request)
    return render(request, 'index.html')

def sevval(request):
    log_visitor(request)
    return render(request, 'sevval.html')


def merve(request):
    log_visitor(request)
    return render(request, 'merve.html')