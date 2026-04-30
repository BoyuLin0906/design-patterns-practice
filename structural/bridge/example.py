from __future__ import annotations

from abc import ABC, abstractmethod


def print_section(title):
    print(f'\n=== {title} ===')


class MessageSender(ABC):
    @abstractmethod
    def send(self, recipient, subject, body):
        raise NotImplementedError('Subclasses must implement send().')


class EmailSender(MessageSender):
    def send(self, recipient, subject, body):
        print(f'Email sent to {recipient}')
        print(f'Subject: {subject}')
        print(f'Body: {body}')


class SlackSender(MessageSender):
    def send(self, recipient, subject, body):
        print(f'Slack message sent to #{recipient}')
        print(f'Headline: {subject}')
        print(f'Message: {body}')


class NotificationMessage(ABC):
    def __init__(self, sender: MessageSender):
        self.sender: MessageSender = sender

    @abstractmethod
    def deliver(self, recipient, topic, details):
        raise NotImplementedError('Subclasses must implement deliver().')


class AlertNotification(NotificationMessage):
    def deliver(self, recipient, topic, details):
        subject = f'ALERT: {topic}'
        body = f'Please investigate now. {details}'
        self.sender.send(recipient, subject, body)


class ReminderNotification(NotificationMessage):
    def deliver(self, recipient, topic, details):
        subject = f'Reminder: {topic}'
        body = f'Friendly reminder. {details}'
        self.sender.send(recipient, subject, body)


if __name__ == '__main__':
    email_sender = EmailSender()
    slack_sender = SlackSender()

    urgent_email_alert = AlertNotification(email_sender)
    team_slack_alert = AlertNotification(slack_sender)
    customer_email_reminder = ReminderNotification(email_sender)
    team_slack_reminder = ReminderNotification(slack_sender)

    print_section('Alert Through Email')
    urgent_email_alert.deliver(
        recipient='ops@example.com',
        topic='Payment service is down',
        details='The checkout API has returned errors for 5 minutes.',
    )

    print_section('Alert Through Slack')
    team_slack_alert.deliver(
        recipient='incident-room',
        topic='Build pipeline failed',
        details='Deployment to production is blocked until tests pass.',
    )

    print_section('Reminder Through Email')
    customer_email_reminder.deliver(
        recipient='andy@example.com',
        topic='Submit expense report',
        details='Please send it before Friday at 5 PM.',
    )

    print_section('Reminder Through Slack')
    team_slack_reminder.deliver(
        recipient='team-ops',
        topic='Rotate on-call handoff',
        details='Update the checklist before the handoff meeting.',
    )
