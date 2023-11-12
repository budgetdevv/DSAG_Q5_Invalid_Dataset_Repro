with open("quiz_questions.txt") as stream:
    for line in stream.read().splitlines():
        print(line);