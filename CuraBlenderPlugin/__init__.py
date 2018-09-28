# Copyright (c) 2016 Thomas Karl Pietrowski

from UM.Platform import Platform

from UM.Logger import Logger

from UM.i18n import i18nCatalog
i18n_catalog = i18nCatalog("CuraBlenderIntegrationPlugin")

def getMetaData():
    return {
        "mesh_reader": [
            {
                "extension": "BLEND",
                "description": i18n_catalog.i18nc("@item:inlistbox", "Blender file")
            },
        ]
    }

def register(app):
    try:
        from . import BlenderReader
        return {"mesh_reader": BlenderReader.BlenderReader()}
    except:
        Logger.logException("e", "An error occured, when trying to import BlenderReader!")
        return {}
