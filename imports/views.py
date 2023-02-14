from django.shortcuts import render, get_object_or_404
from .models import Config
from django.http import HttpResponse, Http404, JsonResponse

def config_list(request):
    configs = Config.objects.all()
    data = {'configs': list(configs.values('id', 'url'))}
    return JsonResponse(data)

def config_detail(request, pk):
    config = get_object_or_404(Config, pk=pk)
    data = {'config': {'id': config.id, 'url': config.url}}
    return JsonResponse(data)

def config_create(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        config = Config(url=url)
        config.save()
        return JsonResponse({'config': {'id': config.id, 'url': config.url}})
    return HttpResponse(status=405)

def config_update(request, pk):
    config = get_object_or_404(Config, pk=pk)
    if request.method == 'PUT':
        url = request.PUT.get('url')
        config.url = url
        config.save()
        return JsonResponse({'config': {'id': config.id, 'url': config.url}})
    return HttpResponse(status=405)

def config_delete(request, pk):
    config = get_object_or_404(Config, pk=pk)
    if request.method == 'DELETE':
        config.delete()
        return HttpResponse(status=204)
    return HttpResponse(status=405)