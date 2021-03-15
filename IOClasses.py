#------------------------------------------#
# Title: IO Classes
# Desc: A Module for IO Classes
# Change Log: DTSakalos, 2021-Mar-14, Added code to complete program
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself')

import DataClasses as DC
import ProcessingClasses as PC


class FileIO:
    """Processes data to and from file:
    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)
    """

    ###    Methods    ###
    @staticmethod
    def save_inventory(file_name: list, lst_Inventory: list) -> None:
        """
        Args:
            file_name (list): list of file names [CD Inventory, Track Inventory] that hold the data.
            lst_Inventory (list): list of CD objects.
        Returns:
            None.
        """

        file_name_CD = file_name[0]
        file_name_Track = file_name[1]
        try:
            with open(file_name_CD, 'w') as file:
                for disc in lst_Inventory:
                    file.write(disc.get_record())
            with open(file_name_Track, 'w') as file:
                for disc in lst_Inventory:
                    for track in disc.cd_tracks:
                        if track is not None:
                            file.write('{},{}'.format(disc.cd_id, track.get_record()))
        except Exception as e:
            print('There was a general error!', e, e.__doc__, type(e), sep='\n')

    @staticmethod
    def load_inventory(file_name: list) -> list:
        """
        Args:
            file_name (list): list of file names [CD Inventory, Track Inventory] that hold the data.
        Returns:
            list_Inventory (list): list of CD objects.
        """

        file_name_CD = file_name[0]
        file_name_Track = file_name[1]
        lst_Inventory = []
        try:
            with open(file_name_CD, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    row = DC.CD(data[0], data[1], data[2])
                    lst_Inventory.append(row)
            with open(file_name_Track, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    row = DC.Track(int(data[1]), data[2], data[3])
                    cd = PC.DataProcessor.select_cd(lst_Inventory, int(data[0]))
                    cd.add_track(row)
        except Exception as e:
            if type(e) == FileNotFoundError:
                print('Found no file to load. Add Album and/or tracks and save to create file')
            else:
                print('There was a general error!', e, e.__doc__, type(e), sep='\n')
        return lst_Inventory


class ScreenIO:
    """Handling Input / Output
    methods:
        print_menu: Prints menu for user -> None
        menu_choice: -> (string) of the choice the user selects
        print_CD_menu: (string) Prints a list of Objects -> None
        menu_CD_choice: -> (string) of the choice the user selects
        show_inventory (table): (string) Prints a list of Objects -> None
        show_tracks (cd): (string) Prints a list of Objects -> None
        get_CD_info (table)-> (object) containing cdId, cdTitle, cdArtist
        get_track_info (cd): -> (object) ocontaining trkId, trkTitle, trkLength

"""
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user
        Args:
            None.
        Returns:
            None.
        """

        print('Main Menu\n\n[l] load Inventory from file\n[a] Add CD / Album\n[d] Display Current Inventory')
        print('[c] Choose CD / Album\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection
        Args:
            None.
        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, d, c, s or x
        """

        choice = ' '
        while choice not in ['l', 'a', 'd', 'c', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, d, c, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def print_CD_menu():
        """Displays a sub menu of choices for CD / Album to the user
        Args:
            None.
        Returns:
            None.
        """

        print('CD Sub Menu\n\n[a] Add track\n[d] Display cd / Album details\n[r] Remove track\n[x] exit to Main Menu')

    @staticmethod
    def menu_CD_choice():
        """Gets user input for CD sub menu selection
        Args:
            None.
        Returns:
            choice (string): a lower case sting of the users input out of the choices a, d, r or x
        """

        choice = ' '
        while choice not in ['a', 'd', 'r', 'x']:
            choice = input('Which operation would you like to perform? [a, d, r or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table
        Args:
            table (list of objects): 2D data structure (list of objects) that holds the data during runtime.
        Returns:
            None.
        """

        
        table = DC.CD.sort(table)
        # for cd in table:
        #     if cd is None:
        #         print('None')
        #         continue
        #     print(cd.cd_id)
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for cd in table:
            if cd is None:
                print('No information for this Album')
                continue
            print(cd)
        print('======================================')

    @staticmethod
    def show_tracks(cd):
        """Displays the Tracks on a CD / Album
        Args:
            cd (CD): CD object.
        Returns:
            None.
        """

        print('====== Current CD / Album: ======')
        print(cd)
        print('=================================')
        print(cd.get_tracks())
        print('=================================')

    @staticmethod
    def get_CD_info(table):
        """function to request CD information from User to add CD to inventory
        Returns:
            cdId (string): Holds the ID of the CD dataset.
            cdTitle (string): Holds the title of the CD.
            cdArtist (string): Holds the artist of the CD.
        """

        while True:
            try:
                cdId = int(input('Enter ID: ').strip())
            except ValueError:
                print('Invalid Input! Try again.')
                continue
            found = False
            for cd in table:
                if cd.cd_id == cdId:
                    print('Album with ID {} already exists. Choose another ID number'.format(cdId))
                    found = True
                    break
            if not found:
                break


        while True:
            try:
                cdTitle = input('What is the CD\'s title? ').strip()
                if cdTitle == '':
                    raise ValueError()
                break
            except ValueError:
                print('Invalid Input! Try again.')
        while True:
            try:
                cdArtist = input('What is the Artist\'s name? ').strip()
                if cdArtist == '':
                    raise ValueError()
                break
            except ValueError:
                print('Invalid Input! Try again.')
        return cdId, cdTitle, cdArtist

    @staticmethod
    def get_track_info(cd):
        """function to request Track information from User to add Track to CD / Album
        Returns:
            trkId (string): Holds the ID of the Track dataset.
            trkTitle (string): Holds the title of the Track.
            trkLength (string): Holds the length (time) of the Track.
        """

        while True:
            try:
                trkId = int(input('Enter Position on CD / Album: ').strip())
            except ValueError:
                print('Invalid Input! Try again.')
                continue
            found = False
            for track in cd.cd_tracks:
                if track is not None and track.position == trkId:
                    print('Track with ID {} already exists. Choose another ID number'.format(trkId))
                    found = True
                    break
            if not found:
                break

        while True:
            try:
                trkTitle = input('What is the Track\'s title? ').strip()
                if trkTitle == '':
                    raise ValueError()
                break
            except ValueError:
                print('Invalid Input! Try again.')
        while True:
            try:
                trkLength = input('What is the Track\'s length? ').strip()
                if trkLength == '':
                    raise ValueError()
                break
            except ValueError:
                print('Invalid Input! Try again.')
        return trkId, trkTitle, trkLength

