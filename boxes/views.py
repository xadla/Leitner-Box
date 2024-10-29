from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .forms import AddWordForm, AddBoxForm
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
            newWord.save()
            messages.success(request, "New Word is created")
            return True
        
        else:
            messages.error(request, "There is no Box for add word!")
            return False
        

    def get(self, request):
        form = self.class_form()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.class_form(request.POST)
        
        if form.is_valid():

            cd = form.cleaned_data
            if self.add_item(cd["name"], cd["explain"]):
                return redirect("pages:home")
            else:
                return render(request, self.template_name, {"form": form})

        return render(request, self.template_name, {"form": form})


class AddBox(View):

    class_form = AddBoxForm
    template_name = "boxes/box.html"

    def add_item(self, request, capacity):

        if BoxLevelOne.objects.first().size == 0:
            newBox = BoxWord.objects.create(capacity=capacity, size=0)
            newBox.box_level_one = BoxLevelOne.objects.first()
            newBox.save()
            messages.success(request, "New Box is created")

        else:
            messages.error(request, "first answer the first box")

    def get(self, request):
        form = self.class_form()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.class_form(request.POST)

        if form.is_valid():
            
            cap = form.cleaned_data["capacity"]
            if cap > 0:
                self.add_item(request, cap)
                return redirect("pages:home")

            else:
                return render(request, self.template_name, {"form": form})

class BoxesView(View):

    template_name = "boxes/boxes.html"

    def get(self, request, id):
        
        box = BoxLevelOne.objects.first()
        boxWords = box.box_words_one.all()
        words = []
        if boxWords:
            for bWord in boxWords:
                words.append(list(bWord.words.all()))

        if id == 2:
            box = BoxLevelTwo.objects.first()
            boxWords = box.box_words_two.all()
            if boxWords:
                words = []
                for bWord in boxWords:
                    words.append(list(bWord.words.all()))

            else:
                words = None
        
        elif id == 3:
            box = BoxLevelThree.objects.first()
            boxWords = box.box_words_three.all()
            if boxWords:
                words = []
                for bWord in boxWords:
                    words.append(list(bWord.words.all()))
            
            else:
                words = None

        elif id == 4:
            box = BoxLevelFour.objects.first()
            boxWords = box.box_words_four.all()
            if boxWords:
                words = []
                for bWord in boxWords:
                    words.append(list(bWord.words.all()))
            
            else:
                words = None
        
        elif id == 5:
            box = BoxLevelFive.objects.first()
            boxWords = box.box_words_five.all()
            if boxWords:
                words = []
                for bWord in boxWords:
                    words.append(list(bWord.words.all()))

            else:
                words = None

        return render(
            request,
            self.template_name,
            {"box": boxWords, "words": words, "id": id},
            )