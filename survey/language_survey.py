from survey import AnonymousSurvey

question = "What language did you first learn to speak?"
language_survey = AnonymousSurvey(question)

language_survey.show_question()
print("To quit at any time, press 'q'")

while True:
    response = input("Language: ")
    if response == 'q':
        break
    else:
        language_survey.store_response(response)
    
print("\nThanks you for your participation!")
if language_survey.responses:
    language_survey.show_results()
