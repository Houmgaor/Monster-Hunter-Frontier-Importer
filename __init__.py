# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 13:38:47 2019

@author: AsteriskAmpersand
"""
# from .dbg import dbg_init
# dbg_init()
import bpy

from .operators.fmodimport import ImportFMOD
from .operators.fsklimport import ImportFSKL
from .operators.fsklConverter import ConvertFSKL
from .operators.fmodimport import menu_func_import as mhf_model_menu_func_import
from .operators.fsklimport import menu_func_import as mhf_skele_menu_func_import

content = bytes("", "UTF-8")
bl_info = {
    "name": "MHF FMod Model Importer",
    "category": "Import-Export",
    "author": "AsteriskAmpersand (Code) & Vuze (Structure)",
    "location": "File > Import-Export > FMod/MHF",
    "version": (2, 0, 0),
    "blender": (2, 80, 0)
}


def register():
    """Add the add-on."""
    bpy.utils.register_class(ImportFMOD)
    # New structure since Blender 2.8x
    if bpy.app.version >= (2, 8):
        bpy.types.TOPBAR_MT_file_import.append(mhf_model_menu_func_import)
    else:
        bpy.types.INFO_MT_file_import.append(mhf_model_menu_func_import)
    bpy.utils.register_class(ImportFSKL)
    if bpy.app.version >= (2, 8):
        bpy.types.TOPBAR_MT_file_import.append(mhf_skele_menu_func_import)
    else:
        bpy.types.INFO_MT_file_import.append(mhf_skele_menu_func_import)
    bpy.utils.register_class(ConvertFSKL)


def unregister():
    """Remove the add-on."""
    bpy.utils.unregister_class(ImportFMOD)
    # New structure since Blender 2.8x
    if bpy.app.version >= (2, 8):
        bpy.types.TOPBAR_MT_file_import.remove(mhf_model_menu_func_import)
    else:
        bpy.types.INFO_MT_file_import.remove(mhf_model_menu_func_import)
    bpy.utils.unregister_class(ImportFSKL)
    if bpy.app.version >= (2, 8):
        bpy.types.TOPBAR_MT_file_import.remove(mhf_skele_menu_func_import)
    else:
        bpy.types.INFO_MT_file_import.remove(mhf_skele_menu_func_import)
    bpy.utils.unregister_class(ConvertFSKL)


if __name__ == "__main__":
    try:
        unregister()
    except Exception as err:
        print("Cannot unregister: ", err)
    finally:
        register()
