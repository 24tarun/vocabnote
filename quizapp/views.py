from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import VocabItem
import random

# Create your views here.
@login_required
def quiz_view(request):
    vocabs = list(VocabItem.objects.filter(user=request.user))
    if not vocabs:
        return render(request, 'quiz.html', {'score': None, 'total': 0, 'questions': None})

    if request.method == 'POST':
        if 'num_questions' in request.POST:
            try:
                num_questions = int(request.POST.get('num_questions', 1))
            except ValueError:
                num_questions = 1
            num_questions = max(1, num_questions)
            # Repeat vocab words if needed to reach num_questions
            if len(vocabs) < num_questions:
                questions = []
                while len(questions) < num_questions:
                    needed = num_questions - len(questions)
                    random.shuffle(vocabs)
                    questions.extend(vocabs[:needed])
            else:
                questions = random.sample(vocabs, num_questions)
            return render(request, 'quiz.html', {'questions': questions, 'score': None, 'total': num_questions})
        else:
            questions = request.POST.getlist('questions')
            answers_gender = request.POST.getlist('answers_gender')
            answers_english_meaning = request.POST.getlist('answers_english_meaning')
            answers_part_of_speech = request.POST.getlist('answers_part_of_speech')
            answers_other_comments = request.POST.getlist('answers_other_comments')
            correct_gender = request.POST.getlist('correct_gender')
            correct_english_meaning = request.POST.getlist('correct_english_meaning')
            correct_part_of_speech = request.POST.getlist('correct_part_of_speech')
            correct_other_comments = request.POST.getlist('correct_other_comments')
            score = 0
            results = []
            for idx in range(len(questions)):
                user_gender = answers_gender[idx].strip().lower()
                user_meaning = answers_english_meaning[idx].strip().lower()
                user_pos = answers_part_of_speech[idx].strip().lower()
                user_comments = answers_other_comments[idx].strip().lower()
                corr_gender = (correct_gender[idx] or '').strip().lower()
                corr_meaning = (correct_english_meaning[idx] or '').strip().lower()
                corr_pos = (correct_part_of_speech[idx] or '').strip().lower()
                corr_comments = (correct_other_comments[idx] or '').strip().lower()
                # Only require gender and english meaning to be correct
                correct = (user_gender == corr_gender and user_meaning == corr_meaning)
                score += int(correct)
                results.append({
                    'word': questions[idx],
                    'user_gender': user_gender,
                    'user_meaning': user_meaning,
                    'user_pos': user_pos,
                    'user_comments': user_comments,
                    'corr_gender': corr_gender,
                    'corr_meaning': corr_meaning,
                    'corr_pos': corr_pos,
                    'corr_comments': corr_comments,
                    'correct': correct
                })
            return render(request, 'quiz.html', {
                'score': score,
                'total': len(questions),
                'results': results,
                'questions': None
            })

    # GET request: ask for number of questions
    return render(request, 'quiz.html', {'questions': None, 'score': None, 'total': 0, 'vocab_count': len(vocabs)})