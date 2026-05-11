from copy import deepcopy


def print_section(title):
    print(f'\n=== {title} ===')


class ReportConfig:
    def __init__(
        self,
        report_name,
        file_type,
        columns,
        filters,
        format_settings,
    ):
        self.report_name = report_name
        self.file_type = file_type
        self.columns = list(columns)
        self.filters = list(filters)
        self.format_settings = dict(format_settings)

    def clone(self):
        return deepcopy(self)

    def show(self):
        print(f'Report: {self.report_name}')
        print(f'File type: {self.file_type}')
        print(f'Columns: {", ".join(self.columns)}')
        print(f'Filters: {", ".join(self.filters)}')
        print('Format settings:')
        for name, value in self.format_settings.items():
            print(f'- {name}: {value}')


if __name__ == '__main__':
    csv_report_config = ReportConfig(
        report_name='Daily Orders CSV Report',
        file_type='csv',
        columns=['order_id', 'customer', 'total'],
        filters=['today', 'paid and pending'],
        format_settings={
            'delimiter': ',',
            'include_header': True,
        },
    )

    print_section('Original CSV Config')
    csv_report_config.show()

    print_section('Clone And Change To XLSX')
    xlsx_report_config = csv_report_config.clone()
    xlsx_report_config.report_name = 'Daily Orders XLSX Report'
    xlsx_report_config.file_type = 'xlsx'
    xlsx_report_config.filters.append('export for finance team')
    xlsx_report_config.format_settings = {
        'sheet_name': 'Orders',
        'freeze_header': True,
    }
    xlsx_report_config.show()

    print_section('Original Config Stays The Same')
    csv_report_config.show()
