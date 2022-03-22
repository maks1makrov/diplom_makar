from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView

from classroom.forms import KonspectOneForm
from classroom.models import Materials, KonspectOne, QuestionForKonspect, AnswerForKonspect


# @method_decorator(login_required, name='dispatch')
class ShowAll(View):

    def get(self, request):
        if request.user.is_authenticated:
            response = {}
            response['materials'] = Materials.objects.all()
            check_list = []
            for material in response['materials']:
                answer_questions = AnswerForKonspect.objects.filter(user=request.user, question__material_id=material.id)
                check_list.append(answer_questions)
            if all(check_list):
                response['all'] = True
            response['all'] = False
            return render(request, "show_all.html", response)
        else:
            return redirect("login")


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'log_in.html', {"form": form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('check')
        messages.error(request, message="login or password is not correct")
        return redirect('login')

@method_decorator(login_required, name='dispatch')
class MaterialView(View):

    def get(self, request, material_id):
        material = Materials.objects.get(id=material_id)
        questions = QuestionForKonspect.objects.filter(material_id=material_id)
        try:
            Answer_questions = AnswerForKonspect.objects.filter(user=request.user, question__material_id=material_id)
        except:
            Answer_questions = False
        return render(request, 'show_material.html', {"material": material, 'questions': questions, "Answer_questions": Answer_questions})


@method_decorator(login_required, name='dispatch')
class CheckView(View):

    def get(self, request):
        return render(request, 'check.html')

    def post(self, request):
        name = request.POST.get('name')
        if name in ('учение', 'идея'):
            return redirect('show_all')
        messages.error(request, message="стыдно! неуч! пробуй еще!")
        return redirect('check')

# @method_decorator(login_required, name='dispatch')
# class KonspectView(CreateView):
#     template_name = 'create_konspect.html'
#     form_class = KonspectOneForm
#     success_url = reverse_lazy('show_konspect')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['konspect'] = KonspectOne.objects.get(user=self.request)
#         return context

# @method_decorator(login_required, name='dispatch')
# class KonspectView(View):
#
#     def get(self, request):
#         try:
#             konspect = KonspectOne.objects.get(user=request.user)
#         except:
#             konspect = None
#         if konspect:
#             return redirect('show_konspect')
#         form = KonspectOneForm()
#         return render(request, 'create_konspect.html', {"form": form})
#
#     def post(self, request):
#         form = KonspectOneForm(data=request.POST)
#         if form.is_valid():
#             nf = form.save(commit=False)
#             nf.user_id = request.user.id
#             nf.save()
#             return redirect('show_konspect')
#         messages.error(request, message="некорректный ввод")
#         return render(request, 'create_konspect.html', {"form": form})


@method_decorator(login_required, name='dispatch')
class ShowKonspectView(View):

    def get(self, request, material_id):
        Answer_questions = AnswerForKonspect.objects.filter(user=request.user, question__material_id=material_id)
        return render(request, 'show_konspect.html', {"Answer_questions": Answer_questions})


class QuestionsKonspectView(View):

    def post(self, request, material_id):
        data = request.POST.dict()
        data.pop('csrfmiddlewaretoken')
        for i in data.items():
            AnswerForKonspect.objects.create(question_id=i[0], answer=i[1], user=request.user)
        Answer_questions = AnswerForKonspect.objects.filter(user=request.user, question__material_id=material_id)
        return render(request, 'show_konspect.html', {"Answer_questions": Answer_questions})