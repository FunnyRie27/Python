class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    volume_tracker = 0

    def __init__(self):
        """
        Method to define variables
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        """
        Method to toggle TV power status.
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self):
        """
        Method to toggle TV mute status.
        """
        if self.__status:
            if self.__muted:
                self.__volume = Television.volume_tracker
                self.__muted = False
            else:
                self.__muted = True
                Television.volume_tracker = self.__volume
                self.__volume = Television.MIN_VOLUME

    def channel_up(self):
        """
        Method to toggle channel station.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        """
        Method to toggle channel station.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        """
        Method to toggle volume level.
        """
        if self.__status:
            self.__muted = False
            self.__volume = Television.volume_tracker
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
                Television.volume_tracker = self.__volume
            else:
                self.__volume = Television.MIN_VOLUME

    def volume_down(self):
        """
        Method to toggle volume level.
        """
        if self.__status:
            self.__muted = False
            self.__volume = Television.volume_tracker
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
                Television.volume_tracker = self.__volume
            else:
                self.__volume = Television.MAX_VOLUME

    def __str__(self) -> str:
        """
        Method to show the tv status.
        :return: tv status
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
        
