import random

def enforce_gender_rule(sheet):
    # What it does ?
    # checks if the gender is filled and if the part of speech is not filled, it fills it with "noun    
    data = sheet.get_all_values() # get all values in the sheet
    for row in data[1:]: # Iterate through each row starting from the second row (skipping headers)
        gender = row[0]  # Gender column (first column)
        part_of_speech = row[3]  # Part of Speech column (fourth column)
        # Check if Gender column has a value and Part of Speech is not already filled
        if gender and not part_of_speech:
            sheet.update_cell(data.index(row) + 1, 4, 'Noun') # Update Part of Speech to 'Noun'
            print(f"Updated Part of Speech for row {data.index(row) + 1} to 'Noun'.")

def capitalize_first_letter(worksheet):
    # What it does ?
    # This function capitalizes the first letter of each cell in the worksheet
    #so this function will run every once when the api connection is established to check and change from the last updated row
    #this is getting rate limited for now

    # Get all the data
    data = worksheet.get_all_values()
    for row_index, row in enumerate(data):
        for col_index, cell in enumerate(row):
            if cell and cell[0].islower():
                capitalized_cell = cell[0].upper() + cell[1:]
                # Update the cell in the worksheet
                worksheet.update_cell(row_index + 1, col_index + 1, capitalized_cell)

def quiz(data, num_questions):
    # What it does ?
    # This function is a quiz that asks the user to input the meaning of a word and checks if it is correct 
    
    score = 0
    if num_questions:
        # Shuffle and select the required number of questions
        questions = random.sample(data, min(num_questions, len(data)))
    else:
        questions = data
    for entry in questions:
        word = entry['Word']
        correct_meaning = entry['English Meaning']
        user_answer = input(f"What is the meaning of the word '{word}'? ")
        if user_answer.strip().lower()== 'break':
            break
        elif user_answer.strip().lower() == correct_meaning.strip().lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct meaning of {word} is '{correct_meaning}'.")
    print(f"Your final score is {score} out of {len(questions)}")