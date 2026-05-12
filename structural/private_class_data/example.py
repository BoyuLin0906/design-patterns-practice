from dataclasses import dataclass


def print_section(title):
    print(f'\n=== {title} ===')


@dataclass(frozen=True)
class ReportConfig:
    file_path: str
    export_format: str
    delimiter: str = ','
    include_header: bool = True


class ReportExporter:
    def __init__(self, file_path, export_format, delimiter=',', include_header=True):
        self._config: ReportConfig = ReportConfig(
            file_path=file_path,
            export_format=export_format,
            delimiter=delimiter,
            include_header=include_header,
        )

    def export(self, columns, rows):
        lines = []

        if self._config.include_header:
            lines.append(self._config.delimiter.join(columns))

        for row in rows:
            values = [str(row[column]) for column in columns]
            lines.append(self._config.delimiter.join(values))

        return '\n'.join(lines)

    def show_export_result(self, columns, rows):
        print(
            f'Report ready for {self._config.file_path} '
            f'({self._config.export_format.upper()})'
        )
        print(self.export(columns, rows))


if __name__ == '__main__':
    sales_rows = [
        {'name': 'North', 'total': 1200, 'owner': 'Alice'},
        {'name': 'South', 'total': 980, 'owner': 'Bob'},
    ]

    exporter = ReportExporter(
        file_path='exports/monthly_sales.csv',
        export_format='csv',
        delimiter=',',
        include_header=True,
    )

    print_section('Export Result')
    exporter.show_export_result(
        columns=['name', 'total', 'owner'],
        rows=sales_rows,
    )

    print_section('Protected Data')
    try:
        exporter._config.file_path = 'exports/other.csv'
    except Exception as error:
        print('Exporter behavior stays the same because config is locked.')
        print(f'Attempt to change config failed: {error}')
