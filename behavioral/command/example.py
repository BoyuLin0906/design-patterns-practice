from abc import ABC, abstractmethod
from dataclasses import dataclass


def print_section(title):
    print(f'\n=== {title} ===')


@dataclass(frozen=True)
class UserData:
    user_id: int
    user_name: str
    email: str


class Command(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError('Subclasses must implement execute().')


class FakeDatabase:
    def __init__(self):
        self._users = {}

    def save_user(self, user: UserData):
        self._users[user.user_id] = {
            'user_id': user.user_id,
            'user_name': user.user_name,
            'email': user.email,
        }
        return f'user {user.user_id} saved in fake database'


class EmailService:
    def send_user_email(self, user: UserData):
        return f'email sent to {user.email}'


class SaveUserCommand(Command):
    def __init__(self, database: FakeDatabase, user: UserData):
        self._database = database
        self._user = user

    def execute(self):
        return self._database.save_user(self._user)


class SendEmailCommand(Command):
    def __init__(self, email_service: EmailService, user: UserData):
        self._email_service = email_service
        self._user = user

    def execute(self):
        return self._email_service.send_user_email(self._user)


@dataclass
class HistoryEntry:
    action_id: int
    command_name: str
    user_id: int
    command: Command
    result: str
    trigger: str


def describe_command(command: Command):
    user = getattr(command, '_user')
    return type(command).__name__, user.user_id


class CommandHistory:
    def __init__(self):
        self._entries = []
        self._next_action_id = 1

    def add(self, command: Command, result, trigger):
        action_id = self._next_action_id
        self._next_action_id += 1
        command_name, user_id = describe_command(command)
        self._entries.append(
            HistoryEntry(
                action_id=action_id,
                command_name=command_name,
                user_id=user_id,
                command=command,
                result=result,
                trigger=trigger,
            )
        )
        return action_id

    def get_command(self, action_id):
        for entry in self._entries:
            if entry.action_id == action_id:
                return entry.command
        raise ValueError(f'Action {action_id} was not found in history.')

    def display(self):
        print_section('Command History')
        for entry in self._entries:
            print(
                f'#{entry.action_id} | {entry.command_name} | '
                f'user_id={entry.user_id} | trigger={entry.trigger}'
            )
            print(f'   result: {entry.result}')


class CommandInvoker:
    def __init__(self):
        self.history = CommandHistory()
        self._queue = []

    def add_to_queue(self, command: Command):
        self._queue.append(command)
        command_name, user_id = describe_command(command)
        print(f'queued: {command_name} (user_id={user_id})')

    def _run_command(self, command: Command, trigger):
        result = command.execute()
        action_id = self.history.add(command, result, trigger)
        command_name, user_id = describe_command(command)
        print(f'action #{action_id}: {command_name} (user_id={user_id}) -> {result}')
        return action_id

    def run_all(self):
        action_ids = []
        while self._queue:
            command = self._queue.pop(0)
            action_ids.append(self._run_command(command, trigger='run'))
        return action_ids

    def rerun(self, action_id):
        command = self.history.get_command(action_id)
        print(f'rerun request for action #{action_id}')
        return self._run_command(command, trigger=f'rerun_of_{action_id}')


if __name__ == '__main__':
    user = UserData(
        user_id=101,
        user_name='Andy Lin',
        email='andy.lin@example.com',
    )

    database = FakeDatabase()
    email_service = EmailService()
    invoker = CommandInvoker()

    save_command = SaveUserCommand(database, user)
    email_command = SendEmailCommand(email_service, user)

    print_section('Queue Commands')
    invoker.add_to_queue(save_command)
    invoker.add_to_queue(email_command)

    print_section('Run All Commands')
    action_ids = invoker.run_all()
    email_action = action_ids[1]

    print_section('Rerun Commands From History')
    invoker.rerun(email_action)

    invoker.history.display()
    print_section('Fake Database')
    print(database._users)
