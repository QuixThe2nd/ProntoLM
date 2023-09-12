import re
import collections
import sys

COMPLETION_LIMIT = 200
VARIATIONS = 5
VERBOSE = True
DATASET = 'olympics_finetuned_2'

with open('datasets/' + DATASET + '.txt', 'r') as f:
    dataset = f.read()

def complete(prompt):
    prompt_length = len(prompt)

    # Find all instances of prompt
    instances = [m.start() for m in re.finditer(prompt, processed_dataset)]

    # Find all possible next characters
    possible_completions = []
    for instance in instances:
        # Skip if prompt is at the end of the processed_dataset
        if len(processed_dataset) < instance + prompt_length + 1:
            continue

        # Add next character to possible completions
        possible_completions.append(processed_dataset[instance + prompt_length])

    # Count occurrences of each possible next character
    possibilities = collections.Counter(possible_completions).most_common()

    # Return the top VARIATIONS possibilities
    return [x[0] for x in possibilities[:VARIATIONS]]

def recursive_complete(prompt, depth=1, max_completions=VARIATIONS):
    if VERBOSE:
        print(prompt)
    # Stop if depth exceeds the COMPLETION_LIMIT.
    if depth > COMPLETION_LIMIT:
        return [prompt]

    # Get next character completions.
    completions = complete(prompt)
    
    # Return if no completions found.
    if not completions:
        return [prompt]

    results = []
    # Recurse for deeper completions and only for top max_completions.
    for completion in completions[:max_completions]:
        last_word = (prompt + completion).split(' ').pop()
        if(last_word not in dataset):
            continue
        # else:
        #     print(last_word + " in processed_dataset")
        results.extend(recursive_complete(prompt + completion, depth + 1, max_completions))
    
    return results


sexy_mode = False if input('Fast mode (F) or Sexy mode (S)? ').lower() == 'f' else True
sys.setrecursionlimit(10000)
alnum = re.compile('[^a-zA-Z0-9 ]')

processed_dataset = dataset.lower()
processed_dataset = alnum.sub('', processed_dataset).replace('  ', ' ')

while True:
    prompt = input('Prompt: ')
    prompt = alnum.sub('', prompt.lower())
    
    completions = recursive_complete(prompt)

    print("Completions:")
    for index, completion in enumerate(completions[:VARIATIONS]):
        print(f"{index+1}. {completion}")

    valid_choices = [str(i+1) for i in range(VARIATIONS)]
    vote = input(f"Which completion do you prefer? ({'/'.join(valid_choices)}): ").strip()
    while vote not in valid_choices:
        print(f"Invalid choice. Please select one of {', '.join(valid_choices)}.")
        vote = input(f"Which completion do you prefer? ({'/'.join(valid_choices)}): ").strip()

    processed_dataset += completions[int(vote)-1]

    print('\nFeedback saved\n')