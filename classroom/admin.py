from django.contrib import admin

from classroom.models import Materials, KonspectOne, QuestionForKonspect, AnswerForKonspect

admin.site.register(Materials)
admin.site.register(KonspectOne)

class AnswerAdmin(admin.StackedInline):
    model = AnswerForKonspect
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]

admin.site.register(QuestionForKonspect, QuestionAdmin)
