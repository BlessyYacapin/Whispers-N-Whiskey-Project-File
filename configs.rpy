init python:
    if "foreground" not in config.layers:
        # Find where 'screens' is and insert 'foreground' before it
        index = config.layers.index("screens")
        config.layers.insert(index, "foreground")

init python:
    def get_save_check_point_id():
        while True:
            i = renpy.random.randint(0, 100000)
            if not renpy.can_load("checkpoint_"+str(i)):
                break
        return "checkpoint_"+str(i)

default checkpoint = get_save_check_point_id()