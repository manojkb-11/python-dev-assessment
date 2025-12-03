def filter_and_sort_evens(numbers):
    evens = [n for n in numbers if n % 2 == 0]
    return sorted(evens)
def count_character_frequency(text):
    freq = {}
    for ch in text.lower():
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq
print(filter_and_sort_evens([3, 1, 4, 1, 5, 9, 2, 6]))
print(count_character_frequency("Hello World"))