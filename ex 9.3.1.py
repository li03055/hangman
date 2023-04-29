def my_mp3_playlist(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines if line.strip()]        # remove empty lines
    num_songs = len(lines)
    song_names = [line.split(";")[0] for line in lines]
    longest_song = max(lines, key=lambda x: int(x.split(";")[2].replace(":", "")))
    longest_song_name = longest_song.split(";")[0]
    performers = [line.split(";")[1] for line in lines]
    most_common_performer = max(set(performers), key=performers.count)
    return (longest_song_name, num_songs, most_common_performer)

def main():
    print(my_mp3_playlist("c:\songs.txt"))

if __name__ == '__main__':
    main()