questions = [
    {'question': 'What is the capital of Italy?', 'A': 'A. Berlin', 'B': 'B. London', 'C': 'C. Paris', 'D': 'D. Rome', 'Answer': 'D'},
    {'question': 'What is the capital of China?', 'A': 'A. Berlin', 'B': 'B. Beijing', 'C': 'C. Paris', 'D': 'D. Rome', 'Answer': 'B'},
    {'question': 'What is the capital of India?', 'A': 'A. Berlin', 'B': 'B. London', 'C': 'C. Delhi', 'D': 'D. Paris', 'Answer': 'C'}
]

score = 0
for q in questions:
    print(q['question'])
    print(q['A'])
    print(q['B'])
    print(q['C'])
    print(q['D'])
    your_answer = input('What is your answer? ').capitalize()
    if your_answer == q['Answer']:
        print('Correct!, The answer is ' + q['Answer'])
        score += 1
    else:
        print('Incorrect!')
        score -= 1
print(f'You got {score} out of {len(questions)} correct.')

