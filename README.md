# ProntoLM

**Pro**babilistic **N**on-**To**kenised **L**anguage **M**odel

ProntoLM is a novel approach to machine learning & language models. The goal when creating this was to create something that is machine learning by definition, using the simplest approach possible. I very much doubt this project will ever have a real use case. I created this because I love experimenting with novel ideas. I don't plan on maintaining this project, though I probably will randomly commit improvements when I have bursts of dopamine/motivation to work on it. For those who love tinkering with projects like this, I encourage you to fork this project. I'd love to see how you can improve it. Feel free to send in a PR if you've improved on this project, if it's good, I'll accept it.

## What is ProntoLM?

ProntoLM is a probabilistic, non-tokenised language model that generates completions based on a provided text dataset. It utilizes a simple pattern matching and counting approach to generate the completions, which allows it to run perfectly well without a GPU/CPU with a single thread. The language model does not use weights or a neural network to remain lightweight and easy to modify/improve.

## What is the Purpose of ProntoLM?

ProntoLM aims to provide a basic language model implementation that can generate completions for user prompts without the need for tokenisation. It offers a lightweight alternative to larger and more complex language models, serving as a starting point for simple language generation tasks.

## Benefits

### Simplicity

ProntoLM provides a straightforward implementation of a non-tokenised language model, making it easy to understand and modify for specific use cases.

### Efficiency
With its simplified approach, ProntoLM can generate completions **quickly**, making it suitable for lightweight language generation tasks. Due to its simplicity, ProntoLM can sustainably generate completions faster than ChatGPT while running on a Raspberry Pi.

### Flexibility
ProntoLM allows you to use your own text dataset, enabling customization and adaptation to specific domains or contexts.

### Training
Despite its simplicity, ProntoLM can be trained. When generating completions, ProntoLM forks into different chains and outputs the x most probable responses. You are able to provide feedback (only stored in memory right now) to train it to provide more accurate answers.

## Limitations

It's important to note the following limitations of ProntoLM:

- ProntoLM relies on simple pattern matching and counting, which may not produce high-quality or contextually accurate completions.
- The performance of ProntoLM heavily depends on the quality and representativeness of the provided text dataset.
- The completions generated by ProntoLM are limited to the next character following the prompt occurrences.
- ProntoLM lacks the sophisticated architecture and training of larger language models like GPT-3 or GPT-4.
- With the addition of response variation, ProntoLM is unable to stream responses anymore, even if there is only 1 variation.
- If a prompt is given that isn't in the dataset, Pronto doesn't complete the text.

## Planned Improvements

### Enhanced Tokenisation

Currently, ProntoLM relies on simple pattern matching and counting, which may limit its performance. Future improvements may involve implementing more advanced tokenisation techniques to handle complex language patterns and improve completion generation.

### Automated Dataset Creation

One of the future improvements for ProntoLM is to incorporate automated methods for dataset creation. This could involve web scraping, text extraction from various sources, or utilizing APIs to gather relevant textual data. By automating the dataset creation process, ProntoLM would become more versatile and adaptable to different domains and topics.

### Data Augmentation Techniques

To enhance the diversity and richness of the generated completions, ProntoLM could benefit from the incorporation of data augmentation techniques. These techniques involve applying transformations or modifications to the existing dataset, such as adding noise, paraphrasing, or generating synthetic samples. By leveraging data augmentation, ProntoLM would be able to produce more varied and contextually relevant completions.

### Dynamic Expansion of Dataset

ProntoLM could benefit from a dynamic dataset expansion feature. This improvement would enable the model to automatically incorporate new data from the internet into its existing dataset, thus increasing its knowledge base and improving completion generation. By dynamically expanding the dataset, ProntoLM would be able to generate completions that encompass a broader range of topics and domains.

### Look-Behinds for Context

To enhance the contextual understanding of generated completions, ProntoLM could incorporate look-behinds. Look-behinds allow the model to consider the preceding context when generating completions, enabling it to generate more contextually relevant and coherent output. By incorporating look-behinds, ProntoLM would be able to capture and utilize a broader context for completion generation.

### ~Parallel Generation~ ADDED

Another planned improvement is the implementation of parallel generation in ProntoLM. Parallel generation involves generating multiple completions simultaneously, providing users with a range of options or alternative suggestions. By adopting parallel generation, ProntoLM can offer more diverse and varied completions, catering to different user preferences and needs. Feedback provided by the user on which completion is better will be used to improve the dataset.

### Punctuation/Special Characters

The AI can currently only handle alphanumeric characters. This is a severe limitation as it is unable to define sentence starts/endings or add proper punctuation. ProntoLM is also unable to share website URLs even if they are explicitly defined in the dataset.

### Completion Completion (Get it?)

ProntoLM is currently unable to finish completion at will or even know when to stop. At the moment, ProntoLM is hardcoded to stop after X characters. This needs to be changed.

## Creating a Dataset

You can create a dataset by simply copying text from websites such as Wikipedia. The smaller the dataset is, the more likely it is that ProntoLM will hallucinate completions.

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/QuixThe2nd/ProntoLM.git
   ```

2. Navigate to the project directory:

   ```bash
   cd ProntoLM
   ```

3. Open the script file named `prontolm.py` in your preferred text editor.

4. Set the `text` variable to the desired text dataset. Replace the empty string (`""`) with your text.

   ```python
   text = """
   Your text dataset goes here.
   """
   ```

5. Save the file.

6. Run the script:

   ```bash
   python prontolm.py
   ```

7. The program will prompt you to enter a prompt string.

8. Enter your desired prompt and press Enter.

9. The program will generate a completion based on the provided prompt.

10. Repeat steps 7-9 as desired to generate multiple completions.

## Contributing

Contributions to ProntoLM are welcome! If you have any suggestions, improvements, or bug fixes, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
