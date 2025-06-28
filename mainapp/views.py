from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def landing(request):
    return render(request, 'landing.html')

def thanks(request):
    return render(request, 'thanks.html')

@user_passes_test(lambda u: u.is_staff)
def orders_list(request):
    # Тестовые данные
    orders = [
        {
            'id': 1,
            'client_name': 'Иван Иванов',
            'date': '2025-06-22 14:00',
            'services': ['Стрижка', 'Бритьё'],
            'master': 'Пётр Петров',
            'status': 'new'
        },
        {
            'id': 2,
            'client_name': 'Алексей Смирнов',
            'date': '2025-06-23 16:00',
            'services': ['Стрижка'],
            'master': 'Сергей Сергеев',
            'status': 'confirmed'
        }
    ]
    return render(request, 'orders_list.html', {'orders': orders})

@user_passes_test(lambda u: u.is_staff)
def order_detail(request, order_id):
    # Тестовые данные
    order = {
        'id': order_id,
        'client_name': 'Иван Иванов',
        'client_phone': '+7 (123) 456-78-90',
        'client_email': 'ivan@example.com',
        'date': '2025-06-22 14:00',
        'services': ['Стрижка', 'Бритьё'],
        'master': 'Пётр Петров',
        'status': 'new',
        'comment': 'Хочу классическую стрижку и бритьё опасной бритвой'
    }
    return render(request, 'order_detail.html', {'order': order})