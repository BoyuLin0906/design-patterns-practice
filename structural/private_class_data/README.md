# Private Class Data Pattern Practice

Private Class Data is a structural design pattern that hides important state in a separate data object so it can be used safely without being changed after construction.

Files:

- `structural/private_class_data/example.py`: a report exporter with frozen configuration data
- `structural/private_class_data/README.md`: short notes for this pattern

Example:

- `ReportConfig` is a frozen dataclass that stores the export settings that should stay stable after setup
- `ReportExporter` is the main class that creates `ReportConfig` in its constructor
- `ReportExporter` keeps that config internal and focuses its public API on exporting a report
- `export()` builds the report text, and `show_export_result()` presents the final result without exposing each config value
- the main block shows the export output and then shows that the internal config cannot be changed later

Advantages:

- keeps important configuration data grouped in one place
- reduces accidental writes after object creation
- makes the object easier to reason about because setup is fixed

Disadvantages:

- adds another class for a small amount of data
- can feel heavier than needed for simple scripts
- Python still relies partly on convention for privacy

When to use:

- when configuration should be set once during construction
- when you want behavior to depend on stable internal data
- when grouping related fields into one protected object improves clarity

Reference:

- https://sourcemaking.com/design_patterns/private_class_data
