import sys
import bpy

stl_path = sys.argv[-1]

bpy.ops.export_mesh.stl(filepath = stl_path,
                        check_existing = False,
                        #use_mesh_modifiers  = False,
                        #use_selection=False,
                        #axis_forward = '-Z',
                        #axis_up = 'Y',
                        )
