# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import CharField, ModelForm

from .models import Topic, UserPreferences


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['subject', 'url', 'description', 'depth']


class PreferencesForm(ModelForm):
    class Meta:
        model = UserPreferences
        #fields = ['user', 'topic', 'users_topic_interest_level', 'users_current_skill_level']
        fields = ['users_topic_interest_level', 'users_current_skill_level']
