from pytube import Playlist
import os


def download_playlist(playlist_url, save_path):
    playlist = Playlist(playlist_url)

    # Create a directory to save downloads if it doesn't exist
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Get the playlist title to create a folder with the same name
    # Replace "/" with "_" to avoid directory creation issues
    playlist_title = playlist.title.replace("/", "_")
    # Remove invalid characters for directory names
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in invalid_chars:
        playlist_title = playlist_title.replace(char, '')

    # Create a directory for the playlist
    playlist_folder_path = os.path.join(save_path, playlist_title)
    if not os.path.exists(playlist_folder_path):
        os.makedirs(playlist_folder_path)

    # Create a file to store the playlist information
    playlist_file = open(os.path.join(playlist_folder_path,
                         "mohamed.adel.txt"), "w", encoding="utf-8")
    playlist_file.write(f"my Github : https://github.com/bo0odda\n")
    playlist_file.write(f"my linkedin : www.linkedin.com/in/bo0odda\n")
    # Iterate through each video in the playlist
    for video in playlist.videos:
        # Get the stream with the highest resolution
        stream = video.streams.filter(progressive=True, file_extension="mp4").order_by(
            'resolution').desc().first()

        # Download the stream
        print(f"Downloading {video.title}...")
        stream.download(output_path=playlist_folder_path)
        print(f"{video.title} downloaded successfully!")

        # Write the video title and URL to the playlist file
        playlist_file.write(f"{video.title} - {video.watch_url}\n")

    # Close the playlist file
    playlist_file.close()


if __name__ == "__main__":
    # Example playlist URL
    playlist_url = ""

    # Path to save downloads
    save_path = "c:/"

    # Call the function to download the playlist
    download_playlist(playlist_url, save_path)
