def print_section(title):
    print(f'\n=== {title} ===')


class Logger:
    _instance = None

    def __init__(self):
        self.logs = []
        self.level = None
        self.format_name = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Logger()
            print('Create logger instance')

        return cls._instance

    def configure(self, level, format_name):
        self.level = level
        self.format_name = format_name
        print(f'Logger configured: level={level}, format={format_name}')

    def log(self, message):
        if self.level is None:
            raise RuntimeError('Logger must be configured before use.')

        entry = f'[{self.level}] {message}'
        self.logs.append(entry)
        print(entry)

    def show_settings(self):
        print(f'Level: {self.level}')
        print(f'Format: {self.format_name}')

    def show_history(self):
        for entry in self.logs:
            print(entry)


if __name__ == '__main__':
    print_section('Startup Configuration')
    startup_logger = Logger.get_instance()
    startup_logger.configure('INFO', 'plain_text')

    print_section('Reuse Check')
    api_logger = Logger.get_instance()
    worker_logger = Logger.get_instance()
    print(startup_logger is api_logger)
    print(api_logger is worker_logger)

    print_section('Shared Settings')
    worker_logger.show_settings()

    print_section('Write Logs')
    startup_logger.log('Application started')
    api_logger.log('Request received: GET /health')
    worker_logger.log('Background job completed')

    print_section('Shared History')
    startup_logger.show_history()
