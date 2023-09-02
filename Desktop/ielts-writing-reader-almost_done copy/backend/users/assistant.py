from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# from api_key import openai_key  # Make sure you have api_key.py with the OpenAI API key
import openai


@api_view(['POST'])
def ask_to_assistance(request):
    if request.method == 'POST':
        prompt_2 = request.data.get('prompt_2')
        gptkey = request.data.get('gptkey')
        openai.api_key = gptkey

        if prompt_2 is not None:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant that answers questions."
                    },
                    {
                        "role": "user",
                        "content": 'Imagine that you are my writing assistance and I will give you the text I wrote below. What would you suggest me to do improve my writings with examples. How would you approach my text, and could have I done to improve my text. Here is the text:  ' + prompt_2 
                    },
                ]
            )

            answer = response['choices'][0]['message']['content']
            return Response({"prompt_2": prompt_2, "answer": answer})
        else:
            return Response({"prompt_2": prompt_2, "answer": "Prompt 2 is missing or empty."})


@api_view(['POST'])
def ask_to_error(request):
    if request.method == 'POST':
        prompt_2 = request.data.get('prompt_2')
        gptkey = request.data.get('gptkey')
        openai.api_key = gptkey

        if prompt_2 is not None:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant that answers questions."
                    },
                    {
                        "role": "user",
                        "content": 'Here is the answer: ' + prompt_2 + '. Can you show me errors in grammar and punctuation in a list form with corrections'
                    },
                ]
            )

            answer = response['choices'][0]['message']['content']
            return Response({"prompt_2": prompt_2, "answer": answer})
        else:
            return Response({"prompt_2": prompt_2, "answer": "Prompt 2 is missing or empty."})
        



@api_view(['POST'])
def ask_to_lexical(request):
    if request.method == 'POST':
        prompt_2 = request.data.get('prompt_2')
        gptkey = request.data.get('gptkey')
        openai.api_key = gptkey

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that answers questions."
                },
                {
                    "role": "user",
                    "content": "Here is the answer: " + prompt_2 + ". What kind of changes could I have done in terms of Lexical Resource to gain higher band and tell me why? Explain it with bulletpoints. Give example sentences for each bulletpoint for users to see how it works?"
                },
            ]
        )

        answer = response['choices'][0]['message']['content']  # Corrected indentation here

        return Response({"prompt_2": prompt_2, "answer": answer})


@api_view(['POST'])
def ask_to_grammatical(request):
    if request.method == 'POST':
        prompt_2 = request.data.get('prompt_2')
        gptkey = request.data.get('gptkey')
        openai.api_key = gptkey

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that answers questions."
                },
                {
                    "role": "user",
                    "content": "Here is the answer: " + prompt_2 + "and What kind of changes could I have done in terms of Grammatical Range and Accuracy to write better text and tell me why? Explain it with bulletpoints. Give example sentences for each bulletpoint for users to see how it works? and give examples based on my answer I gave you above as Original sentence and Revised sentence"

                    
                },
            ]
        )

        answer = response['choices'][0]['message']['content']  # Corrected indentation here

        return Response({"prompt_2": prompt_2, "answer": answer})



@api_view(['POST'])
def ask_to_rewritten_by_AI(request):
    if request.method == 'POST':
        prompt_2 = request.data.get('prompt_2')
        gptkey = request.data.get('gptkey')
        openai.api_key = gptkey

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that answers questions."
                },
                {
                    "role": "user",
                    "content": 'Here is the text: ' + prompt_2 + ". How would you write this text if you were the one writing this text based on the text I gave you "
                },
            ]
        )

        answer = response['choices'][0]['message']['content']  # Corrected indentation here

        return Response({ "prompt_2": prompt_2, "answer": answer})



