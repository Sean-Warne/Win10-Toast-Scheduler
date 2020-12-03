import toasty

notifs = [
    toasty.Notification("Time to stretch!", "Stretch your neck for 30 seconds", None, 3, 36),
    toasty.Notification("Look away!", "Look away from the screen for 30 seconds", None, 2, 12)
]
notif_threads = {}

# loop through notifications and create a thread for each
i = 0
for notif in notifs:
    notif_i = f"notif_thread_{i}"
    print(notif_i)
    notif_threads[notif_i] = toasty.NotificationThread(notif)
    notif_threads[notif_i].start()
    i += 1