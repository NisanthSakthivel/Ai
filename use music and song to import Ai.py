 elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
           
            music_dir = "...." # music_dir = "G:\\Song"
            songs = os.listdir(music_dir)
            print(songs)   
            random = os.startfile(os.path.join(music_dir, songs[1]))