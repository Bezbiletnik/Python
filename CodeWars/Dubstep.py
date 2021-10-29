'''
    My solution:
'''


def song_decoder(song):
    new_song = ' '.join(song.split('WUB')).strip(); return ' '.join(new_song.split())


print(song_decoder("AWUBBWUBC"))
print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))
print(song_decoder("WUBAWUBBWUBCWUB"))


'''
    Best Practices:


        def song_decoder(song):
        return " ".join(song.replace('WUB', ' ').split())
        
'''