from django.contrib import admin

from .models import (
    BoxLevelOne,
    BoxLevelTwo,
    BoxLevelThree,
    BoxLevelFour,
    BoxLevelFive,
    BoxWord,
    Word,
)


admin.site.register(BoxLevelOne)
admin.site.register(BoxLevelTwo)
admin.site.register(BoxLevelThree)
admin.site.register(BoxLevelFour)
admin.site.register(BoxLevelFive)
admin.site.register(Word)
admin.site.register(BoxWord)