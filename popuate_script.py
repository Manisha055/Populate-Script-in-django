import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Project.settings')

import django
django.setup()

import random
from App.models import Topic,Webpage,AccessRecord
from faker import Faker

fakegen=Faker()
topics=['search','social','Market','game','music']

def add_topics():
	t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
	t.save()
	return t

def populate(N=5):
	for entry in range(N):

		top=add_topics()

		fake_name=fakegen.company()
		fake_url=fakegen.url()
		fake_date=fakegen.date()

		webpg = Webpage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]
		accrec= AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
	print('population script')
	populate(10)
	print("successful")



