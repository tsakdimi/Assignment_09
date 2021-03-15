#------------------------------------------#
# Title: Data Classes
# Desc: A Module for Data Classes
# Change Log: DTSakalos, 2021-Mar-14, Added code to complete program
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Modified to add Track class, added methods to CD class to handle tracks
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself')


class Track():
    """Stores Data about a single Track:
    properties:
        position: (int) with Track position on CD / Album
        title: (str) with Track title
        length: (str) with length / playtime of Track
    methods:
        __str__(): -> (str) with position, title and length of a track formated for screen display
        get_record() -> (str) with position, title and length of a track formated for saving to file
    """

    ###    Constructor    ###
    def __init__(self, p, t, l):
        #Attributes#
        self.__position = p
        self.__title = t
        self.__length = l

    ###    Properties    ###
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, p):
        if type(p) == int:
            if p < 1:
                raise Exception('Track position must be greater than 0')
            self.__position = p
        else:
            raise Exception('Track position must be an integer')

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, t):
        if type(t) == str:
            self.__title = t
        else:
            raise Exception('Track title must be a string')

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, l):
        if type(l) == str:
            self.__length = l
        else:
            raise Exception('Track length must be a string')

    ###    Methods    ###
    def __str__(self) -> str:
        """Returns Track details as formatted string"""
        return '{}. {} ({})'.format(self.position, self.title, self.length)

    def get_record(self) -> str:
        """Returns: Track record formatted for saving to file"""
        return '{},{},{}\n'.format(self.position, self.title, self.length)


class CD:
    """Stores data about a CD / Album:
    properties:
        cd_id: (int) with CD  / Album ID
        cd_title: (string) with the title of the CD / Album
        cd_artist: (string) with the artist of the CD / Album
        cd_tracks: (list) with track objects of the CD / Album
    methods:
        __str__: -> (string) of a CD album formatted as we want
        get_record() -> (string) CD record formatted for saving to file
        add_track(object) Track object to be added to CD / Album. -> None
        rmv_track(int) Removes the track identified by track_id from Album -> None
        sort(list) -> tmp_cd A list containing the sorted cd tuples
        sort_tracks(): Sorts the tracks using Track.position. Fills blanks with None
        get_tracks() -> (string) formatted string of tracks
        get_long_record() -> (string) Formatted information about album and its tracks
    """

    ###    Constructor    ###
    def __init__(self, cd_id: int, cd_title: str, cd_artist: str) -> None:
        """Set ID, Title and Artist of a new CD Object"""
        ###    Attributes    ###
        try:
            self.__cd_id = int(cd_id)
            self.__cd_title = str(cd_title)
            self.__cd_artist = str(cd_artist)
            self.__tracks = []
        except Exception as e:
            raise Exception('Error setting initial values:\n' + str(e))

    ###    Properties    ###
    # CD ID
    @property
    def cd_id(self):
        return self.__cd_id

    @cd_id.setter
    def cd_id(self, value):
        try:
            self.__cd_id = int(value)
        except Exception:
            raise Exception('ID needs to be Integer')

    # CD title
    @property
    def cd_title(self):
        return self.__cd_title

    @cd_title.setter
    def cd_title(self, value):
        try:
            self.__cd_title = str(value)
        except Exception:
            raise Exception('Title needs to be String!')

    # CD artist
    @property
    def cd_artist(self):
        return self.__cd_artist

    @cd_artist.setter
    def cd_artist(self, value):
        try:
            self.__cd_artist = str(value)
        except Exception:
            raise Exception('Artist needs to be String!')

    # CD tracks
    @property
    def cd_tracks(self):
        """Returns: Tracks details as formatted string"""
        return self.__tracks
    
    @cd_tracks.setter
    def cd_tracks(self, value):
        try:
            self.__cd_tracks = list
        except Exception:
            raise Exception('Track needs to be list!')
    

    ###    Methods    ###
    def __str__(self):
        """Returns: CD details as formatted string"""
        return '{}\t{} (by: {})'.format(self.cd_id, self.cd_title, self.cd_artist)

    def get_record(self):
        """Returns: CD record formatted for saving to file"""
        return '{},{},{}\n'.format(self.cd_id, self.cd_title, self.cd_artist)

    def add_track(self, track: Track) -> None:
        """Adds a track to the CD / Album
        Args:
            track (Track): Track object to be added to CD / Album.
        Returns:
            None.
        """

        self.__tracks.append(track)
        self.__sort_tracks()

    def rmv_track(self, track_id: int) -> None:
        """Removes the track identified by track_id from Album
        Args:
            track_id (int): ID of track to be removed.
        Returns:
            None.
        """

        del self.__tracks[track_id - 1]
        self.__sort_tracks()

    @staticmethod
    def sort(table):
        """Sorts the tracks using cd.cd_id. Fills blanks with None
        Args:
            table (list of tuples): A 2D list of tuples containing the CD album data
        Returns:
            tmp_cd (list): A list containing the sorted cd tuples
        
        """
        n = len(table)
        for cd in table:
            if (cd is not None) and (n < cd.cd_id):
                n = cd.cd_id
        tmp_cd = [None] * n
        for cd in table:
            if cd is not None:
                tmp_cd[cd.cd_id - 1] = cd
        return tmp_cd


    def __sort_tracks(self):
        """Sorts the tracks using Track.position. Fills blanks with None"""
        n = len(self.__tracks)
        for track in self.__tracks:
            if (track is not None) and (n < track.position):
                n = track.position
        tmp_tracks = [None] * n
        for track in self.__tracks:
            if track is not None:
                tmp_tracks[track.position - 1] = track
        self.__tracks = tmp_tracks

    def get_tracks(self) -> str:
        """Returns a string list of the tracks saved for the Album
        Raises:
            Exception: If no tracks are saved with album.
        Returns:
            result (string):formatted string of tracks.
        """

        self.__sort_tracks()
        if len(self.__tracks) < 1:
            raise Exception('No tracks saved for this Album')
        result = ''
        for track in self.__tracks:
            if track is None:
                result += 'No Information for this track\n'
            else:
                result += str(track) + '\n'
        return result

    def get_long_record(self) -> str:
        """gets a formatted long record of the Album: Album information plus track details
        Returns:
            result (string): Formatted information about album and its tracks.
        """

        result = self.get_record() + '\n'
        result += self.get_tracks() + '\n'
        return result




