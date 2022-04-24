class Settings:
    """ GuitarTuner global app configuration """

    COMPILED_APP_MODE = False

    """ general settings """
    APP_NAME = "GuitarTuner"
    VERSION = "0.1"
    AUTHOR = ""
    YEAR = ""


    USER_SETTINGS_PATH = "/assets/user_settings/user_settings.json"

    ABOUT_TEXT = "{} Version {}  © {} {}".format(APP_NAME, VERSION, YEAR, AUTHOR)
    CF_BUNDLE_IDENTIFIER = "com.{}.{}".format(AUTHOR, APP_NAME)

    WIDTH = 450  # window size when starting the app
    HEIGHT = 440

    MAX_WIDTH = 600  # max window size
    MAX_HEIGHT = 500

    FPS = 60  # canvas update rate
    CANVAS_SIZE = 300  # size of the audio-display

    NEEDLE_BUFFER_LENGTH = 30
    HITS_TILL_NOTE_NUMBER_UPDATE = 15
