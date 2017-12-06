# Copyright (c) 2016 Thomas Karl Pietrowski

import os
import platform

from UM.Logger import Logger # @UnresolvedImport

from UM.i18n import i18nCatalog # @UnresolvedImport
i18n_catalog = i18nCatalog("CuraBlenderIntegrationPlugin")

from .CadIntegrationUtils.CommonCLIReader import CommonCLIReader # @UnresolvedImport

class BlenderReader(CommonCLIReader):
    def __init__(self):
        super().__init__("Blender")
        self._supported_extensions = [".BLEND".lower(),
                                      ]
        
        self.scanForAllPaths()

    def areReadersAvailable(self):
        return bool(self._readerForFileformat)


    def openForeignFile(self, options):
        return options
    
    def exportFileAs(self, options, quality_enum = None):

        # Use the appropriate command for the current OS
        if platform.system() == 'Darwin':
            cmd = '/Applications/Blender.app/Contents/MacOS/blender'
        else:
            cmd = 'blender'

        bpy_scripts = os.path.join(os.path.split(__file__)[0], "BpyScripts")
        
        Logger.log("d", "BpyScripts at: {}".format(bpy_scripts))
        Logger.log("d", "Using blender file at: {}".format(options["foreignFile"]))
        Logger.log("d", "Exporting to: {}".format(options["tempFile"]))
        
        cmd = [cmd, options["foreignFile"], "--background", "--python", os.path.join(bpy_scripts, "ExportAsStl.py"), "--", options["tempFile"]]
        
        self.executeCommand(cmd, cwd = os.path.split(options["foreignFile"])[0])