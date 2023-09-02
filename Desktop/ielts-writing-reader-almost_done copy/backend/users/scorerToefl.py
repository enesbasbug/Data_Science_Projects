
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# from api_key import openai_key  # Make sure you have api_key.py with the OpenAI API key
import openai

# openai.api_key = openai_key

def read_the_criteria_of_ielts(doc):
    with open(doc, 'r') as file:
        text = file.read()
    return text

@api_view(['POST'])
def ask_to_mark(request):
    if request.method == 'POST':
        prompt = request.data.get('prompt')
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
                    "content": read_the_criteria_of_ielts('toefl.txt') + ". They were all the assessment criteria I mentioned above, based on this information and criteria; which raw score from 1 to 5 (may consider 1 and one quarter 1 and a half 1 and three quarters.) would this text receive and why, for the promt (question) given?, you must also give scaled score as I showed you above. Could you also mention what score you gave for each assessment criteria. Here is the prompt (questions):  " + prompt + ' and here is the answer: ' + prompt_2 + '.'
                }
            ]
        )

        answer = response['choices'][0]['message']['content']  # Corrected indentation here
        # print(answer)

        return Response({"prompt": prompt, "prompt_2": prompt_2, "answer": answer})


@api_view(['POST'])
def ask_to_error(request):
    if request.method == 'POST':
        prompt = request.data.get('prompt')
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
            return Response({"prompt": prompt, "prompt_2": prompt_2, "answer": answer})
        else:
            return Response({"prompt": prompt, "prompt_2": prompt_2, "answer": "Prompt 2 is missing or empty."})
        



@api_view(['POST'])
def ask_to_lexical(request):
    if request.method == 'POST':
        prompt = request.data.get('prompt')
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
                    "content": "Here is the answer: " + prompt_2 + ". What kind of changes could I have done in terms of Lexical Resource to gain higher band and tell me why? Explain it with 5 bulletpoints. Give example sentences for each bulletpoint for users to see how it works?"
                },
            ]
        )

        answer = response['choices'][0]['message']['content']  # Corrected indentation here

        return Response({"prompt": prompt, "prompt_2": prompt_2, "answer": answer})


@api_view(['POST'])
def ask_to_grammatical(request):
    if request.method == 'POST':
        prompt = request.data.get('prompt')
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
                    "content": "Here is the answer: " + prompt_2 + "and here is the criteria info:" + read_the_criteria_of_ielts('toefl.txt') + ". They were all the assessment criteria I mentioned above, based on this information and criteria; What kind of changes could I have done in terms of Grammatical Range and Accuracy to gain higher band and tell me why? Explain it with bulletpoints. Give example sentences for each bulletpoint for users to see how it works? and give examples based on my answer I gave you above as Original text and Revised text"

                    
                },
            ]
        )

        answer = response['choices'][0]['message']['content']  # Corrected indentation here

        return Response({"prompt": prompt, "prompt_2": prompt_2, "answer": answer})



@api_view(['POST'])
def ask_to_rewritten_by_AI(request):
    if request.method == 'POST':
        prompt = request.data.get('prompt')
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
                    "content": 'Here is the answer: ' + prompt_2 + ". How would you write this text if you were the one writing this text based on this question '" + prompt + "' considering the same assestment criteria, Do not forget that the ideal length is between 350 to 400 words."
                },
            ]
        )

        answer = response['choices'][0]['message']['content']  # Corrected indentation here

        return Response({"prompt": prompt, "prompt_2": prompt_2, "answer": answer})



@api_view(['POST'])
def ask_to_band_five(request):
    if request.method == 'POST':
        prompt = request.data.get('prompt')
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
                    "content": 'Here is the criteria; ' + read_the_criteria_of_ielts('toefl.txt') + '. This is the question you are gonna answer to ' + prompt + '. Write me a text that should achieve a score 5 based on the assesment criteria you have learned before. Do not forget that the ideal length is between 350 to 400 words.'
                },
            ]
        )

        answer = response['choices'][0]['message']['content']  # Corrected indentation here

        return Response({"prompt": prompt, "prompt_2": prompt_2, "answer": answer})

