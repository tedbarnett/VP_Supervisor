import unreal

def set_lumen_enabled(enable_lumen=True):
    setting_value = '1' if enable_lumen else '0'
    ini_path = unreal.Paths.combine([unreal.SystemLibrary.get_project_directory(), "Config/DefaultEngine.ini"])

    config = unreal.ConfigFile()
    config.load_file(ini_path)

    section = "/Script/Engine.RendererSettings"
    config.set_string(section, "r.DynamicGlobalIlluminationMethod", setting_value)
    config.set_string(section, "r.ReflectionMethod", setting_value)

    config.write(ini_path)

    state = 'enabled' if enable_lumen else 'disabled'
    unreal.log(f"Lumen has been {state} in DefaultEngine.ini.")


def is_lumen_enabled():
    ini_path = unreal.Paths.combine([unreal.SystemLibrary.get_project_directory(), "Config/DefaultEngine.ini"])

    config = unreal.ConfigFile()
    config.load_file(ini_path)

    section = "/Script/Engine.RendererSettings"
    value = config.get_string(section, "r.DynamicGlobalIlluminationMethod")

    return value == '1'


def apply_lumen_state_to_widget(widget_path):
    ini_path = unreal.Paths.combine([unreal.SystemLibrary.get_project_directory(), "Config/DefaultEngine.ini"])

    config = unreal.ConfigFile()
    config.load_file(ini_path)

    section = "/Script/Engine.RendererSettings"
    value = config.get_string(section, "r.DynamicGlobalIlluminationMethod")
    is_enabled = value == '1'

    widget = unreal.load_object(None, widget_path)
    if widget:
        widget.set_editor_property('bLumenEnabled', is_enabled)
        unreal.log(f"Checkbox set to {is_enabled}")