# Design Patterns Practice

This repository is for practicing common software design patterns.

The practice structure follows the main pattern categories described by Refactoring.Guru,
with a few additional patterns referenced from SourceMaking.
This repository currently tracks 26 patterns in total.

- Creational patterns
- Structural patterns
- Behavioral patterns

Reference:

- https://refactoring.guru/design-patterns
- https://sourcemaking.com/design_patterns

## Goal

Use this repository to:

- understand common pattern categories
- implement typical patterns with small examples
- build familiarity with design tradeoffs

## Repository Structure

Each pattern folder is intended to stay small and focused, and usually contains:

- `example.py` for the runnable example
- `README.md` for a short practical explanation

```text
.
├── README.md
├── behavioral/
├── creational/
└── structural/
```

## How to Run

Go to a specific pattern directory and run `example.py`.

Example:

```bash
cd behavioral/strategy
python3 example.py
```

## Pattern Checklist

### Creational

- Factory Method
- Abstract Factory
- Builder
- Object Pool
- Prototype
- Singleton

### Structural

- Adapter
- Bridge
- Composite
- Decorator
- Facade
- Flyweight
- Private Class Data
- Proxy

### Behavioral

- Chain of Responsibility
- Command
- Interpreter
- Iterator
- Mediator
- Memento
- Null Object
- Observer
- State
- Strategy
- Template Method
- Visitor

## Environment Setup

For `uv` installation and virtual environment notes, see [UV_SETUP.md](./UV_SETUP.md).
