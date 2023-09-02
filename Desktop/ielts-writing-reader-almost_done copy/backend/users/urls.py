
from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView
from . import scorer
from . import scorerToefl
from . import assistant


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    # path('add_gptkey', GptKeyView.as_view(), name='add_gptkey'),


    path('assistant/ask_to_assistance', assistant.ask_to_assistance, name='ask_to_assistance'),
    path('assistant/ask_to_error', assistant.ask_to_error, name='ask_to_error'),
    path('assistant/ask_to_lexical', assistant.ask_to_lexical, name='ask_to_lexical'),
    path('assistant/ask_to_grammatical', assistant.ask_to_grammatical, name='ask_to_grammatical'),
    path('assistant/ask_to_rewritten_by_AI', assistant.ask_to_rewritten_by_AI, name='ask_to_rewritten_by_AI'),
    
    path('toefl/ask_to_mark', scorerToefl.ask_to_mark, name='ask_to_mark'),
    path('toefl/ask_to_error', scorerToefl.ask_to_error, name='ask_to_error'),
    path('toefl/ask_to_lexical', scorerToefl.ask_to_lexical, name='ask_to_lexical'),
    path('toefl/ask_to_grammatical', scorerToefl.ask_to_grammatical, name='ask_to_grammatical'),
    path('toefl/ask_to_rewritten_by_AI', scorerToefl.ask_to_rewritten_by_AI, name='ask_to_rewritten_by_AI'),
    path('toefl/ask_to_band_five', scorerToefl.ask_to_band_five, name='ask_to_band_five'),

    path('ielts/ask_to_mark', scorer.ask_to_mark, name='ask_to_mark'),
    path('ielts/ask_to_error', scorer.ask_to_error, name='ask_to_error'),
    path('ielts/ask_to_lexical', scorer.ask_to_lexical, name='ask_to_lexical'),
    path('ielts/ask_to_grammatical', scorer.ask_to_grammatical, name='ask_to_grammatical'),
    path('ielts/ask_to_rewritten_by_AI', scorer.ask_to_rewritten_by_AI, name='ask_to_rewritten_by_AI'),
    path('ielts/ask_to_band_nine', scorer.ask_to_band_nine, name='ask_to_band_nine'),
]


