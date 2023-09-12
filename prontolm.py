import re
import collections
import sys

COMPLETION_LIMIT = 20
VARIATIONS = 5

text = """"""

def complete(prompt):
    prompt_length = len(prompt)

    # Find all instances of prompt
    instances = [m.start() for m in re.finditer(prompt, dataset)]

    # Find all possible next characters
    possible_completions = []
    for instance in instances:
        # Skip if prompt is at the end of the dataset
        if len(dataset) < instance + prompt_length + 1:
            continue

        # Add next character to possible completions
        possible_completions.append(dataset[instance + prompt_length])

    # Count occurrences of each possible next character
    possibilities = collections.Counter(possible_completions).most_common()

    # Return the top VARIATIONS possibilities
    return [x[0] for x in possibilities[:VARIATIONS]]

def recursive_complete(prompt, depth=1, max_completions=VARIATIONS):
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
        results.extend(recursive_complete(prompt + completion, depth + 1, max_completions))
    
    return results


sexy_mode = False if input('Fast mode (F) or Sexy mode (S)? ').lower() == 'f' else True
sys.setrecursionlimit(10000)
alnum = re.compile('[^a-zA-Z0-9 ]')

dataset = text.lower()
dataset = alnum.sub('', dataset).replace('  ', ' ')

while True:
    prompt = input('Prompt: ')
    prompt = alnum.sub('', prompt.lower())
    
    completions = recursive_complete(prompt)

    print("Completions:")
    for index, completion in enumerate(completions[:VARIATIONS]):
        label = chr(97 + index) # Convert index to alphabet
        print(f"{label}. {completion}")

    valid_choices = [chr(97 + i) for i in range(VARIATIONS)]
    vote = input(f"Which completion do you prefer? ({'/'.join(valid_choices)}): ").strip().lower()
    while vote not in valid_choices:
        print(f"Invalid choice. Please select one of {', '.join(valid_choices)}.")
        vote = input(f"Which completion do you prefer? ({'/'.join(valid_choices)}): ").strip().lower()

    chosen_text = completions[ord(vote) - 97]  # Convert vote back to index
    dataset += chosen_text

    print(len(dataset))
    print('\nFeedback saved\n')