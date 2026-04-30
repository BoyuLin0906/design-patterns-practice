from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


def print_section(title):
    print(f'\n=== {title} ===')


@dataclass
class Notification:
    recipient: str
    subject: str
    message: str


class NotificationChannel(ABC):
    @abstractmethod
    def send(self, notification: Notification):
        raise NotImplementedError('Subclasses must implement send().')


class EmailNotifier:
    def send_email(self, email_address, subject, body):
        print(f'Email sent to {email_address}')
        print(f'Subject: {subject}')
        print(f'Body: {body}')


class SlackNotifier:
    def post_message(self, channel_name, text):
        print(f'Slack message sent to #{channel_name}')
        print(f'Message: {text}')


class AppNotifier:
    def push(self, user_id, title, content):
        print(f'App notification sent to user {user_id}')
        print(f'Title: {title}')
        print(f'Content: {content}')


class EmailAdapter(NotificationChannel):
    def __init__(self, email_notifier: EmailNotifier):
        self.email_notifier: EmailNotifier = email_notifier

    def send(self, notification: Notification):
        self.email_notifier.send_email(
            email_address=notification.recipient,
            subject=notification.subject,
            body=notification.message,
        )


class SlackAdapter(NotificationChannel):
    def __init__(self, slack_notifier: SlackNotifier):
        self.slack_notifier: SlackNotifier = slack_notifier

    def send(self, notification: Notification):
        text = f'{notification.subject}: {notification.message}'
        self.slack_notifier.post_message(
            channel_name=notification.recipient,
            text=text,
        )


class AppAdapter(NotificationChannel):
    def __init__(self, app_notifier: AppNotifier):
        self.app_notifier: AppNotifier = app_notifier

    def send(self, notification: Notification):
        self.app_notifier.push(
            user_id=notification.recipient,
            title=notification.subject,
            content=notification.message,
        )


# Client code depends only on the target interface.
def deliver_notification(channel: NotificationChannel, notification: Notification):
    channel.send(notification)


if __name__ == '__main__':
    email_channel = EmailAdapter(EmailNotifier())
    slack_channel = SlackAdapter(SlackNotifier())
    app_channel = AppAdapter(AppNotifier())

    print_section('Email Adapter')
    deliver_notification(
        email_channel,
        Notification(
            recipient='andy@example.com',
            subject='Welcome',
            message='Your account has been created.',
        ),
    )

    print_section('Slack Adapter')
    deliver_notification(
        slack_channel,
        Notification(
            recipient='team-updates',
            subject='Deploy',
            message='Version 1.2 was deployed successfully.',
        ),
    )

    print_section('App Adapter')
    deliver_notification(
        app_channel,
        Notification(
            recipient='user-501',
            subject='Reminder',
            message='Your appointment starts in 10 minutes.',
        ),
    )
