# from datetime import datetime, timedelta
# from Foundation import NSDate
# from EventKit import EKEventStore, EKEvent, EKAlarm, EKRecurrenceRule

# # Initialize the event store
# event_store = EKEventStore.alloc().init()

# # Request access to the calendar
# def request_access():
#     granted = False

#     def access_granted(grant, error):
#         nonlocal granted
#         granted = grant

#     event_store.requestAccessToEntityTypecompletion(EKEntityTypeEvent, access_granted)

#     # Wait for user to grant access
#     while granted is False:
#         pass

# request_access()

# # Create a new event
# event = EKEvent.eventWithEventStore_(event_store)

# # Set event details
# event.title = "Python Script Event"
# event.startDate = NSDate.dateWithTimeIntervalSinceNow_(3600)  # 1 hour from now
# event.endDate = NSDate.dateWithTimeIntervalSinceNow_(7200)    # 2 hours from now
# event.notes = "This event was created using a Python script."

# # Add an alarm to the event (reminder 15 minutes before)
# alarm = EKAlarm.alarmWithRelativeOffset_(-900)
# event.addAlarm_(alarm)

# # Specify the calendar to add the event to
# event.calendar = event_store.defaultCalendarForNewEvents()

# # Save the event
# error = None
# event_store.saveEvent_span_error_(event, EKSpanThisEvent, error)

# if error is None:
#     print("Event added to Calendar successfully!")
# else:
#     print("Failed to add event:", error)


from CalendarStore import CalCalendarStore

calendars = CalCalendarStore.defaultCalendarStore().calendars()

for calendar in calendars:
    print("")
    print("Name:", calendar._.title)
    print("UUID:", calendar._.uid)
    print("Type:", calendar._.type)
