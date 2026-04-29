# Repository Rules

This repository is for practicing software design patterns with small, focused examples.

## General Rules

- Keep examples simple and readable.
- Prefer small files over large frameworks or full applications.
- Use one clear pattern exercise per folder.
- Use Python for practice files unless a folder says otherwise.
- Each pattern folder should mainly contain `example.py` and `README.md`.
- Treat existing pattern folders as templates for future folders.

## File Roles

Each folder uses a simple two-file structure.

### `example.py`

- Implement the target design pattern directly.
- Keep the example focused on how the pattern works.
- Improve extensibility, readability, and separation of concerns.
- Keep the code understandable without adding unnecessary complexity.
- Do not add basic type hints such as `name: str`, `count: int`, `items: list[str]`, or routine `-> None` return types just for completeness.
- Keep typing light for practice examples, but retain important class-based type hints such as `user: UserData` or `command: Command` when they make the code easier to understand.
- If there is any tension between "keep examples simple" and the typing guidance above, prefer the typing guidance, but keep the hints limited to important class-based relationships.
- Prefer one small, concrete domain example such as a navigator, notifier, payment flow, or document workflow.
- Keep the structure close to the pattern's core roles.
- Include a short runnable example in `if __name__ == '__main__':`.
- Make the output easy to read from the terminal.
- Add a small `print_section(title)` helper and use it in `if __name__ == '__main__':` so terminal output is grouped into clear sections, like the `command` and `state` examples.

Recommended `example.py` template:

- define the common abstraction or shared interface first
- add a few concrete implementations of that interface
- add the main object that uses or coordinates those implementations
- add a small print helper only if it improves readability
- show the pattern in action in a short main block

### `README.md`

- Keep the README short and practical.
- Start with a one-sentence description of the pattern.
- Describe the files in the folder.
- Explain the example using the actual class names from `example.py`.
- Include a short advantages section.
- Include a short disadvantages section.
- Include a short "When to use" section.
- Include a reference link when there is a clear canonical source.
- Keep notes short and practical.
- Avoid long theory unless the folder specifically asks for it.

Recommended `README.md` template:

- title: `# <Pattern Name> Pattern Practice`
- short intro: what the pattern is in plain language
- files: `example.py` and `README.md`
- example: map the concrete classes in `example.py` to the pattern roles
- advantages
- disadvantages
- when to use
- reference

## Naming Rules

- Use lowercase file and folder names.
- Use descriptive folder names based on the pattern name.
- For multi-word pattern names, keep the full pattern name in lowercase folder form. Use underscores between words. Examples: `template_method` and `chain_of_responsibility`.
- Keep public class and function names clear and conventional.
- Match names in `README.md` to the real names used in `example.py`.

## Scope Rules

- Do not solve multiple patterns in one example unless explicitly requested.
- Do not add extra infrastructure unless it supports the practice goal.
- Prefer clarity over optimization.
- Prefer a small teaching example over a realistic but noisy design.
