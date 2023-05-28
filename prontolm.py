import re
import collections
import sys
sys.setrecursionlimit(10000)


text = """"""

alnum = re.compile('[^a-zA-Z0-9 ]')

dataset = text.lower()
dataset = alnum.sub('', dataset).replace('  ', ' ')

while True:
    prompt = input("prompt: ").lower()
    prompt = alnum.sub('', prompt)
    final_completion = ''


    def complete(prompt):
        prompt_length = len(prompt)
        instances = [m.start() for m in re.finditer(prompt, dataset)]
        possible_completions = []
        for instance in instances:
            if len(dataset) < instance + prompt_length + 1:
                continue
            possible_completions.append(dataset[instance + prompt_length])
        possibilities = collections.Counter(possible_completions).most_common()
        for possible_completion in possibilities:
            if possible_completion[1] < 2:
                return prompt
            return complete(prompt + possible_completion[0])


    i = 0
    def recursive_complete(prompt):
        global i
        global final_completion
        i += 1
        if i == 1000:
            return
        completion = complete(prompt)
        if completion is None:
            completion = ' '
        print(completion[:1], end='')
        final_completion = final_completion + completion[:1]
        recursive_complete(completion[1:])

    recursive_complete(prompt)
    print('\n'
