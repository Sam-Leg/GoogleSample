"""A video player class."""

from .video_library import VideoLibrary
from random import randint
global videoPlaying
videoPlaying = False
global titlePlaying
titlePlaying = True
global videoPaused
videoPaused = False
class VideoPlayer:

    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        


    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        videoLibrary = VideoLibrary()
        videoList = videoLibrary.get_all_videos()
        finalData = []
        print("Here's a list of all available videos:")
        for i in range(len(videoList)):
            title = (videoList[i]).title
            url = (videoList[i]).video_id
            tags = ""
            for j in range(len(videoList[i].tags)):
                
                tags = tags+(videoList[i].tags)[j]
                if(j == 0):
                    tags = tags + " "
            data = title +" (" +url +") ["+ tags +"]"
            finalData.append(data)
        finalData.sort()
        for i in range(len(finalData)):
            print(finalData[i])

        
        #print("show_all_videos needs implementation")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        global videoPlaying
        global titlePlaying
        global videoPaused
        videoLibrary = VideoLibrary()
        try:
            title = (videoLibrary.get_video(video_id)).title
            if (videoPlaying):
                
                VideoPlayer.stop_video(self)
                videoPlaying = False
                VideoPlayer.play_video(self,video_id)
                
            #print("play_video needs implementation")
            else:
                print("Playing video: "+title)
                titlePlaying = title
                videoPlaying = True
                videoPaused = False
        except:
            print("Cannot play video: Video does not exist")
            

    def stop_video(self):
        """Stops the current video."""
        global videoPlaying
        global titlePlaying
        global videoPaused
        
        if (videoPlaying):
            print("Stopping video: "+titlePlaying)

            #print("stop_video needs implementation")
        else:
            print("Cannot stop video: No video is currently playing")
        videoPlaying = False
        videoPaused = False
    def play_random_video(self):
        """Plays a random video from the video library."""
        videoLibrary = VideoLibrary()
        videoList = videoLibrary.get_all_videos()
        randomNumber = randint(0,len(videoList)-1)
        randomVideo = videoList[randomNumber]
        randomID = randomVideo.video_id
        VideoPlayer.play_video(self,randomID)
        #print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""
        global videoPaused
        global titlePlaying
        global videoPlaying
        if (videoPaused):
            print("Video already paused: "+titlePlaying)
        elif(not(videoPlaying)):
            print("Cannot pause video: No video is currently playing")
        else:
            videoPaused = True
            print("Pausing video: " + titlePlaying)

        #print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""
        global videoPaused
        global titlePlaying
        global videoPlaying
        
        if(not(videoPlaying)):
            print("Cannot continue video: No video is currently playing")
        elif (videoPaused):
            print("Continuing video: "+titlePlaying)
            videoPaused = False
        else:
            print("Cannot continue video: Video is not paused")
        

        #print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""
        if (not(videoPlaying)):
            print("No video is currently playing")
        else:
            
            videolibrary = VideoLibrary()
            videoList = videolibrary.get_all_videos()
            for i in range(0,len(videoList)-1):
                if ((videoList[i]).title == titlePlaying):
                    ID = videoList[i].video_id
                    tags = ""
                    for j in range(len(videoList[i].tags)):
                        tags = tags+(videoList[i].tags)[j]+" "
                    
            
            data = "Currently playing: "+titlePlaying+" "+ ID+ " ["+tags+"\b]"
            if (videoPaused):
                data = data + " - PAUSED"
            print (data)

            #Currently playing: Amazing Cats (amazing_cats_video_id) [#cat #animal]
        #print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

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
