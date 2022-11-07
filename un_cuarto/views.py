import json
import smtplib
from crispy_forms.templatetags.crispy_forms_filters import as_crispy_field
from django.http import (
    HttpResponseRedirect, HttpResponseNotFound, HttpResponseForbidden,
    HttpResponse, JsonResponse, HttpResponse, Http404
)
from django.urls import reverse
# from crispy_forms.utils import render_crispy_form
from django.core.mail import send_mail, BadHeaderError
from django.views.generic import (
    View, ListView, DetailView, CreateView, UpdateView,
    DeleteView, RedirectView, FormView, TemplateView
)
from django.conf import settings
from django.views.decorators import csrf, http
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import (
    MetaElements, HeroSettings,
    ServicesSection, Services,
    PortafolioSection, Portafolio,
    AboutUsSection, ShowReel,
    Team, SocialLinks, Contact, Comment, Galeria,TeamSection, GaleriaSection
)
from .forms import ContactForm, CommentForm
from csp.decorators import csp_exempt

decorators = [
    csrf.csrf_protect,
    http.require_http_methods(["POST","GET", "HEAD"])]
@method_decorator(decorators, name='dispatch')
class StartView(TemplateView):
    template_name = "base.html"

    def post(self, request):
        form = ContactForm(request.POST or None)
        if form.is_valid():
            print(form)
            try:
                nombre = form.cleaned_data['nombre']
                asunto = form.cleaned_data['asunto']
                email = form.cleaned_data['email']
                contenido = form.cleaned_data['contenido']
            except BadHeaderError:
                return messages.warning('Cabecera HTTP invalida encontrada.')
            else:
                body = '{}\n\n{}\n\n{}\n\n{}'.format(nombre, asunto, email, contenido)
                server = smtplib.SMTP('smtp.gmail.com','587')
                server.starttls()
                server.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
                server.sendmail('agenciauncuarto@gmail.com', 'alencina407@gmail.com', body)
                server.quit()
                messages.success(request, 'Mensaje eniado')
                return HttpResponseRedirect("/")
        else:
            return render(request, self.template_name, {'contactform': form})

    def get_context_data(self, **kwargs):
        context = super(StartView, self).get_context_data(**kwargs)
        context["meta_settings"] =  MetaElements.objects.all()
        context["hero_setting"] = HeroSettings.objects.all()
        context["services_setting"] = ServicesSection.objects.all()
        context["services"] = Services.objects.all()
        context["nos_setting"] = AboutUsSection.objects.all()
        context["comentarios"] = Comment.objects.all()
        context["team_setting"] = TeamSection.objects.all()
        context["members"] = Team.objects.all()
        context["social_links"] = SocialLinks.objects.all()
        context["contact"] = Contact.objects.all()
        context["port_setting"] =PortafolioSection.objects.all()
        context["cartera"] = Portafolio.objects.all()
        context["contactform"] = ContactForm()
        context["showreel"] = ShowReel.objects.all()
        context["galery_setting"] = GaleriaSection.objects.all()
        context["galery"] = Galeria.objects.all()
        return context


# @csrf.csrf_protect
# @http.require_http_methods(["POST"])
# def check_captcha(request):
#     print(request.is_secure())
#     if request.method == "POST":
#         body = json.loads(request.body)
#         response = requests.post(
#             'https://www.google.com/recaptcha/api/siteverify', {
#             'secret': settings.RECAPTCHA_PRIVATE_KEY,
#             'response': body,
#             'remoteip': request.get_host()})

#         if response.json()['success']:
#             return JsonResponse({'response': ""})

@csrf.csrf_protect
@http.require_http_methods(["POST","GET", "HEAD"])
def comment_view(request):
    if request.method == 'GET':
        return render(request, 'un_cuarto/pages/comment_form.html', {'form': CommentForm()})
    elif request.method == 'POST':
        form = CommentForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'gracias')
            return redirect('/')
        return render(request, 'un_cuarto/pages/comment_form.html', {"form": form})


decorators = [
    http.require_http_methods(["GET", "HEAD"])]
@method_decorator(decorators, name='dispatch')
class PortafolioDetailView(DetailView):
    model = Portafolio
    template_name = "un_cuarto/pages/detail.html"