# Template Method Pattern Practice

This folder shows a simple Template Method pattern example.

Template Method is a behavioral design pattern that defines the fixed steps of an algorithm in a base class while letting subclasses customize specific parts.

Files:

- `example.py`: an ETL pipeline that converts txt, csv, and pdf documents into JSON output
- `README.md`: short notes for this pattern

Example:

- `DocumentETL` is the abstract class that defines the ETL flow in `run`
- `TxtDocumentETL`, `CsvDocumentETL`, and `PdfDocumentETL` are the concrete classes
- each concrete class changes `extract` and `transform` while reusing the shared `load` step

Advantages:

- keeps the overall ETL workflow consistent
- moves document-specific steps into small subclasses
- makes it easier to add new document types later

Disadvantages:

- uses inheritance, which can feel heavy for very small examples
- careless subclass changes can break Liskov Substitution Principle expectations if they no longer behave like the base workflow
- changing the template structure may affect every subclass

When to use:

- when multiple workflows share the same high-level steps
- when only a few parts of an algorithm need to vary
- when you want to avoid repeating the same process order in many classes

Reference:

- https://refactoring.guru/design-patterns/template-method
