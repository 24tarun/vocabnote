from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import quiz
import gspread
from google.oauth2.service_account import Credentials
from django import forms
import random

# Path to your credentials JSON file
CREDS_FILE =  "creds.json"

# Define the scope
SCOPE = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

def options_view(request):
    return render(request, 'options.html')


def get_sheet():
    creds = Credentials.from_service_account_file(CREDS_FILE, scopes=SCOPE)
    client = gspread.authorize(creds)
    sheet = client.open('German words and meanings').sheet1
    return sheet

class DataEntryForm(forms.Form):
    Gender = forms.CharField(max_length=10, required=False)
    Word = forms.CharField(max_length=100)
    English_Meaning = forms.CharField(max_length=200)
    Part_of_Speech = forms.CharField(max_length=50, required=False)
    Other_Comments = forms.CharField(widget=forms.Textarea, required=False)

def enter_data_view(request):
    if request.method == 'POST':
        form = DataEntryForm(request.POST)
        if form.is_valid():
            sheet = get_sheet()
            gender = form.cleaned_data['Gender']
            word = form.cleaned_data['Word']
            english_meaning = form.cleaned_data['English_Meaning']
            part_of_speech = form.cleaned_data['Part_of_Speech']
            other_comments = form.cleaned_data['Other_Comments']
            
            # Append the new row to the sheet
            sheet.append_row([gender, word, english_meaning, part_of_speech, other_comments])
            
            return redirect('success')
    else:
        form = DataEntryForm()
    
    return render(request, 'enter_data.html', {'form': form})

def quiz_view(request):
    if request.method == 'POST':
        if 'num_questions' in request.POST:
            # Handle the number of questions selection
            num_questions = int(request.POST.get('num_questions', 2))  # Default to 2 questions
            return redirect(f'/quiz/?num_questions={num_questions}')  # Redirect to the same view with the number of questions

        # Process the submitted answers
        answers = request.POST.getlist('answers')
        correct_answers = request.POST.getlist('correct_answers')
        questions = request.POST.getlist('questions')
        
        # Calculate the score
        score = sum(1 for answer, correct in zip(answers, correct_answers) if answer.strip().lower() == correct.strip().lower())
        
        # Prepare data for rendering
        results = zip(questions, answers, correct_answers)  # Combine questions, answers, and correct answers
        return render(request, 'quiz.html', {'score': score, 'total': len(correct_answers), 'results': results})

    # If it's a GET request, show the quiz form
    num_questions = int(request.GET.get('num_questions', 0))  # Default to 0 questions
    questions = []

    if num_questions > 0:
        data = get_sheet().get_all_records()
        # Prepare questions with correct answers
        questions = random.sample(data, min(num_questions, len(data)))
        for question in questions:
            question['correct_answer'] = question['English Meaning']  # Add a new key for the correct answer

    return render(request, 'quiz.html', {'questions': questions, 'num_questions': num_questions})

def success_view(request):
    return HttpResponse("Operation was successful!")

def success_view(request):
    return render(request, 'success.html')


