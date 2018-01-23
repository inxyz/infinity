from django.contrib import admin

# Register your models here.

from src.core.models import Topic, Comment
from src.core.forms import TopicForm, CommentForm


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    form = TopicForm


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    form = CommentForm
