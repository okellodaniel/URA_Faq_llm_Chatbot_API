# Generated by Django 5.1.1 on 2024-10-07 18:28

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('section', models.CharField(max_length=255)),
                ('model_used', models.CharField(max_length=255)),
                ('response_time', models.FloatField()),
                ('relevance', models.CharField(max_length=50)),
                ('relevance_explanation', models.TextField()),
                ('prompt_tokens', models.IntegerField()),
                ('completion_tokens', models.IntegerField()),
                ('total_tokens', models.IntegerField()),
                ('eval_prompt_tokens', models.IntegerField()),
                ('eval_completion_tokens', models.IntegerField()),
                ('eval_total_tokens', models.IntegerField()),
                ('openai_cost', models.FloatField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.IntegerField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rag.conversation')),
            ],
        ),
    ]
