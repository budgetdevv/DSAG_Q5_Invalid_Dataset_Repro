# What is the issue?
It seems like the given quiz dataset have encoding issues. This is a minimal reproducible example that demonstrates the issue at hand

# How to run
`python3 try_read_quiz_qns.py`

# Error output
```
trumpmcdonaldz@TrumpMcDonaldz-MacBook-Air DSAG_Q5_Invalid_Dataset_Repro % python3 try_read_quiz_qns.py
Traceback (most recent call last):
  File "/Users/trumpmcdonaldz/Desktop/DSAG_Q5_Invalid_Dataset_Repro/try_read_quiz_qns.py", line 2, in <module>
    for line in stream.read().splitlines():
                ^^^^^^^^^^^^^
  File "<frozen codecs>", line 322, in decode
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 132: invalid continuation byte
```

# Cause
Person that wrote the .txt file uses Windows, which uses the `cp1252` encoding format.

# Solution
`input_stream = open("quiz_questions.txt", encoding='cp1252');`
