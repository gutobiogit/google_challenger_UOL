"""A video class."""

from typing import Sequence


class Video:
    """A class used to represent a Video."""

    def __init__(self, video_title: str, video_id: str, video_tags: Sequence[str]):
        """Video constructor."""
        self._title = video_title
        self._video_id = video_id
        self.set_position = False
        self.set_pause = False

        # Turn the tags into a tuple here so it's unmodifiable,
        # in case the caller changes the 'video_tags' they passed to us
        self._tags = tuple(video_tags)

    @property
    def title(self) -> str:
        """Returns the title of a video."""
        return self._title

    @property
    def video_id(self) -> str:
        """Returns the video id of a video."""
        return self._video_id

    @property
    def tags(self) -> Sequence[str]:
        """Returns the list of tags of a video."""
        return self._tags
    

    def playing(self,set_position = "Empty"):
        """Return if is playing"""
        if set_position == 'Empty':
            return self.set_position
        else:
            self.set_position = not self.set_position

    def paused(self, paused = "Empty"):
        """Return if is paused"""
        if paused == 'Empty':
            return self.set_pause
        else:
            self.set_pause = not self.set_pause
        


