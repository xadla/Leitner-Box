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

class AddWordView(View):

    class_form = AddWordForm
    template_name = "boxes/word.html"

    def get(self, request, box_id):
        form = self.class_form()
        return render(request, self.template_name, {"form": form})

    def post(self, request, box_id):
        form = self.class_form(request.POST)

        if form.is_valid():

            cd = form.cleaned_data
            try:
                box = BoxWord.objects.get(pk=box_id)

                word = Word.objects.create(
                    name=cd["name"],
                    example=cd["example"],
                    definition=cd["definition"],
                    box=box,
                )
                word.save()

                messages.success(request, "New word is created")

                return redirect("boxes:box_detail", box_id)

            except BoxWord.DoesNotExist:
                messages.error(request, "This box is not exist!")
                return redirect("pages:home")


        return render(request, self.template_name, {"form": form})


class BoxWordView(View):

    template_name = "boxes/box_word.html"

    def get(self, request, id):

        try:
            box = BoxWord.objects.get(pk=id)
            words = box.words.all()

            return render(request, self.template_name, {"words": words, "id": id})


        except Word.DoesNotExist:
            messages.error(request, "This box is not exist")
            return redirect("pages:home")


class AddBoxView(View):

    template_name = "boxes/box.html"

    def get(self, request):

        boxLevelOne = BoxLevelOne.objects.first()

        if boxLevelOne.size > 0:
            messages.error(request, "You can't create new Box word")
            return redirect("pages:home")
        
        newBox = BoxWord.objects.create(box_level_one=boxLevelOne)
        newBox.save()
        boxLevelOne.size += 1
        boxLevelOne.save()

        messages.success(request, "New Box is created")

        return redirect("boxes:box_detail", id=newBox.id)


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


class WordEditView(View):

    class_form = AddWordForm
    template_name = "boxes/edit_word.html"

    def get(self, request, id, red):

        try:
            word = Word.objects.get(pk=id)

            form = self.class_form(initial={
                "name": word.name,
                "example": word.example,
                "definition": word.definition,
            })

            return render(request, self.template_name, {"form": form})

        except Word.DoesNotExist:
            messages.error(request, "Word does not found")
            return redirect("pages:home")

    def post(self, request, id, red):

        form = self.class_form(request.POST)
        if form.is_valid():
            try:
                word = Word.objects.get(pk=id)
                word.name = form.cleaned_data["name"]
                word.example = form.cleaned_data["example"]

                word.save()
                messages.success(request, "Word is edited successfully")

                return redirect("boxes:boxes_view", id=red)

            except Word.DoesNotExist:

                messages.error(request, "Word Does not exist")
                return redirect("pages:home")


class WordDeleteView(View):

    def get(self, request, id):

        try:
            word = Word.objects.get(pk=id)
            word.delete()

            messages.success(request, "Word is deleted")

            return redirect(request.META.get('HTTP_REFERER', 'pages:home'))
        
        except Word.DoesNotExist:

            messages.error(request, "Word does not exist")
            return redirect("pages:home")


class ShiftBoxes(View):
    
    template_name = "boxes/shift.html"

    def get(self, request):

        box1 = BoxLevelOne.objects.first().box_words_one.last()
        box2 = BoxLevelTwo.objects.first().box_words_two.last()
        box3 = BoxLevelThree.objects.first().box_words_three.last()
        box4 = BoxLevelFour.objects.first().box_words_four.last()
        box5 = BoxLevelFive.objects.first().box_words_five.last()
        
        words = []

        if box1:
            words.append(list(box1.words.all()))
        
        if box2:
            words.append(list(box2.words.all()))

        if box3:
            words.append(list(box3.words.all()))
        
        if box4:
            words.append(list(box4.words.all()))
        
        if box5:
            words.append(list(box5.words.all()))

        return render(request, self.template_name, {"words": words})