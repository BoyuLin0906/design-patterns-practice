# Repository Rules

This repository is for practicing software design patterns with small, focused examples.

## Core Rules

- Keep examples simple, readable, and focused on one pattern per folder.
- Prefer Python unless a folder says otherwise.
- Keep files small and avoid extra infrastructure unless it supports the practice goal.
- Treat existing pattern folders as templates for future folders.

## Folder Structure

- Each pattern folder should mainly contain `example.py` and `README.md`.
- Use lowercase folder and file names.
- For multi-word pattern names, use lowercase with underscores, such as `template_method` and `chain_of_responsibility`.

## `example.py`

- Implement the pattern directly and keep the structure close to the pattern's core roles.
- Prefer a small concrete domain, such as a navigator, notifier, payment flow, or document workflow.
- Include a short runnable example in `if __name__ == '__main__':`.
- Add `print_section(title)` and use it in the main block so terminal output is grouped into clear sections.
- Keep typing light:
  - do not add basic type hints like `name: str`, `count: int`, `items: list[str]`, or routine `-> None`
  - keep important class-based hints such as `user: UserData`, `command: Command`, `state: OrderState`, or `repository: OrderRepository`
- If simplicity conflicts with typing, keep the important class-based hints and skip the basic ones.

Recommended flow:

- define the shared abstraction first
- add concrete implementations
- add the main coordinating object
- show the pattern in action in a short main block

## `README.md`

- Keep it short and practical.
- Start with a one-sentence description of the pattern.
- Describe `example.py` and `README.md`, for example `behavioral/state/example.py` and `behavioral/state/README.md`.
- Explain the example using the real class names from `example.py`.
- Include short sections for advantages, disadvantages, when to use, and a reference link when helpful.

## Scope

- Do not combine multiple patterns in one example unless explicitly requested.
- Prefer clarity over optimization.
- Prefer a small teaching example over a realistic but noisy design.
