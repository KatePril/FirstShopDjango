from django.shortcuts import render
from faker import Faker
fake = Faker()

# Create your views here.
def frontpage(request):
    articles = [
        {'id': 1, 'title': 'First article', 'content': 'This is the first article'}
        , {'id': 2, 'title': 'Second article', 'content': 'This is the second article'}
        , {'id': 3, 'title': 'Third article', 'content': 'This is the third article'}
        , {'id': 4, 'title': 'Fourth article', 'content': 'This is the fourth article'}
        , {'id': 5, 'title': 'Fifth article', 'content': 'This is the fifth article'}
        , {'id': 6, 'title': 'Sixth article', 'content': 'This is the sixth article'}
    ]
    return render(request, 'core/frontpage.html', {'articles': articles})

def about_us(request):
    active_image = {'link' : 'https://officebanao.com/wp-content/uploads/2022/10/Modern-office-design-5-1024x576.jpg'}
    other_images = [
        {'link' : 'https://www.jennor.co.uk/wp-content/uploads/2021/10/14-Peel-3Z7A3757-1024x683.jpg'}
        , {'link' : 'https://officeprinciples.com/assets/uploads/images/Page-Banners/_1200x630_crop_center-center_82_none/Office-Interior-Design.jpg?mtime=1655274853'}
    ]
    return render(request, 'core/about_us.html', {'active_image' : active_image,'images' : other_images})

def contacts(request):
    working_hours = {'open': '9 am', 'close': '18 pm'}
    networks = [
        {'name': 'facebook'}
        , {'name': 'instagram'}
        , {'name': 'twitter'}
        , {'name': 'telegram'}
        , {'name': 'viber'}
        , {'name': 'whatsapp'}
    ]
    return render(request, 'core/contacts.html', {'working_hours': working_hours, 'networks': networks, 'phone': fake.phone_number(), 'email' : fake.email()})

def questions(request):
    common_questions = [
        {'id': 'One', 'question': ' What services does your IT company provide?', 'answer': 'Our IT company provides a wide range of services, including software development, network infrastructure setup, cloud computing solutions, cybersecurity services, IT consulting, and data analytics.'}
        , {'id': 'Two', 'question': 'How experienced is your team?', 'answer': 'Our team consists of highly skilled professionals with extensive experience in their respective fields. We have a diverse team of software engineers, data scientists, cybersecurity experts, and IT consultants who bring a wealth of knowledge and expertise to every project.'}
        , {'id': 'Three', 'question': 'Can you handle both small-scale and large-scale projects?', 'answer': "Absolutely! We have experience working on projects of various sizes and complexities. Whether it's a small startup or a large enterprise, we have the capabilities and resources to cater to the specific needs of any organization."}
        , {'id': 'Four', 'question': "How do you ensure data security and privacy?", 'answer': "Data security and privacy are of utmost importance to us. We implement robust security measures, including encryption protocols, firewalls, access controls, and regular security audits to safeguard sensitive information. We strictly adhere to industry best practices and compliance regulations to protect our clients' data."}
        , {'id': 'Five', 'question': "What is your approach to project management?", 'answer': "We follow a systematic and collaborative project management approach. We begin by thoroughly understanding the client's requirements, creating a detailed project plan, setting milestones, and assigning dedicated project managers to ensure smooth execution. We maintain transparent communication throughout the project, providing regular updates and addressing any concerns promptly."}
        , {'id': 'Six', 'question': "Do you offer ongoing technical support?", 'answer': "Yes, we offer comprehensive technical support to our clients. We understand that technology needs continuous maintenance and support, so we provide post-implementation support, regular maintenance, and troubleshooting services to ensure the smooth functioning of our solutions. Our support team is readily available to assist with any technical issues or queries."}
        , {'id': 'Seven', 'question': "Can you integrate your solutions with our existing systems?", 'answer': "Absolutely! We have expertise in integrating our solutions with existing systems. Our team will carefully assess your current infrastructure and work towards seamless integration to maximize efficiency and minimize disruption."}
        , {'id': 'Eight', 'question': "How do you stay updated with the latest technologies?", 'answer': "We prioritize staying at the forefront of technological advancements. Our team actively participates in industry conferences, engages in continuous learning, and conducts research to stay updated with emerging technologies. This allows us to provide innovative and up-to-date solutions to our clients."}
        , {'id': 'Nine', 'question': "What industries have you worked with?", 'answer': "We have worked with clients from a diverse range of industries, including healthcare, finance, e-commerce, manufacturing, education, and more. Our experience spans across various sectors, enabling us to understand industry-specific requirements and deliver tailored solutions."}
        , {'id': 'Ten', 'question': "Can you provide references from your previous clients?", 'answer': "Yes, we can provide references from satisfied clients who have availed our services. We are proud of the relationships we have built and the successful projects we have delivered. We will be happy to share references upon request."}        
    ]
    return render(request, 'core/questions.html', {'questions': common_questions})