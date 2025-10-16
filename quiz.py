questions = [
    {'question': 'What is the capital of Italy?', 'A': 'A. Berlin', 'B': 'B. London', 'C': 'C. Paris', 'D': 'D. Rome', 'Answer': 'D'},
    {'question': 'What is the capital of China?', 'A': 'A. Berlin', 'B': 'B. Beijing', 'C': 'C. Paris', 'D': 'D. Rome', 'Answer': 'B'},
    {'question': 'What is the capital of India?', 'A': 'A. Berlin', 'B': 'B. London', 'C': 'C. Delhi', 'D': 'D. Paris', 'Answer': 'C'}
]

# Automated answers, simulate correct responses
automated_answers = ['D', 'B', 'C']  # Just set the correct answers

score = 0

for i, q in enumerate(questions):
    print(q['question'])
    print(q['A'])
    print(q['B'])
    print(q['C'])
    print(q['D'])
    
    # Use the automated answer (simulating user input)
    your_answer = automated_answers[i]
    
    print(f"Your answer: {your_answer}")
    
    if your_answer == q['Answer']:
        print(f"Correct! The answer is {your_answer}")
        score += 1
    else:
        print(f"Incorrect! The correct answer was {q['Answer']}")
        score -= 1

print(f'You got {score} out of {len(questions)} correct.')
