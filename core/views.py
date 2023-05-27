from django.shortcuts import render
from faker import Faker
fake = Faker()

# from core.models import Question, Network

# Create your views here.
def about_us(request):
    active_image = {'link' : 'https://officebanao.com/wp-content/uploads/2022/10/Modern-office-design-5-1024x576.jpg'}
    other_images = [
        {'link' : 'https://www.jennor.co.uk/wp-content/uploads/2021/10/14-Peel-3Z7A3757-1024x683.jpg'}
        , {'link' : 'https://officeprinciples.com/assets/uploads/images/Page-Banners/_1200x630_crop_center-center_82_none/Office-Interior-Design.jpg?mtime=1655274853'}
    ]
    return render(request, 'core/about_us.html', {'active_image' : active_image,'images' : other_images})

def contacts(request):
    working_hours = {'open': '9 am', 'close': '18 pm'}
    networks = None
    # Network.objects.all()
    return render(request, 'core/contacts.html', {'working_hours': working_hours, 'networks': networks, 'phone': fake.phone_number(), 'email' : fake.email()})

def questions(request):
    common_questions = None
    # Question.objects.all()
    return render(request, 'core/questions.html', {'questions': common_questions})