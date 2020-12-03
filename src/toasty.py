from win10toasty import ToastNotifier
import time
from threading import Thread

class Notification:
    def __init__(self, title, message, icon_path, duration_in_seconds, interval_in_seconds):
        self.title = title
        self.msg = message
        self.icon_path = icon_path
        self.duration = duration_in_seconds
        self.interval = interval_in_seconds

    def set_title(self, title):
        self.title = title
    
    def get_title(self):
        return self.title

    def set_message(self, message):
        self.msg = message

    def get_message(self):
        return self.msg

    def set_icon_path(self, icon_path):
        self.icon_path = icon_path

    def get_icon_path(self):
        return self.icon_path

    def set_duration(self, duration):
        self.duration = duration

    def get_duration(self):
        return self.duration

    def set_interval(self, interval_in_seconds):
        self.interval = interval_in_seconds

    def get_interval(self):
        return self.interval

class NotificationThread(Thread):
    def __init__(self, notification):
        self.stopped = False
        self.notification = notification
        Thread.__init__(self)

    def run(self):
        while not self.stopped:
            self.send_notification()
            time.sleep(self.notification.get_interval())

    def send_notification(self):
        toaster = ToastNotifier()
        toaster.show_toast(self.notification.get_title(), self.notification.get_message(), self.notification.get_icon_path(), self.notification.get_duration(), threaded=True)

    def stop_thread(self):
        self.stopped = True