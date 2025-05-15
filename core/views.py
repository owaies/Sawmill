from rest_framework import viewsets, status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import SiteContent
from .serializers import SiteContentSerializer


class SiteContentViewSet(viewsets.ModelViewSet):
    """API ViewSet for managing site content."""
    queryset = SiteContent.objects.all()
    serializer_class = SiteContentSerializer


def login_view(request):
    """User login view."""
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('/admin-panel/')
        return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


@login_required
def admin_panel_view(request):
    """View to render the custom admin panel."""
    return render(request, 'admin.html')


def index_view(request):
    """Home page rendering with dynamic content."""
    sections = {
        'home': SiteContent.objects.filter(section='home'),
        'about': SiteContent.objects.filter(section='about'),
        'products': SiteContent.objects.filter(section='products'),
        'gallery': SiteContent.objects.filter(section='gallery'),
        'contact': SiteContent.objects.filter(section='contact'),
        'theme': SiteContent.objects.filter(section='theme'),
    }

    # Extract content from each section
    home = sections['home']
    about = sections['about']
    products = sections['products']
    gallery = sections['gallery']
    contact = sections['contact']
    theme = sections['theme']

    # Home section
    home_hero_text = home.filter(key='heroText').first().value if home.filter(key='heroText').exists() else 'Default Hero Text'
    home_intro_text = home.filter(key='homeIntroText').first().value if home.filter(key='homeIntroText').exists() else 'Default Intro Text'
    home_bg = home.filter(key='heroBackground').first()
    home_bg_url = home_bg.image.url if home_bg and home_bg.image else ''

    # About section
    about_text = about.filter(key='aboutText').first().value if about.filter(key='aboutText').exists() else 'Default About Text'

    # Products section
    products_list = [product.value for product in products if product.key.startswith('product')]

    # Gallery section (handle ImageField)
    gallery_images = [
        {'image': g.image.url, 'alt_text': g.key} for g in gallery if g.image
    ]

    # Contact section
    contact_email = contact.filter(key='email').first().value if contact.filter(key='email').exists() else 'info@sawmill.com'
    contact_phone = contact.filter(key='phone').first().value if contact.filter(key='phone').exists() else '+123-456-7890'
    contact_address = contact.filter(key='address').first().value if contact.filter(key='address').exists() else '123 Timber Lane, Woodville'
    contact_map_url = contact.filter(key__iexact='mapUrl').first().value if contact.filter(key__iexact='mapUrl').exists() else 'https://maps.google.com'

    # Theme settings
    primary_color = theme.filter(key='primaryColor').first().value if theme.filter(key='primaryColor').exists() else '#5D3A00'
    secondary_color = theme.filter(key='secondaryColor').first().value if theme.filter(key='secondaryColor').exists() else '#D2B48C'
    background_color = theme.filter(key='backgroundColor').first().value if theme.filter(key='backgroundColor').exists() else '#FAF3E0'
    nav_color = theme.filter(key='navColor').first().value if theme.filter(key='navColor').exists() else '#2E1C12'

    context = {
        'home': {'hero_text': home_hero_text, 'intro_text': home_intro_text},
        'about': {'text': about_text},
        'products': products_list,
        'gallery_images': gallery_images,
        'contact': {
            'email': contact_email,
            'phone': contact_phone,
            'address': contact_address,
        },
        'home_bg_url': home_bg_url,
        'contact_map_url': contact_map_url,
        'theme': {
            'primary_color': primary_color,
            'secondary_color': secondary_color,
            'background_color': background_color,
            'nav_color': nav_color,
        }
    }

    return render(request, 'index.html', context)


def admin_html(request):
    """Optional route to render admin.html directly."""
    return render(request, 'admin.html')


@csrf_exempt
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def save_content(request):
    """API endpoint to save content via POST."""
    serializer = SiteContentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@login_required
def render_page(request, section_name):
    """Dynamic route to render a section page (if needed)."""
    content = SiteContent.objects.filter(section=section_name)
    return render(request, f'{section_name}.html', {'content': content})
