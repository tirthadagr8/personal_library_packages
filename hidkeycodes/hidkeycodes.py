class HIDKeyCodes:
    def __init__(self):
        super(HIDKeyCodes).__init__()
        
        # Modifier Keys
        self.KEY_LEFT_CTRL = 0x01
        self.KEY_LEFT_SHIFT = 0x02
        self.KEY_LEFT_ALT = 0x04
        self.KEY_LEFT_GUI = 0x08  # Windows/Command key
        self.KEY_RIGHT_CTRL = 0x10
        self.KEY_RIGHT_SHIFT = 0x20
        self.KEY_RIGHT_ALT = 0x40
        self.KEY_RIGHT_GUI = 0x80

        # Alphanumeric Keys
        self.KEY_A = 0x04
        self.KEY_B = 0x05
        self.KEY_C = 0x06
        self.KEY_D = 0x07
        self.KEY_E = 0x08
        self.KEY_F = 0x09
        self.KEY_G = 0x0A
        self.KEY_H = 0x0B
        self.KEY_I = 0x0C
        self.KEY_J = 0x0D
        self.KEY_K = 0x0E
        self.KEY_L = 0x0F
        self.KEY_M = 0x10
        self.KEY_N = 0x11
        self.KEY_O = 0x12
        self.KEY_P = 0x13
        self.KEY_Q = 0x14
        self.KEY_R = 0x15
        self.KEY_S = 0x16
        self.KEY_T = 0x17
        self.KEY_U = 0x18
        self.KEY_V = 0x19
        self.KEY_W = 0x1A
        self.KEY_X = 0x1B
        self.KEY_Y = 0x1C
        self.KEY_Z = 0x1D
        self.KEY_1 = 0x1E
        self.KEY_2 = 0x1F
        self.KEY_3 = 0x20
        self.KEY_4 = 0x21
        self.KEY_5 = 0x22
        self.KEY_6 = 0x23
        self.KEY_7 = 0x24
        self.KEY_8 = 0x25
        self.KEY_9 = 0x26
        self.KEY_0 = 0x27

        # Control Keys
        self.KEY_ENTER = 0x28
        self.KEY_ESCAPE = 0x29
        self.KEY_BACKSPACE = 0x2A
        self.KEY_TAB = 0x2B
        self.KEY_SPACE = 0x2C

        # Symbols
        self.KEY_MINUS = 0x2D      # -
        self.KEY_EQUAL = 0x2E      # =
        self.KEY_LEFT_BRACKET = 0x2F  # [
        self.KEY_RIGHT_BRACKET = 0x30  # ]
        self.KEY_BACKSLASH = 0x31  # \
        self.KEY_SEMICOLON = 0x33  # ;
        self.KEY_APOSTROPHE = 0x34  # '
        self.KEY_GRAVE = 0x35      # `
        self.KEY_COMMA = 0x36      # ,
        self.KEY_PERIOD = 0x37     # .
        self.KEY_SLASH = 0x38      # /
        self.KEY_MOD=0xC4          # %
        self.KEY_BAR=0xC9          # |

        # Function Keys
        self.KEY_F1 = 0x3A
        self.KEY_F2 = 0x3B
        self.KEY_F3 = 0x3C
        self.KEY_F4 = 0x3D
        self.KEY_F5 = 0x3E
        self.KEY_F6 = 0x3F
        self.KEY_F7 = 0x40
        self.KEY_F8 = 0x41
        self.KEY_F9 = 0x42
        self.KEY_F10 = 0x43
        self.KEY_F11 = 0x44
        self.KEY_F12 = 0x45

        # Lock Keys
        self.KEY_PRINT_SCREEN = 0x46
        self.KEY_SCROLL_LOCK = 0x47
        self.KEY_PAUSE = 0x48
        self.KEY_INSERT = 0x49
        self.KEY_HOME = 0x4A
        self.KEY_PAGE_UP = 0x4B
        self.KEY_DELETE = 0x4C
        self.KEY_END = 0x4D
        self.KEY_PAGE_DOWN = 0x4E
        self.KEY_RIGHT_ARROW = 0x4F
        self.KEY_LEFT_ARROW = 0x50
        self.KEY_DOWN_ARROW = 0x51
        self.KEY_UP_ARROW = 0x52

        # Keypad Keys
        self.KEYPAD_NUM_LOCK = 0x53
        self.KEYPAD_DIVIDE = 0x54
        self.KEYPAD_MULTIPLY = 0x55
        self.KEYPAD_SUBTRACT = 0x56
        self.KEYPAD_ADD = 0x57
        self.KEYPAD_ENTER = 0x58
        self.KEYPAD_1 = 0x59
        self.KEYPAD_2 = 0x5A
        self.KEYPAD_3 = 0x5B
        self.KEYPAD_4 = 0x5C
        self.KEYPAD_5 = 0x5D
        self.KEYPAD_6 = 0x5E
        self.KEYPAD_7 = 0x5F
        self.KEYPAD_8 = 0x60
        self.KEYPAD_9 = 0x61
        self.KEYPAD_0 = 0x62
        self.KEYPAD_PERIOD = 0x63

        # Media Keys (if supported)
        self.KEY_VOLUME_UP = 0x80
        self.KEY_VOLUME_DOWN = 0x81
        self.KEY_MUTE = 0x7F
        self.KEY_MEDIA_PLAY_PAUSE = 0xE8
        self.KEY_MEDIA_STOP = 0xE9
        self.KEY_MEDIA_NEXT_TRACK = 0xEA
        self.KEY_MEDIA_PREV_TRACK = 0xEB
