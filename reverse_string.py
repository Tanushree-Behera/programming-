def reverse_string(sentence):
  words = sentence.split()
  res2 = words[::-1]
  final_string = " ".join(res2)
  print(final_string)
  
      
sentence = "the sky is blue"
print(sentence)
res = reverse_string(sentence)
