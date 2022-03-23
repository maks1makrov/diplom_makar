from django.contrib import admin

from classroom.models import Materials, QuestionForKonspect, AnswerForKonspect, TestName, TestQuestion, \
    TestAnswer, TestAnswerResponse, TestResult

admin.site.register(Materials)
admin.site.register(AnswerForKonspect)
admin.site.register(TestName)
admin.site.register(TestAnswerResponse)
admin.site.register(TestResult)


class AnswerAdmin(admin.StackedInline):
    model = AnswerForKonspect
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]


admin.site.register(QuestionForKonspect, QuestionAdmin)


class TestAnswerAdmin(admin.StackedInline):
    model = TestAnswer
    extra = 3


class TestQuestionAdmin(admin.ModelAdmin):
    inlines = [TestAnswerAdmin]
    list_display = ['test', 'text']


admin.site.register(TestQuestion, TestQuestionAdmin)