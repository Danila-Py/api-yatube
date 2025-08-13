from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название группы',
        help_text='Введите название тематической группы',
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='Номер группы',
        help_text='Укажите порядковый номер группы',
    )
    description = models.TextField(
        max_length=200,
        verbose_name='Описание группы',
        help_text='Добавьте текст описания группы',
    )

    class Meta:
        ordering = ('-title',)
        verbose_name = 'Группа статей'
        verbose_name_plural = 'Группы статей'

    def __str__(self) -> str:
        return self.title[:10]


class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор статьи',
        help_text='Укажите автора статьи',
    )
    text = models.TextField(
        verbose_name='Текст статьи',
        help_text='Введите текст статьи',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
        help_text='Укажите дату публикации',
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
        verbose_name='Картинка статьи',
        help_text='Добавьте картинку статьи',
    )
    group = models.ForeignKey(
        Group,
        related_name='posts',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Группа статей',
        help_text='Выберите тематическую группу '
                  'в выпадающем списке по желанию',
    )

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self) -> str:
        return self.title[:10]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Имя автора',
        help_text='Укажите автора',
    )
    text = models.TextField(
        max_length=300,
        verbose_name='Текст комментария',
        help_text='Укажите текст комментария',
    )
    created = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата комментария',
        help_text='Укажите дату комментария',
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Имя поста',
        help_text='Укажите имя поста',
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self) -> str:
        return self.title[:10]