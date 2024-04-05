import random


def generate_number_rows_and_qa(nr, nc, nq):
    """
    Generates a tuple, where the first element is a list of lists of random numbers, and the second element is a list of
    tuples, where each tuple contains a question and a list of choices.
    """
    numbers = [[get_biased_random_number() for _ in range(nc)] for _ in range(nr)]

    #  re-roll if there are duplicates
    while len(set(n for row in numbers for n in row)) < nr * nc:
        numbers = [[get_biased_random_number() for _ in range(nc)] for _ in range(nr)]

    # sort numbers in each row in ascending order
    for row in numbers:
        row.sort()

    questions = []

    while len(questions) < nq:
        if random.random() < 0.8:
            questions.append(generate_recall_question(nc, nr, numbers))
        else:
            questions.append(generate_divide_question(numbers))

    return numbers, questions


def generate_recall_question(nc, nr, numbers):
    r = random.randint(0, nr - 1)
    c = random.randint(0, nc - 1)
    qa = (f"What number is at row {r + 1}, column {c + 1}?", numbers[r][c])
    choices = [numbers[r][c]]
    while len(choices) < 5:
        choice = get_biased_random_number()
        if choice not in choices:
            choices.append(choice)
    random.shuffle(choices)
    return (qa, choices)


def generate_divide_question(numbers):
    """
    Generates a question like "how many numbers are divisible by 3?" and a list of choices.
    """
    div = random.randint(2, 5)

    qa = (f"How many numbers are divisible by {div}?", sum(1 for row in numbers for n in row if n % div == 0))
    choices = [qa[1]]
    while len(choices) < 5:
        choice = random.randint(0, 6)
        if choice not in choices:
            choices.append(choice)
    return (qa, choices)

def get_biased_random_number():
    if random.random() < 0.1:
        return random.randint(100, 500)
    elif random.random() < 0.3:
        return random.randint(50, 100)
    elif random.random() < 0.3:
        return random.randint(10, 50)
    else:
        return random.randint(1, 10)

