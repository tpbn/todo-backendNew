from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model

SECRET_KEY = "kaySpidermanOKayBatman"

@csrf_exempt
def create_superuser(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST allowed'}, status=405)

    token = request.headers.get('X-Secret-Token')
    if token != SECRET_KEY:
        return JsonResponse({'error': 'Invalid secret token'}, status=401)

    User = get_user_model()

    if User.objects.filter(is_superuser=True).exists():
        return JsonResponse({'message': 'Superuser already exists'}, status=403)

    User.objects.create_superuser(username='admin', password='admin123', email='admin@example.com')
    return JsonResponse({'message': 'Superuser created successfully!'})
