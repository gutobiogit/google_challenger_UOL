"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.playlist = {}
        self.play_list = Playlist()


    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        all_videos = self._video_library.get_all_videos()
        videos_dic = {}
        """Returns all videos."""
        print("Here's a list of all available videos:")
        for video in all_videos:
            videos_dic[video.title] = (video.video_id,*video.tags)
            sorted_videos = sorted(videos_dic.items())
        for sorted_video in sorted_videos:
            print (sorted_video[0],'('+sorted_video[1][0]+')',end = '')
            print(" [",end = '')
            print(*sorted_video[1][1:],end = '')
            print("]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        has_video = False
        all_videos = self._video_library.get_all_videos()
        for video in all_videos:
            if video.playing() == True:
                playing_video = video.title
                has_video = True
                video.playing("ON")
            if video.video_id == video_id:
                video_name = video.title
                video.playing("OFF")
            if video.paused() == True:
                video.paused("ON")
        if not 'video_name' in locals():
            print('Cannot play video: Video does not exist')
            return
        else:
            if has_video:
                print ("Stopping video: " + playing_video)
            print("Playing video: " + video_name)

    def stop_video(self):
        """Stops the current video."""
        has_video = False
        all_videos = self._video_library.get_all_videos()
        for video in all_videos:
            if video.playing() == True:
                playing_video = video.title
                print('Stopping video:',playing_video)
                video.playing("OFF")
                return True
        print('Cannot stop video: No video is currently playing')

    def play_random_video(self):
        """Plays a random video from the video library."""
        all_videos = self._video_library.get_all_videos()
        for video in all_videos:
            if video.playing() == True:
                playing_video = video.title
                print('Stopping video:',playing_video)
                video.playing("OFF")
            
        self.play_video(all_videos[random.randint(0,len(all_videos)-1)].video_id)
            
    def pause_video(self):
        """Pauses the current video."""
        has_video = False
        all_videos = self._video_library.get_all_videos()
        for video in all_videos:
            playing_video = video.title
            if video.playing() == True:
                has_video==True
                if video.paused() == True: 
                    print('Video already paused:',playing_video)
                    return
                else :    
                    print('Pausing video:',playing_video)
                    video.paused("OFF")
                    return
        if has_video == False:
            print('Cannot pause video: No video is currently playing')
        
    def continue_video(self):
        """Resumes playing the current video."""
        has_video = False
        all_videos = self._video_library.get_all_videos()
        for video in all_videos:
            playing_video = video.title
            if video.playing() == True:
                has_video=True
                if video.paused() == False:
                    print('Cannot continue video: Video is not paused')
                    return
                else:
                    print('Continuing video:',playing_video)
                    video.paused("ON")
                    return
        if has_video == False:
            print('Cannot continue video: No video is currently playing')
            
    def show_playing(self):
        """Displays video currently playing."""
        has_video = False
        all_videos = self._video_library.get_all_videos()
        for video in all_videos:
            playing_video = video.title
            if video.playing() == True:
                has_video=True
                print ("Currently playing:",video.title,'('+video.video_id+')',end = '')
                print(" [",end = '')
                print(*video.tags,end = '')
                if video.paused() == True:
                    print("] - PAUSED")
                else:
                    print("]")
        if has_video == False:
            print('No video is currently playing')
        #print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.upper() in map(str.upper,self.playlist):
            print('Cannot create playlist: A playlist with the same name already exists')
        else:
            self.play_list.create_play_list(playlist_name)
            print('Successfully created new playlist:', playlist_name)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        has_video = False
        all_videos = self._video_library.get_all_videos()
        for video in all_videos:
            if video.video_id == video_id:

                has_video = True
                print(f'Added video to {playlist_name}: {video.title}')
                self.play_list.add_play_list(playlist_name,video.title)



        if has_video == False:
            print(f'Cannot add video to {playlist_name}: Video does not exist')
            pass

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
