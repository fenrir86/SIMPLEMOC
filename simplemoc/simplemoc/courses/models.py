from django.db import models
from django.conf import settings

from ..core.mail import send_mail_template
from django.utils import timezone


# Create your models here.


class CourseManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__incotains=query) | \
            models.Q(descripition__icontains=query)
        )


class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    about = models.TextField('Sobre o curso', blank=True)
    start_date = models.DateField('Data de inicio', null=True, blank=True)
    image = models.ImageField(
        upload_to='courses/images',
        verbose_name='Imagem',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField('Criado em ', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em ', auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return 'courses:details', (), {'slug': self.slug}

    def release_lessons(self):
        today = timezone.now().date()
        return self.lessons.filter(release_date__gte=today)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']


class Lesson(models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Descrição', blank=True)
    number = models.IntegerField('Numero (ordem)', blank=True, default=0)
    release_date = models.DateField('Data de liberação', blank=True, null=True)

    course = models.ForeignKey(Course, verbose_name='Curso', related_name='lessons', on_delete=models.CASCADE)

    created_at = models.DateTimeField('Criado em ', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em ', auto_now=True)

    def __str__(self):
        return self.name

    def is_available(self):
        if self.release_date:
            today = timezone.now().date()
            return self.release_date >= today
        return False

    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'
        ordering = ['-number']


class Material(models.Model):
    name = models.CharField('Name', max_length=100)
    embedded = models.TextField('Vídeo embedded', blank=True)
    file = models.FileField(upload_to='lessons/material', blank=True, null=True)

    lesson = models.ForeignKey(Lesson,
                               verbose_name='Aula',
                               related_name='materials',
                               on_delete=models.CASCADE)

    def is_embedded(self):
        return bool(self.embedded)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiais'


class Enrollment(models.Model):
    STATUS_CHOICES = (
        (0, 'Pendente'),
        (1, 'Aprovado'),
        (2, 'Cancelado')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             verbose_name='Usuário',
                             related_name='enrollments',
                             on_delete=models.CASCADE)

    course = models.ForeignKey(Course,
                               verbose_name='Curso',
                               related_name='enrollments',
                               on_delete=models.CASCADE)
    status = models.IntegerField('Situação', choices=STATUS_CHOICES, default=1, blank=True)
    created_at = models.DateTimeField('Criado em ', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em ', auto_now=True)

    def active(self):
        self.status = 1
        self.save()

    def is_approved(self):
        return self.status == 1

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        unique_together = (('user', 'course'),)


class Announcements(models.Model):
    course = models.ForeignKey(Course, verbose_name='Curso',
                               related_name='announcements',
                               on_delete=models.CASCADE)
    title = models.CharField('Titulo', max_length=100)
    content = models.TextField('Conteudo')
    created_at = models.DateTimeField('Criado em ', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em ', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Anúncio'
        verbose_name_plural = 'Anúncios'
        ordering = ['-created_at']


class Comment(models.Model):
    announcements = models.ForeignKey(Announcements, verbose_name='Anúncio',
                                      related_name='comments',
                                      on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', on_delete=models.CASCADE)
    comment = models.TextField('Comentário')

    created_at = models.DateTimeField('Criado em ', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em ', auto_now=True)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
        ordering = ['created_at']


def post_save_announcement(instance, created, **kwargs):
    if created:
        subject = instance.title
        context = {
            'announcement': instance
        }
        template_name = 'courses/announcement_mail.html'
        enrollments = Enrollment.objects.filter(
            course=instance.course, status=1
        )
        for enrollment in enrollments:
            recipient_list = [enrollment.user.email]
            send_mail_template(subject, template_name, context, recipient_list)


models.signals.post_save.connect(
    post_save_announcement, sender=Announcements,
    dispatch_uid='post_save_announcement'
)

# objects = CourseManager()
