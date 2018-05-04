from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Contact
from .models import Post
import json

# Create your views here.

class IndexView(TemplateView):
	template_name = "index.html"
    
	def get_context_data(self, **kwargs):
		posts = Post.objects.order_by('-date')[:3]
		for post in posts:
			print(post.title)

		context = super(IndexView, self).get_context_data(**kwargs)
		context.update({
			'posts': posts
		})

		return context


@method_decorator(csrf_exempt, name='dispatch')
class ContactView(CreateView):
	http_method_names = ['post']
	model = Contact
	fields = '__all__'

	def get_form_kwargs(self):
		"""
		Returns the keyword arguments for instantiating the form.
		"""
		kwargs = {
			'initial': self.get_initial(),
			'prefix': self.get_prefix(),
		}
		if self.request.method in ('POST', 'PUT'):
			json_data = json.loads(self.request.body.decode("utf-8"))
			kwargs.update({
				'data': json_data
			})

		return kwargs

	def form_invalid(self, form):
		return JsonResponse({'errors': form.errors, 'sent': False})

	def form_valid(self, form):
		# text_content = render_to_string('emails/contact.txt', {'data': form.data})
		# html_content = render_to_string('emails/contact.html', {'data': form.data})
		# email = EmailMultiAlternatives('Subject', text_content)
		# email.attach_alternative(html_content, "text/html")
		# email.to = ['info@dominio.com']
		# email.send()
		form.save()
		return JsonResponse({'text': 'Consulta enviada', 'sent': True})
