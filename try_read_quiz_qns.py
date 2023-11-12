INPUT_PATH = "quiz_questions.txt";

input_stream = open(INPUT_PATH, encoding='cp1252');
input_text = input_stream.read();
print(input_text);
input_stream.close();
input_stream = None;

OUTPUT_PATH = "quiz_questions_utf8.txt";

output_stream = open(OUTPUT_PATH, "w", encoding='utf-8')
output_stream.write(input_text);
output_stream.close();

input_stream = open(OUTPUT_PATH, encoding='utf-8');
input_text = input_stream.read();
print(input_text);