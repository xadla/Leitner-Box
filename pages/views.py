from django.shortcuts import render
from django.views import View

from boxes.models import BoxLevelOne, BoxLevelTwo, BoxLevelFive

class HomeView(View):

    def get(self, request):
        boxLevelOne = BoxLevelOne.objects.first()
        box1 = boxLevelOne.box_words_one.first()
        words1 = box1.words.all()

        boxLevelTwo = BoxLevelTwo.objects.first()
        box2 = boxLevelTwo.box_words_two.first()
        words2 = box2.words.all()

        return render(request, "pages/home.html", {"words1": words1, "words2": words2})