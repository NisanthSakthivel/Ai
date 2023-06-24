   elif 'what time is it' in query:
         now = datetime.datetime.now()
         print("It's " + now.strftime("%H:%M:%S"))
