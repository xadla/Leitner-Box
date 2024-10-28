from django.db import models


class AbstractBox(models.Model):

    capacity = models.IntegerField()

    class Meta:
        abstract = True

class BoxLevelOne(AbstractBox):

    capacity = models.IntegerField(default=1)
    size = models.IntegerField(default=0)

    def __str__(self):
        return "Box Level 1"

    class Meta:
        verbose_name = "Box Level 1"
        verbose_name_plural = "Boxes Level 1"


class BoxLevelTwo(AbstractBox):

    capacity = models.IntegerField(default=2)
    size = models.IntegerField(default=0)

    def __str__(self):
        return "Box Level 2"

    class Meta:
        verbose_name = "Box Level 2"
        verbose_name_plural = "Boxes Level 2"


class BoxLevelThree(AbstractBox):

    capacity = models.IntegerField(default=4)
    size = models.IntegerField(default=0)

    def __str__(self):
        return "Box Level 3"

    class Meta:
        verbose_name = "Box Level 3"
        verbose_name_plural = "Boxes Level 3"


class BoxLevelFour(AbstractBox):

    capacity = models.IntegerField(default=8)
    size = models.IntegerField(default=0)

    def __str__(self):
        return "Box Level 4"

    class Meta:
        verbose_name = "Box Level 4"
        verbose_name_plural = "Boxes Level 4"


class BoxLevelFive(AbstractBox):

    capacity = models.IntegerField(default=15)
    size = models.IntegerField(default=0)

    def __str__(self):
        return "Box Level 5"

    class Meta:
        verbose_name = "Box Level 5"
        verbose_name_plural = "Boxes Level 5"


class BoxWord(models.Model):

    capacity = models.IntegerField(default=10)
    size = models.IntegerField(default=0)

    box_level_one = models.ForeignKey(
        BoxLevelOne,
        related_name="box_words_one",
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    box_level_two = models.ForeignKey(
        BoxLevelTwo,
        related_name="box_words_two",
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    box_level_three = models.ForeignKey(
        BoxLevelThree,
        related_name="box_words_three",
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    box_level_four = models.ForeignKey(
        BoxLevelFour,
        related_name="box_words_four",
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    box_level_five = models.ForeignKey(
        BoxLevelFive,
        related_name="box_words_five",
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Box Word"
        verbose_name_plural = "Box Words"


class Word(models.Model):

    name = models.CharField(max_length=200, unique=True)
    explain = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    box = models.ForeignKey(
        BoxWord,
        related_name="words",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]