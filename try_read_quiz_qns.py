with open("quiz_questions.txt", encoding='utf-8') as stream:
    for line in stream.read().splitlines():
        print(line);