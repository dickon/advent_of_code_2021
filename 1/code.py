samples = """199
200
208
210
200
207
240
269
260
263
"""
print(samples)
def increments(numbers):
    return len([i for i in range(len(numbers)) if i > 0 and numbers[i-1] < numbers[i]])
def text_to_intlist(text):
    return [int(x) for x in text.split('\n') if x]
def sliding3(numbers):
    return [numbers[i-2] + numbers[i-1] + numbers[i] for i in range(len(numbers)) if i >= 2]
assert increments([1,2,3]) == 2
assert increments(text_to_intlist(samples)) == 7
print(sliding3(text_to_intlist(samples)))
assert increments(sliding3(text_to_intlist(samples))) == 5
data = open('1/data.txt', 'r').read()
print(increments(text_to_intlist(data)))
print(increments(sliding3(text_to_intlist(data))))

