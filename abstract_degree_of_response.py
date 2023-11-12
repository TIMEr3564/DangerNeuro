from audio_realisator import play_sound


class Action:
    @staticmethod
    def low_lvl_audio():
        play_sound()

    @staticmethod
    def low_lvl_light():
        pass

    @staticmethod
    def avg_lvl_audio():
        play_sound()
        play_sound()

    @staticmethod
    def avg_lvl_light():
        pass

    @staticmethod
    def max_audio():
        play_sound()
        play_sound()
        play_sound()
        play_sound()

    @staticmethod
    def max_light():
        pass


class Resposer:
    def __init__(self, percent):
        pass

    @staticmethod
    def low_lvl_danger():
        Action.low_lvl_audio()
        Action.low_lvl_light()
        pass

    @staticmethod
    def avg_lvl_danger():
        Action.avg_lvl_audio()
        Action.avg_lvl_light()
        pass

    @staticmethod
    def high_lvl_danger():
        Action.max_audio()
        Action.max_light()
        pass
