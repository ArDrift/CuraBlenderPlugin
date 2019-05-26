# Copyright (c) 2016 Thomas Karl Pietrowski

__plugin_name__ = "Blender plugin"
__plugin_id__ = "CuraBlenderPlugin"

# Uranium
from UM.Logger import Logger
from UM.i18n import i18nCatalog
i18n_catalog = i18nCatalog(__plugin_id__)

# This plugin
from . import BlenderReader

def getMetaData():
    return {
        "mesh_reader": [
            {
                "extension": "BLEND",
                "description": i18n_catalog.i18nc("@item:inlistbox",
                                                  "Blender file"
                                                  )
            },
        ]
    }

def register(app):
    plugin_data = {}
    try:
        reader = BlenderReader.BlenderReader()
        plugin_data["mesh_reader"] = reader
    except:
        Logger.logException("e", "An error occured, when trying to import BlenderReader!")
        return {}

    return plugin_data
