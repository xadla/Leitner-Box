from django.shortcuts import render, redirect
from django.views import View

from .forms import AddWordForm
from .models import (
    Word,
    BoxWord,
    BoxLevelOne,
    BoxLevelTwo,
    BoxLevelThree,
    BoxLevelFour,
    BoxLevelFive,
)

class AddWord(View):

    class_form = AddWordForm
    template_name = "boxes/word.html"

    def add_item(self, name, explain):
        newWord = Word(name=name, explain=explain)
        
        boxWords = BoxWord.objects.filter(size__lt=10).first()
        
        if boxWords:
            newWord.box = boxWords  
            boxWords.size += 1
            boxWords.save()
        else:
            boxWords = BoxWord.objects.create()
            
            level_one = BoxLevelOne.objects.first()
            level_two = BoxLevelTwo.objects.first()
            level_three = BoxLevelThree.objects.first()
            level_four = BoxLevelFour.objects.first()
            level_five = BoxLevelFive.objects.first()

            if level_one and level_one.size < 1:
                boxWords.box_level_one = level_one
                level_one.size += 1
                level_one.save()
            
            elif level_two and level_two.size < 2:
                boxWords.box_level_two = level_two
                level_two.size += 1
                level_two.save()

            elif level_three and level_three.size < 4:
                boxWords.box_level_three = level_three
                level_three.size += 1
                level_three.save()
            
            elif level_four and level_four.size < 8:
                boxWords.box_level_four = level_four
                level_four.size += 1
                level_four.save()
            
            elif level_five and level_five.size < 15:
                boxWords.box_level_five = level_five
                level_five.size += 1
                level_five.save()
            
            boxWords.size += 1
            boxWords.save()
            newWord.box = boxWords

        newWord.save()

    def get(self, request):
        form = self.class_form()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.class_form(request.POST)
        
        if form.is_valid():

            cd = form.cleaned_data
            self.add_item(cd["name"], cd["explain"])

            return redirect("pages:home")

        return render(request, self.template_name, {"form": form})