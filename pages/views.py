from django.shortcuts import render
from django.views import View

from boxes.models import (
    BoxLevelOne,
    BoxLevelTwo,
    BoxLevelThree,
    BoxLevelFour,
    BoxLevelFive
)

class HomeView(View):

    def get(self, request):
        box1 = BoxLevelOne.objects.first()
        number1 = box1.box_words_one.count()

        box2 = BoxLevelTwo.objects.first()
        number2 = box2.box_words_two.count()

        box3 = BoxLevelThree.objects.first()
        number3 = box3.box_words_three.count()

        box4 = BoxLevelFour.objects.first()
        number4 = box4.box_words_four.count()

        box5 = BoxLevelFive.objects.first()
        number5 = box5.box_words_five.count()

        return render(
            request,
            "pages/home.html",
            {
                "number1": number1,
                "number2": number2,
                "number3": number3,
                "number4": number4,
                "number5": number5
            },
            )