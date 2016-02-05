# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import ModelForm

from .models import Topic, UserPreferences


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['subject', 'url', 'description', 'depth']


class PreferencesForm(ModelForm):
    class Meta:
        model = UserPreferences
        fields = ['user_topic', 'user', 'users_current_skill_level', 'topic']
