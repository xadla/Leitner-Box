from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .forms import AddWordForm
from .models import (
    Word,
    BoxWord,
    BoxLevelOne,
    BoxLevelTwo,
    BoxLevelThree,
    BoxLevelFour,
    BoxLevelFive,
    Temp,
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

            for word in words:
                word.example = word.example.replace("\n", "<br>")
                word.definition = word.definition.replace("\n", "<br>")

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

        tempBox = Temp.objects.first()
        tempWords = tempBox.words.all()

        for word in tempWords:

            word.box_temp = None
            word.box = newBox
            word.save()

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
        if words:
            for word in words:
                for w in word:
                    w.example = w.example.replace("\n", "<br>")
                    w.definition = w.definition.replace("\n", "<br>")

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
                word.definition = form.cleaned_data["definition"]

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

        box1 = BoxLevelOne.objects.first().box_words_one.first()
        box2 = BoxLevelTwo.objects.first().box_words_two.first()
        box3 = BoxLevelThree.objects.first().box_words_three.first()
        box4 = BoxLevelFour.objects.first().box_words_four.first()
        box5 = BoxLevelFive.objects.first().box_words_five.first()

        words1 = []
        box_id1 = 0

        words2 = []
        box_id2 = 0

        words3 = []
        box_id3 = 0

        words4 = []
        box_id4 = 0

        words5 = []
        box_id5 = 0

        if box1:
            words1 = box1.words.all()
            box_id1 = box1.id

        if box2:
            words2 = box2.words.all()
            box_id2 = box2.id

        if box3:
            words3 = box3.words.all()
            box_id3 = box3.id
        
        if box4:
            words4 = box4.words.all()
            box_id4 = box4.id

        if box5:
            words5 = box5.words.all()
            box_id5 = box5.id

        for word in words1:
            word.example = word.example.replace("\n", "<br>")
            word.definition = word.definition.replace("\n", "<br>")

        for word in words2:
            word.example = word.example.replace("\n", "<br>")
            word.definition = word.definition.replace("\n", "<br>")

        for word in words3:
            word.example = word.example.replace("\n", "<br>")
            word.definition = word.definition.replace("\n", "<br>")

        for word in words4:
            word.example = word.example.replace("\n", "<br>")
            word.definition = word.definition.replace("\n", "<br>")
        
        for word in words5:
            word.example = word.example.replace("\n", "<br>")
            word.definition = word.definition.replace("\n", "<br>")

        return render(request, self.template_name, {
            "words1": words1, "id1": box_id1,
            "words2": words2, "id2": box_id2,
            "words3": words3, "id3": box_id3,
            "words4": words4, "id4": box_id4,
            "words5": words5, "id5": box_id5,
            }
        )


class UnknownWordView(View):

    def get(self, request, id_word):

        try:

            temp = Temp.objects.first()

            word = Word.objects.get(pk=id_word)
            word.box = None
            word.box_temp = temp

            word.save()

            return redirect(request.META.get('HTTP_REFERER', 'pages:home'))

        except Word.DoesNotExist:

            messages.error(request, "This word is not exist")
            return redirect("pages:home")


class ShiftBoxView(View):

    def get(self, request, id_box):

        try:
            box = BoxWord.objects.get(pk=id_box)

            if box.box_level_one:
                
                newBox = BoxLevelTwo.objects.first()
                if newBox.size < newBox.capacity:
                    newBox.size += 1
                    newBox.save()
                    box.box_level_two = newBox
                    box.box_level_one.size -= 1
                    box.box_level_one.save()
                    box.box_level_one = None
                    box.save()

                else:
                    messages.error(request, "Next Level is full!")
                    return redirect(request.META.get('HTTP_REFERER', 'pages:home'))
            
            elif box.box_level_two:

                newBox = BoxLevelThree.objects.first()
                if newBox.size < newBox.capacity:
                    newBox.size += 1
                    newBox.save()
                    box.box_level_three = newBox
                    box.box_level_two.size -= 1
                    box.box_level_two.save()
                    box.box_level_two = None
                    box.save()

                else:
                    messages.error(request, "Next Level is full!")
                    return redirect(request.META.get('HTTP_REFERER', 'pages:home'))

            elif box.box_level_three:

                newBox = BoxLevelFour.objects.first()
                if newBox.size < newBox.capacity:
                    newBox.size += 1
                    newBox.save()
                    box.box_level_four = newBox
                    box.box_level_three.size -= 1
                    box.box_level_three.save()
                    box.box_level_three = None
                    box.save()

                else:
                    messages.error(request, "Next Level is full!")
                    return redirect(request.META.get('HTTP_REFERER', 'pages:home'))
            
            elif box.box_level_four:

                newBox = BoxLevelFive.objects.first()
                if newBox.size < newBox.capacity:
                    newBox.size += 1
                    newBox.save()
                    box.box_level_five = newBox
                    box.box_level_four.size -= 1
                    box.box_level_four.save()
                    box.box_level_four = None
                    box.save()

                else:
                    messages.error(request, "Next Level is full!")
                    return redirect(request.META.get('HTTP_REFERER', 'pages:home'))

            else:
                box.box_level_five.size -= 1
                box.box_level_five.save()
                box.delete()

            return redirect(request.META.get('HTTP_REFERER', 'pages:home'))

        except BoxWord.DoesNotExist:
            messages.error(request, "This Box is not exist")
            return redirect("pages:home")