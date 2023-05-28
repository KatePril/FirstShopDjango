from django.shortcuts import render
from faker import Faker
fake = Faker()

from core.models import Question, Network

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
    # networks = [
    #     {'name': 'facebook'}
    #     , {'name': 'instagram'}
    #     , {'name': 'twitter'}
    #     , {'name': 'telegram'}
    #     , {'name': 'viber'}
    #     , {'name': 'whatsapp'}
    # ]
    networks = Network.objects.all()
    return render(request, 'core/contacts.html', {'working_hours': working_hours, 'networks': networks, 'phone': fake.phone_number(), 'email' : fake.email()})

def questions(request):
    # common_questions = [
    #     {'id': 'One', 'question': 'How long does it takes to develop a project?', 'answer': 'It depends on the amount of work your project requires to do so as to be finished.'}
    #     , {'id': 'Two', 'question': 'Do you provide long-term support for your project?', 'answer': 'Surely. We provide support to all our projects during their life cycle.'}
    #     , {'id': 'Three', 'question': 'Which is the best way to contact us?', 'answer': "It does not matter. We check your email regulary during the working hours so as to make sure we won't miss any of your emails. Your managers are also avaliable by phone during the working hours. So you may choose way that is the most convinient for you when contacting us."}
    #     , {'id': 'Four', 'question': 'Do you work at the weekends?', 'answer': 'Yes, we work during the weekends.'}
    # ]
    common_questions = Question.objects.all()
    return render(request, 'core/questions.html', {'questions': common_questions})