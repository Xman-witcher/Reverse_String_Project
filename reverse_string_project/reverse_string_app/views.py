from django.http import JsonResponse
from django.http import HttpResponse

def reverse_string(request):
    if request.method == 'POST':
        input_str = request.POST.get('string')
        if not input_str:
            input_str = request.body.decode('utf-8')
        
        if input_str is None:
            return HttpResponse('Input string not found in request')
        output_str = input_str[::-1]
        return HttpResponse(output_str)
    else:
        return HttpResponse('Invalid request method')
    


def reverse_string_json(request):
    if request.method == 'POST':
        input_str = request.POST.get('string')
        if not input_str:
            input_str = request.body.decode('utf-8')            
      
        if input_str is None:
            return JsonResponse({'error': 'Input string not found in request'})
        output_str = input_str[::-1]
        return JsonResponse({'reversed_string': output_str})
    else:
        return JsonResponse({'error': 'Invalid request method'})