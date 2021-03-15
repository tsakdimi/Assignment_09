#------------------------------------------#
# Title: Processing Classes
# Desc: A Module for processing Classes
# Change Log: DTSakalos, 2021-Mar-14, Added code to complete program
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as DC


class DataProcessor:
    """Processing the data in the application"""
    @staticmethod
    def add_CD(CDInfo, table):
        """function to add CD info in CDinfo to the inventory table.
        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist) to be added to inventory.
            table (list of CD Objects): 2D data structure (list of CD Objects) that holds the data during runtime.
        Returns:
            None.
        """

        cdId, title, artist = CDInfo
        try:
            cdId = int(cdId)
        except:
            raise Exception('ID must be an Integer!')
        row = DC.CD(cdId, title, artist)
        table.append(row)
        DC.CD.sort(table)

    @staticmethod
    def select_cd(table: list, cd_idx: int) -> DC.CD:
        """selects a CD object out of table that has the ID cd_idx
        Args:
            table (list): Inventory list of CD objects.
            cd_idx (int): id of CD object to return
        Raises:
            Exception: If id is not in list.
        Returns:
            cd (DC.CD): CD object that matches cd_idx
        """

        try:
            cd_idx = int(cd_idx)
        except ValueError as e:
            print('ID must be an integer')
            print(e.__doc__)
        for cd in table:
            if cd.cd_id == cd_idx:
                return cd
        raise Exception('CD does not exist')


    @staticmethod
    def add_track(track_info: tuple, cd: DC.CD) -> None:
        """adds a Track object with attributes in track_info to cd
        Args:
            track_info (tuple): Tuple containing track info (position, title, Length).
            cd (DC.CD): cd object the tarck gets added to.
        Raises:
            Exception: DESCraised in case position is not an integer.
        Returns:
            None.
        """

        pos, ttl, lng = track_info
        try:
            pos = int(pos)
        except:
            raise Exception('Position must be an integer')
        track = DC.Track(pos, ttl, lng)
        cd.add_track(track)

