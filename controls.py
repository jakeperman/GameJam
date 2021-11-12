# control object
class Control:
    def __init__(self):
        self.repeat_keys = []
        self.controls = []
        self.keypress_action = {}
        self.keypress_params = {}
        self.release_action = {}
        self.repeat_action = {}

    # update for keys pressed
    def update(self):
        if self.repeat_keys:
            for key in self.repeat_keys:
                # call function bound to key
                if self.keypress_params[key]:
                    self.keypress_action[key](self.keypress_params[key])
                else:
                    self.keypress_action[key]()
                pass

    # bind a key to a function
    def bind_key(self, key, on_press: object, params=None, on_release: object = None, repeat: bool = False, delay=0):
        # only bind the key if the on_press or on_release variables are objects (functions)
        if callable(on_press):
            self.keypress_action[key] = on_press
            self.keypress_params[key] = params
        if callable(on_release):
            self.release_action[key] = on_release
        # set whether to repeat action
        self.repeat_action[key] = repeat

    # activate on_press action for key
    def on_press(self, key):

        if key in list(self.keypress_action):
            if self.keypress_params[key]:

                self.keypress_action[key](self.keypress_params[key])  # pass through parameters if given
            else:
                self.keypress_action[key]()  # call function without parameters

        if self.repeat_action[key]:  # check if key action should be repeated as long as key is held down
            self.repeat_keys.append(key)

    # active on_release action for key
    def on_release(self, key):
        if key in list(self.release_action):
            self.release_action[key]()
        if self.repeat_action[key]:  # if key is repeated, remove from repeat list
            self.repeat_keys.remove(key)
