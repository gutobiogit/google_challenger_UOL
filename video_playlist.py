"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self):
        self.playlist_main={}

    def create_play_list(self,name):
        self.playlist_main[name]=()

    def add_play_list(self,name,_list):
        pass
        #self.playlist_main[name]+=_list

        
    
    def search_list(self,name,_list):
        if name.upper() in map(str.upper,self._list):
            return True
        else:
            return False

    



