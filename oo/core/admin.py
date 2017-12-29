from django.contrib import admin

# Register your models here.

from oo.core.models import Topic, Comment
from oo.core.forms import TopicForm, CommentForm


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    form = TopicForm


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    form = CommentForm
