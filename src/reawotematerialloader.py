# -*- coding: utf-8 -*-
# #### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import os
import sys

import c4d
from c4d import plugins, gui
import maxon
import redshift

import reawotesettings as SettingsDialog


REAWOTE_PLUGIN_ID=1056421
ROOT_DIR = os.path.split(__file__)[0]
__res__ = None

dialog = None

checkbox_list = []
same_path_dirs = []
material_to_add = []
path_lists = []
path_list = []
mapID_list = []
file_names = []
path = ""


ID_CHECKBOX = 999
ID_NAME = 998
ID_OTHER = 997

IDS_REAWOTE_PBR_CONVERTER = 10000
IDS_DIALOG_BROWSE = 10001
IDS_DIALOG_TEXTURE_FOLDER = 10002

IDS_DIALOG_MAIN_GROUP = 10014
IDS_DIALOG_SCROLL_GROUP = 10012
IDS_DIALOG_SCROLL_GROUP_TWO = 10016
IDS_DIALOG_SECONDARY_GROUP = 10015
IDS_DIALOG_LIST_CHECKBOX = 10011
IDS_DIALOG_LIST_BUTTON = 10017
IDS_DIALOG_SELECT_ALL_BUTTON = 10018
IDS_DIALOG_FOLDER_LIST = 10013

IDS_DIALOG_INCLUDE_AO = 10003
IDS_DIALOG_INCLUDE_DISPLACEMENT = 10004
IDS_DIALOG_USE_16_BIT_DISPLACEMENT_MAPS = 10005
IDS_DIALOG_LOAD = 10006
IDS_DIALOG_USE_16_BIT_NORMAL_MAPS = 10007

class ID(): 
    DIALOG_FOLDER_GROUP = 100000
    DIALOG_FOLDER_TEXT =  100001
    DIALOG_FOLDER_BUTTON = 100002
    DIALOG_FOLDER_SECONDARY_BUTTON = 100031


    DIALOG_MAP_AO_CB = 100003
    DIALOG_MAP_DISPL_CB = 100004
    DIALOG_MAP_16B_DISPL_CB = 100005
    DIALOG_MAP_IOR_CB = 100006
    DIALOG_LOAD_BUTTON = 100007
    DIALOG_ERROR = 100008
    DIALOG_MAP_16B_NORMAL_CB = 100009
    
    DIALOG_MAIN_GROUP = 100014
    DIALOG_SCROLL_GROUP = 100012
    DIALOG_SCROLL_GROUP_TWO = 100016
    DIALOG_SECONDARY_GROUP = 10011
    DIALOG_FOLDER_LIST = 100015
    DIALOG_LIST_BUTTON = 100017
    DIALOG_LIST_CHECKBOX = 100013
    DIALOG_LIST_MINI_BUTTONS = 100020
    DIALOG_SELECT_ALL_BUTTON = 100018
    DIALOG_REFRESH_ALL_BUTTON = 100019
    DIALOG_ADD_TO_QUEUE_BUTTON = 100021
    DIALOG_CLEAN_BUTTON = 100022
    DIALOG_GROUP_RENDERER = 100023
    DIALOG_RENDERER_TEXT = 100024
    DIALOG_RENDERER_COMBOBOX = 100025
    DIALOG_SETTINGS_BUTTON = 100026

    DIALOG_PREVIEW_GROUP = 100027
    DIALOG_MATERIAL_PREVIEW = 100028
    DIALOG_PREVIEW_TEXT = 100029
    DIALOG_HIDDEN_PREVIEW = 100030

    PLUGINID_CORONA4D_MATERIAL = 1032100
    PLUGINID_CORONA4D_NORMALSHADER = 1035405
    PLUGINID_CORONA4D_AOSHADER = 1034433

    CORONA_MATERIAL_PREVIEWSIZE = 4050
    CORONA_MATERIAL_PREVIEWSIZE_1024 = 10

    CORONA_DIFFUSE_TEXTURE = 4301
    CORONA_NORMALMAP_TEXTURE = 11321

    CORONA_MATERIAL_BUMPMAPPING = 4108
    CORONA_BUMPMAPPING_STRENGTH = 4850
    CORONA_BUMPMAPPING_TEXTURE = 4851

    CORONA_MATERIAL_DISPLACEMENT = 4106
    CORONA_DISPLACEMENT_TEXTURE = 4802
    CORONA_DISPLACEMENT_MIN_LEVEL = 4800
    CORONA_DISPLACEMENT_MAX_LEVEL = 4801

    CORONA_AO_UNOCCLUDED_TEXTURE = 11021
    CORONA_AO_CALCULATE_FROM = 11007
    CORONA_AO_CALCULATE_FROM_BOTH = 2

    CORONA_MATERIAL_ALPHA = 4109
    CORONA_ALPHA_TEXTURE = 4751

    CORONA_REFLECT_GLOSSINESS_TEXTURE = 4512

    CORONA_MATERIAL_REFLECT = 4103
    CORONA_REFLECT_TEXTURE = 4501

    CORONA_MATERIAL_VOLUME = 4110
    CORONA_VOLUME_SCATTER_TEXTURE = 4681
    CORONA_VOLUME_ABSORPTION_TEXTURE = 4631

    CORONA_REFLECT_FRESNELLOR_VALUE = 4541
    CORONA_REFLECT_FRESNELLOR_TEXTURE = 4542

    
    CORONA_STR_MATERIAL_PHYSICAL = 1056306
    CORONA_PHYSICAL_MATERIAL_HEADER = 20000

    CORONA_PHYSICAL_MATERIAL_GENERAL         = 20001
    CORONA_PHYSICAL_MATERIAL_BASE_LAYER      = 20002
    CORONA_PHYSICAL_MATERIAL_REFRACT         = 20003
    CORONA_PHYSICAL_MATERIAL_ALPHA           = 20004
    CORONA_PHYSICAL_MATERIAL_DISPLACEMENT    = 20005
    CORONA_PHYSICAL_MATERIAL_CLEARCOAT       = 20006
    CORONA_PHYSICAL_MATERIAL_SHEEN           = 20007
    CORONA_PHYSICAL_MATERIAL_VOLUMETRICS     = 20008
    CORONA_PHYSICAL_MATERIAL_SSS             = 20009
    CORONA_PHYSICAL_MATERIAL_EMISSION        = 20010
    CORONA_PHYSICAL_MATERIAL_THIN_ABSORPTION = 20012
    CORONA_PHYSICAL_MATERIAL_TRANSLUCENCY    = 20013

    ID_CORONA_PHYSICAL_MATERIAL_GENERAL         = 20051
    ID_CORONA_PHYSICAL_MATERIAL_BASE_LAYER      = 20052
    ID_CORONA_PHYSICAL_MATERIAL_REFRACT         = 20053
    ID_CORONA_PHYSICAL_MATERIAL_ALPHA           = 20054
    ID_CORONA_PHYSICAL_MATERIAL_DISPLACEMENT    = 20055
    ID_CORONA_PHYSICAL_MATERIAL_CLEARCOAT       = 20056
    ID_CORONA_PHYSICAL_MATERIAL_SHEEN           = 20057
    ID_CORONA_PHYSICAL_MATERIAL_VOLUMETRICS     = 20058
    ID_CORONA_PHYSICAL_MATERIAL_SSS             = 20059
    ID_CORONA_PHYSICAL_MATERIAL_EMISSION        = 20060
    ID_CORONA_PHYSICAL_MATERIAL_THIN_ABSORPTION = 20062
    ID_CORONA_PHYSICAL_MATERIAL_TRANSLUCENCY    = 20063

    CORONA_PHYSICAL_MATERIAL_METALLIC_MODE            = 20101
    CORONA_PHYSICAL_MATERIAL_METALLIC_MODE_VALUE      = 20102
    CORONA_PHYSICAL_MATERIAL_METALLIC_MODE_METALLIC   = 0
    CORONA_PHYSICAL_MATERIAL_METALLIC_MODE_DIELECTRIC = 1
    CORONA_PHYSICAL_MATERIAL_METALLIC_MODE_TEXTURE    = 20103

    CORONA_PHYSICAL_MATERIAL_PRESET           = 20104
    CORONA_PHYSICAL_MATERIAL_PRESET_NO_PRESET = 0
    CORONA_PHYSICAL_MATERIAL_PRESET_DEFAULT = 1


    CORONA_PHYSICAL_MATERIAL_BASE_COLOR                 = 20201
    CORONA_PHYSICAL_MATERIAL_BASE_COLOR_TEXTURE         = 20202
    CORONA_PHYSICAL_MATERIAL_BASE_COLOR_LEVEL           = 20203
    CORONA_PHYSICAL_MATERIAL_BASE_COLOR_MIX_VALUE       = 20204
    CORONA_PHYSICAL_MATERIAL_BASE_COLOR_MIX_MODE        = 20205
    CORONA_PHYSICAL_MATERIAL_BASE_ROUGHNESS             = 20207
    CORONA_PHYSICAL_MATERIAL_BASE_ROUGHNESS_VALUE       = 20208
    CORONA_PHYSICAL_MATERIAL_BASE_ROUGHNESS_TEXTURE     = 20209
    CORONA_PHYSICAL_MATERIAL_BASE_IOR                   = 20210
    CORONA_PHYSICAL_MATERIAL_BASE_IOR_VALUE             = 20211
    CORONA_PHYSICAL_MATERIAL_BASE_IOR_TEXTURE           = 20212
    CORONA_PHYSICAL_MATERIAL_BASE_EDGECOLOR             = 20226
    CORONA_PHYSICAL_MATERIAL_BASE_EDGECOLOR_COLOR       = 20227
    CORONA_PHYSICAL_MATERIAL_BASE_EDGECOLOR_TEXTURE     = 20228
    CORONA_PHYSICAL_MATERIAL_BASE_EDGECOLOR_LEVEL       = 20229
    CORONA_PHYSICAL_MATERIAL_BASE_EDGECOLOR_MIX_VALUE   = 20230
    CORONA_PHYSICAL_MATERIAL_BASE_EDGECOLOR_MIX_MODE    = 20231
    CORONA_PHYSICAL_MATERIAL_BASE_BUMPMAPPING           = 20216
    CORONA_PHYSICAL_MATERIAL_BASE_BUMPMAPPING_VALUE     = 20217
    CORONA_PHYSICAL_MATERIAL_BASE_BUMPMAPPING_TEXTURE   = 20218
    CORONA_PHYSICAL_MATERIAL_BASE_BUMPMAPPING_ENABLE    = 20225
    CORONA_PHYSICAL_MATERIAL_BASE_ANISOTROPY            = 20219
    CORONA_PHYSICAL_MATERIAL_BASE_ANISOTROPY_VALUE      = 20220
    CORONA_PHYSICAL_MATERIAL_BASE_ANISOTROPY_TEXTURE    = 20221
    CORONA_PHYSICAL_MATERIAL_BASE_ANISOROTATION         = 20222
    CORONA_PHYSICAL_MATERIAL_BASE_ANISOROTATION_VALUE   = 20223
    CORONA_PHYSICAL_MATERIAL_BASE_ANISOROTATION_TEXTURE = 20224

    CORONA_PHYSICAL_MATERIAL_TRANSLUCENCY_FRACTION         = 21307
    CORONA_PHYSICAL_MATERIAL_TRANSLUCENCY_FRACTION_VALUE   = 21308
    CORONA_PHYSICAL_MATERIAL_TRANSLUCENCY_FRACTION_TEXTURE = 21309
    CORONA_PHYSICAL_MATERIAL_TRANSLUCENCY_COLOR_TITLE      = 21301
    CORONA_PHYSICAL_MATERIAL_TRANSLUCENCY_COLOR            = 21302
    CORONA_PHYSICAL_MATERIAL_TRANSLUCENCY_TEXTURE          = 21303
    CORONA_PHYSICAL_MATERIAL_TRANSLUCENCY_LEVEL            = 21304
    CORONA_PHYSICAL_MATERIAL_TRANSLUCENCY_MIX_VALUE        = 21305
    CORONA_PHYSICAL_MATERIAL_TRANSLUCENCY_MIX_MODE         = 21306

    CORONA_PHYSICAL_MATERIAL_REFRACT_AMOUNT           = 20301
    CORONA_PHYSICAL_MATERIAL_REFRACT_AMOUNT_VALUE     = 20302
    CORONA_PHYSICAL_MATERIAL_REFRACT_AMOUNT_TEXTURE   = 20303
    CORONA_PHYSICAL_MATERIAL_REFRACT_BEHAVIOR         = 20311
    CORONA_PHYSICAL_MATERIAL_REFRACT_CAUSTICS         = 20312
    CORONA_PHYSICAL_MATERIAL_REFRACT_THIN             = 20313
    CORONA_PHYSICAL_MATERIAL_REFRACT_DISPERSION       = 20314
    CORONA_PHYSICAL_MATERIAL_REFRACT_DISPERSION_VALUE = 20315
    CORONA_PHYSICAL_MATERIAL_REFRACT_ABBE_NUMBER      = 20316

    CORONA_PHYSICAL_MATERIAL_ALPHA_COLOR     = 20401
    CORONA_PHYSICAL_MATERIAL_ALPHA_TEXTURE   = 20402
    CORONA_PHYSICAL_MATERIAL_ALPHA_LEVEL     = 20403
    CORONA_PHYSICAL_MATERIAL_ALPHA_MIX_VALUE = 20404
    CORONA_PHYSICAL_MATERIAL_ALPHA_MIX_MODE  = 20405
    CORONA_PHYSICAL_MATERIAL_ALPHA_CLIP      = 20407

    CORONA_PHYSICAL_MATERIAL_DISPLACEMENT_MIN_LEVEL           = 20501
    CORONA_PHYSICAL_MATERIAL_DISPLACEMENT_MAX_LEVEL           = 20502
    CORONA_PHYSICAL_MATERIAL_DISPLACEMENT_TEXTURE             = 20503
    CORONA_PHYSICAL_MATERIAL_DISPLACEMENT_WATER_LEVEL_ENABLE  = 20504
    CORONA_PHYSICAL_MATERIAL_DISPLACEMENT_WATER_LEVEL         = 20505
    CORONA_PHYSICAL_MATERIAL_DISPLACEMENT_MODE                = 20506
    CORONA_PHYSICAL_MATERIAL_DISPLACEMENT_MODE_NORMAL         = 0
    CORONA_PHYSICAL_MATERIAL_DISPLACEMENT_MODE_VECTOR_TANGENT = 1
    CORONA_PHYSICAL_MATERIAL_DISPLACEMENT_MODE_VECTOR_OBJECT  = 2

    CORONA_PHYSICAL_MATERIAL_CLEARCOAT_AMOUNT               = 20601
    CORONA_PHYSICAL_MATERIAL_CLEARCOAT_AMOUNT_VALUE         = 20602
    CORONA_PHYSICAL_MATERIAL_CLEARCOAT_AMOUNT_TEXTURE       = 20603
    CORONA_PHYSICAL_MATERIAL_CLEARCOAT_ROUGHNESS            = 20604
    CORONA_PHYSICAL_MATERIAL_CLEARCOAT_ROUGHNESS_VALUE      = 20605
    CORONA_PHYSICAL_MATERIAL_CLEARCOAT_ROUGHNESS_TEXTURE    = 20606
    CORONA_PHYSICAL_MATERIAL_CLEARCOAT_IOR                  = 20607
    CORONA_PHYSICAL_MATERIAL_CLEARCOAT_IOR_VALUE            = 20608
    CORONA_PHYSICAL_MATERIAL_CLEARCOAT_IOR_TEXTURE          = 20609
    CORONA_PHYSICAL_MATERIAL_CLEARCOAT_ABSORPTION           = 20610
    CORONA_PHYSICAL_MATERIAL_CLEARCOAT_ABSORPTION_COLOR     = 20611
    CORONA_PHYSICAL_MATERIAL_CLEARCOAT_ABSORPTION_TEXTURE   = 20612
    CORONA_PHYSICAL_MATERIAL_CLEARCOAT_ABSORPTION_LEVEL     = 20613
    CORONA_PHYSICAL_MATERIAL_CLEARCOAT_ABSORPTION_MIX_VALUE = 20614
    CORONA_PHYSICAL_MATERIAL_CLEARCOAT_ABSORPTION_MIX_MODE  = 20615
    CORONA_PHYSICAL_MATERIAL_CLEARCOAT_BUMPMAPPING          = 20617
    CORONA_PHYSICAL_MATERIAL_CLEARCOAT_BUMPMAPPING_VALUE    = 20618
    CORONA_PHYSICAL_MATERIAL_CLEARCOAT_BUMPMAPPING_TEXTURE  = 20619
    CORONA_PHYSICAL_MATERIAL_CLEARCOAT_BUMPMAPPING_ENABLE   = 20620


    CORONA_PHYSICAL_MATERIAL_SHEEN_AMOUNT            = 20701
    CORONA_PHYSICAL_MATERIAL_SHEEN_AMOUNT_VALUE      = 20702
    CORONA_PHYSICAL_MATERIAL_SHEEN_AMOUNT_TEXTURE    = 20703
    CORONA_PHYSICAL_MATERIAL_SHEEN_ROUGHNESS         = 20704
    CORONA_PHYSICAL_MATERIAL_SHEEN_ROUGHNESS_VALUE   = 20705
    CORONA_PHYSICAL_MATERIAL_SHEEN_ROUGHNESS_TEXTURE = 20706
    CORONA_PHYSICAL_MATERIAL_SHEEN_COLOR             = 20707
    CORONA_PHYSICAL_MATERIAL_SHEEN_COLOR_VALUE       = 20708
    CORONA_PHYSICAL_MATERIAL_SHEEN_COLOR_TEXTURE     = 20709
    CORONA_PHYSICAL_MATERIAL_SHEEN_COLOR_LEVEL       = 20710
    CORONA_PHYSICAL_MATERIAL_SHEEN_COLOR_MIX_VALUE   = 20711
    CORONA_PHYSICAL_MATERIAL_SHEEN_COLOR_MIX_MODE    = 20712

    CORONA_PHYSICAL_MATERIAL_VOLUME_MODE_VOLUMETRIC        = 20801
    CORONA_PHYSICAL_MATERIAL_VOLUME_MODE_SSS               = 20802
    CORONA_PHYSICAL_MATERIAL_VOLUME_ABSORPTION             = 20803
    CORONA_PHYSICAL_MATERIAL_VOLUME_ABSORPTION_COLOR       = 20804
    CORONA_PHYSICAL_MATERIAL_VOLUME_ABSORPTION_TEXTURE     = 20805
    CORONA_PHYSICAL_MATERIAL_VOLUME_ABSORPTION_LEVEL       = 20806
    CORONA_PHYSICAL_MATERIAL_VOLUME_ABSORPTION_MIX_VALUE   = 20807
    CORONA_PHYSICAL_MATERIAL_VOLUME_ABSORPTION_MIX_MODE    = 20808
    CORONA_PHYSICAL_MATERIAL_VOLUME_ABSORPTION_DISTANCE    = 20810
    CORONA_PHYSICAL_MATERIAL_VOLUME_SCATTER                = 20811
    CORONA_PHYSICAL_MATERIAL_VOLUME_SCATTER_COLOR          = 20812
    CORONA_PHYSICAL_MATERIAL_VOLUME_SCATTER_TEXTURE        = 20813
    CORONA_PHYSICAL_MATERIAL_VOLUME_SCATTER_LEVEL          = 20814
    CORONA_PHYSICAL_MATERIAL_VOLUME_SCATTER_MIX_VALUE      = 20815
    CORONA_PHYSICAL_MATERIAL_VOLUME_SCATTER_MIX_MODE       = 20816
    CORONA_PHYSICAL_MATERIAL_VOLUME_SCATTER_DIRECTIONALITY = 20818
    CORONA_PHYSICAL_MATERIAL_VOLUME_SCATTER_SINGLE         = 20819
    CORONA_PHYSICAL_MATERIAL_VOLUME_SCATTER_OTHER          = 20821

    CORONA_PHYSICAL_MATERIAL_VOLUME_SSS_FRACTION         = 20901
    CORONA_PHYSICAL_MATERIAL_VOLUME_SSS_FRACTION_VALUE   = 20902
    CORONA_PHYSICAL_MATERIAL_VOLUME_SSS_FRACTION_TEXTURE = 20903
    CORONA_PHYSICAL_MATERIAL_VOLUME_SSS_RADIUS           = 20904
    CORONA_PHYSICAL_MATERIAL_VOLUME_SSS_RADIUS_VALUE     = 20905
    CORONA_PHYSICAL_MATERIAL_VOLUME_SSS_RADIUS_TEXTURE   = 20906
    CORONA_PHYSICAL_MATERIAL_VOLUME_SSS                  = 20907
    CORONA_PHYSICAL_MATERIAL_VOLUME_SSS_BLEED            = 20908
    CORONA_PHYSICAL_MATERIAL_VOLUME_SSS_TEXTURE          = 20909
    CORONA_PHYSICAL_MATERIAL_VOLUME_SSS_LEVEL            = 20910
    CORONA_PHYSICAL_MATERIAL_VOLUME_SSS_MIX_VALUE        = 20911
    CORONA_PHYSICAL_MATERIAL_VOLUME_SSS_MIX_MODE         = 20912

    CORONA_PHYSICAL_MATERIAL_EMISSION_COLOR_LEVEL     = 21004
    CORONA_PHYSICAL_MATERIAL_EMISSION_COLOR_MIX_VALUE = 21005
    CORONA_PHYSICAL_MATERIAL_EMISSION_COLOR_MIX_MODE  = 21006
    CORONA_PHYSICAL_MATERIAL_SELFILLUM_NOTE           = 21008

    CORONA_PHYSICAL_MATERIAL_ROUGHNESS_MODE            = 21101
    CORONA_PHYSICAL_MATERIAL_ROUGHNESS_MODE_ROUGHNESS  = 0
    CORONA_PHYSICAL_MATERIAL_ROUGHNESS_MODE_GLOSSINESS = 1

    CORONA_PHYSICAL_MATERIAL_IOR_MODE          = 21109
    CORONA_PHYSICAL_MATERIAL_IOR_MODE_IOR      = 0
    CORONA_PHYSICAL_MATERIAL_IOR_MODE_SPECULAR = 1

    CORONA_PHYSICAL_MATERIAL_COMPLEX_IOR         = 21102
    CORONA_PHYSICAL_MATERIAL_COMPLEX_IOR_ENABLED = 21103
    CORONA_PHYSICAL_MATERIAL_COMPLEX_IOR_R       = 21104
    CORONA_PHYSICAL_MATERIAL_COMPLEX_IOR_G       = 21105
    CORONA_PHYSICAL_MATERIAL_COMPLEX_IOR_B       = 21106
    CORONA_PHYSICAL_MATERIAL_COMPLEX_IOR_ETA     = 21107
    CORONA_PHYSICAL_MATERIAL_COMPLEX_IOR_KAPPA   = 21108

    CORONA_PHYSICAL_MATERIAL_BASE_TAIL         = 21400
    CORONA_PHYSICAL_MATERIAL_BASE_TAIL_VALUE   = 21401
    CORONA_PHYSICAL_MATERIAL_BASE_TAIL_TEXTURE = 21402

    CORONA_PHYSICAL_MATERIAL_ABSORPTION_COLOR     = 21201
    CORONA_PHYSICAL_MATERIAL_ABSORPTION_TEXTURE   = 21202
    CORONA_PHYSICAL_MATERIAL_ABSORPTION_LEVEL     = 21203
    CORONA_PHYSICAL_MATERIAL_ABSORPTION_MIX_VALUE = 21204
    CORONA_PHYSICAL_MATERIAL_ABSORPTION_MIX_MODE  = 21205

    _CORONA_PHYSICAL_MATERIAL_REFRACT_ABSORPTION_COLOR     = 20305
    _CORONA_PHYSICAL_MATERIAL_REFRACT_ABSORPTION_TEXTURE   = 20306
    _CORONA_PHYSICAL_MATERIAL_REFRACT_ABSORPTION_MIX_VALUE = 20308
    _CORONA_PHYSICAL_MATERIAL_REFRACT_ABSORPTION_MIX_MODE  = 20309

    # xnormalshader.h
    CORONA_NORMALMAP_TEXTURE = 11321
    CORONA_NORMALMAP_ = 11319
    CORONA_NORMALMAP_MODE = 11301
    CORONA_NORMALMAP_MODE_TANGENT = 0
    CORONA_NORMALMAP_MODE_OBJECT = 1
    CORONA_NORMALMAP_MODE_WORLD = 2
    CORONA_NORMALMAP_FLIP_R = 11311
    CORONA_NORMALMAP_FLIP_G = 11312
    CORONA_NORMALMAP_FLIP_B = 11313
    CORONA_NORMALMAP_SWAP_RG = 11317
    CORONA_NORMALMAP_BUMP = 11330
    CORONA_NORMALMAP_BUMP_STRENGTH = 11331
    CORONA_NORMALMAP_BUMP_TEXTURE = 11332
    CORONA_NORMALMAP_NOTE = 11338
    CORONA_NORMALMAP_NOTE2 = 11339
    CORONA_NORMALMAP_CUSTOM_UVW_OVERRIDE = 11341
    CORONA_NORMALMAP_CUSTOM_UVW_CHANNEL = 11342

    VRAY_MATERIAL = 1053286
    VRAY_BITMAP = 5833
    VRAY_BITMAP_SHADER = 1055619
    
    VRAY_NORMAL_MAP = 1057881
    VRAY_USE_BUMP_SHADOWS = 1921591250
    VRAY_FUSION = 1011109

    REDSHIFT_MATERIAL = 1036219

    OCTANE_MATERIAL = 1029501
    OCTANE_BSDF_MODEL = 2585
    OCTANE_BITMAP = 5833
    OCTANE_TEXTURE = 1029508
    OCTANE_MULTIPLY = 1029516
    OCTANE_DISPLACEMENT = 1031901

class TextureObject(object):
    texturePath = "TexPath"
    otherData = "OtherData"
    _selected = False

    def __init__(self, texturePath):
        self.texturePath = texturePath
        self.otherData+= texturePath

    @property
    def IsSelected(self):
        return self._selected
 
    def Select(self):
        self._selected = True
 
    def Deselect(self):
        self._selected = False
 
    def __repr__(self):
        return str(self)
 
    def __str__(self):
        return self.texturePath
    
class MaterialPreview(c4d.gui.GeUserArea):
    def __init__(self, bmp):
      super(MaterialPreview, self).__init__()
      self._bmp = bmp

    def DrawMsg(self, x1, y1, x2, y2, msg):
      #self.DrawSetPen(c4d.Vector(0))
      #self.DrawRectangle(0, 0, 42, 42)
      if not self._bmp: return

      coords = self.Local2Global()
      self.DrawBitmap(self._bmp, 0, 0, 62, 62, 0, 0, 62, 62, c4d.BMP_NORMAL | c4d.BMP_ALLOWALPHA)

    def GetMinSize(self):
      return 62, 62

    def setBitmap(self, bmp):
      self._bmp = bmp

class ListView(c4d.gui.TreeViewFunctions):
 
    def __init__(self, dialog_ref=None):
        self.listOfTexture = list()
        self.dialog_ref = dialog_ref
 
    def IsResizeColAllowed(self, root, userdata, lColID):
        return True
 
    def IsTristate(self, root, userdata):
        return False
 
    def GetColumnWidth(self, root, userdata, obj, col, area):
        return 80
 
    def IsMoveColAllowed(self, root, userdata, lColID):
        return True
 
    def GetFirst(self, root, userdata):
        rValue = None if not self.listOfTexture else self.listOfTexture[0]
        return rValue
 
    def GetDown(self, root, userdata, obj):
        return None
 
    def GetNext(self, root, userdata, obj):
        rValue = None
        currentObjIndex = self.listOfTexture.index(obj)
        nextIndex = currentObjIndex + 1
        if nextIndex < len(self.listOfTexture):
            rValue = self.listOfTexture[nextIndex]
 
        return rValue
 
    def GetPred(self, root, userdata, obj):
        rValue = None
        currentObjIndex = self.listOfTexture.index(obj)
        predIndex = currentObjIndex - 1
        if 0 <= predIndex < len(self.listOfTexture):
            rValue = self.listOfTexture[predIndex]
 
        return rValue
 
    def GetId(self, root, userdata, obj):
        return hash(obj)
 
    def Select(self, root, userdata, obj, mode):
        if mode == c4d.SELECTION_NEW:
            for tex in self.listOfTexture:
                tex.Deselect()
            obj.Select()
        elif mode == c4d.SELECTION_ADD:
            obj.Select()
        elif mode == c4d.SELECTION_SUB:
            obj.Deselect()
        self.UpdateMaterialPreview(obj)
 
    def IsSelected(self, root, userdata, obj):
        return obj.IsSelected
 
    def SetCheck(self, root, userdata, obj, column, checked, msg):
        if checked:
            self.UpdateMaterialPreview(obj)
            # print("Checked")
            obj.Select()
        else:
            self.UpdateMaterialPreview(obj)
            obj.Deselect()
 
    def IsChecked(self, root, userdata, obj, column):
        if obj.IsSelected:
            return c4d.LV_CHECKBOX_CHECKED | c4d.LV_CHECKBOX_ENABLED
        else:
            return c4d.LV_CHECKBOX_ENABLED

    def UpdateMaterialPreview(self, obj):
        self.dialog_ref.HideElement(ID.DIALOG_PREVIEW_GROUP, False)
        self.dialog_ref.LayoutChanged(ID.DIALOG_HIDDEN_PREVIEW)
        
        # print(f"Updating preview for: {obj}")
        path = path_list[self.listOfTexture.index(obj)]
        
        if os.name == "posix":
            path_parts = path.split(os.path.sep)[:-1]
            preview_path = os.path.sep.join(path_parts) + os.path.sep + "PREVIEW"

        if os.name == "nt":
            path_parts = path.split(os.path.sep)[:-1]
            preview_path = os.path.sep.join(path_parts) + os.path.sep + "PREVIEW"

        self.dialog_ref.SetString(ID.DIALOG_PREVIEW_TEXT, f"  {obj}")
        if os.path.exists(preview_path):
            contents = os.listdir(preview_path)
            for file in contents:
                if "FABRIC_1" in file or "SPHERE_1" in file:
                    # print(os.path.join(preview_path, file))
                    if self.dialog_ref:
                        self.dialog_ref.set_preview_material(path=(os.path.join(preview_path, file)))
                    else:
                        print("Failed to load bitmap from:", path)
                    break  # Exit the loop once we've found and processed the file
        else:
            print(f"The directory {preview_path} does not exist.")

 
    def GetName(self, root, userdata, obj):
        return str(obj)
 
    def DrawCell(self, root, userdata, obj, col, drawinfo, bgColor):
        if col == ID_OTHER:
            name = obj.otherData
            geUserArea = drawinfo["frame"]
            w = geUserArea.DrawGetTextWidth(name)
            h = geUserArea.DrawGetFontHeight()
            xpos = drawinfo["xpos"]
            ypos = drawinfo["ypos"] + drawinfo["height"]
            drawinfo["frame"].DrawText(name, xpos, ypos - h * 1.1)
 
    def DoubleClick(self, root, userdata, obj, col, mouseinfo):
        c4d.gui.MessageDialog("You clicked on " + str(obj))
        return True
 
    def DeletePressed(self, root, userdata):
        "Called when a delete event is received."
        for tex in reversed(self.listOfTexture):
            if tex.IsSelected:
                self.listOfTexture.remove(tex)

class ReawoteMaterialDialog(gui.GeDialog):
    has_16b_disp = False
    has_16b_normal = False
    has_disp = False
    has_AO = False
    has_Ior = False
    material_folder = None

    _treegui = None
    _listView = None

    def __init__(self):
        self._listView = ListView(self)
        self._area = MaterialPreview(None)
        self.MaterialPreviewBmp = c4d.bitmaps.BaseBitmap()
        self.MaterialPreviewBmpTmp = c4d.bitmaps.BaseBitmap()
        self.MaterialPreviewBmp.Init(62, 62)
        super(ReawoteMaterialDialog, self).__init__()
        #pass

    def CreateLayout(self):

        default_flags: int = c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT

        self.SetTitle("Reawote PBR Loader")

        self.ScrollGroupBegin(ID.DIALOG_SCROLL_GROUP, default_flags, c4d.SCROLLGROUP_VERT | c4d.SCROLLGROUP_HORIZ)
        self.GroupBegin(ID.DIALOG_MAIN_GROUP, default_flags, 1)
        self.GroupBorderSpace(15, 0, 0, 0)

        # self.GroupBegin(ID.DIALOG_FOLDER_GROUP, c4d.BFH_SCALEFIT, 3, 1, "Material folder", 0, 10, 10)
        # self.AddStaticText(ID.DIALOG_FOLDER_TEXT, c4d.BFH_SCALEFIT, 0, 0, "Material folder", 0)
        # self.AddButton(ID.DIALOG_FOLDER_BUTTON, c4d.BFH_RIGHT, inith=10, initw=250, name="Browse")
        # self.GroupEnd()

        self.GroupBegin(ID.DIALOG_FOLDER_GROUP, c4d.BFH_SCALEFIT, 2, 1, "Material folder", 0)
        self.AddStaticText(ID.DIALOG_FOLDER_TEXT, c4d.BFH_SCALEFIT, name="Material folder", initw=100)

        # Nested group for buttons, aligned vertically
        self.GroupBegin(0, c4d.BFH_SCALEFIT, 1, 2, "", 0)  # Anonymous group for buttons
        self.AddButton(ID.DIALOG_FOLDER_BUTTON, c4d.BFH_SCALEFIT, name="Browse", inith=10, initw=250)
        self.AddButton(ID.DIALOG_FOLDER_SECONDARY_BUTTON, c4d.BFH_SCALEFIT, name="Browse 1", inith=10, initw=250)  # New Button
        self.GroupEnd()

        self.GroupEnd()  # End of DIALOG_FOLDER_GROUP

        self.GroupBegin(ID.DIALOG_GROUP_RENDERER,  c4d.BFH_SCALEFIT, 3, 1, "Renderer", 0, 10, 10)
        self.AddStaticText(ID.DIALOG_RENDERER_TEXT, c4d.BFH_SCALEFIT, 0, 0, "Select Renderer", 0)
        header = c4d.BaseContainer()
        header.SetInt32(c4d.BITMAPBUTTON_IGNORE_BITMAP_WIDTH, False)
        header.SetInt32(c4d.BITMAPBUTTON_IGNORE_BITMAP_HEIGHT, True)
        header.SetBool(c4d.BITMAPBUTTON_BUTTON, True)
        header.SetBool(c4d.BITMAPBUTTON_TOGGLE, False)
        header.SetString(c4d.BITMAPBUTTON_TOOLTIP, "settings")
        if c4d.GetC4DVersion() // 1000 >= 21:
            idIconPrefs = 1026694
        else:
            idIconPrefs = 1026693
        header.SetInt32(c4d.BITMAPBUTTON_ICONID1, idIconPrefs)
        self.AddCustomGui(ID.DIALOG_SETTINGS_BUTTON, c4d.CUSTOMGUI_BITMAPBUTTON, "", c4d.BFH_LEFT, 32, 16, header)
        renderers = self.AddComboBox(ID.DIALOG_RENDERER_COMBOBOX, c4d.BFH_RIGHT, inith=10, initw=250)
        physical = self.AddChild(renderers, 6400, "Physical")
        corona = self.AddChild(renderers, 6401, "Corona")
        vray = self.AddChild(renderers, 6402, "V-ray")
        redshift = self.AddChild(renderers, 6403, "Redshift")
        octane = self.AddChild(renderers, 6404, "Octane")
        self.GroupEnd()

        self.AddEditText(ID.DIALOG_FOLDER_LIST,  c4d.BFH_SCALEFIT, inith=10, initw=50)
        self.AddCheckbox(ID.DIALOG_MAP_AO_CB, c4d.BFH_SCALEFIT, 1, 1, "Include ambient occlusion (AO) maps")
        self.AddCheckbox(ID.DIALOG_MAP_DISPL_CB, c4d.BFH_SCALEFIT, 1, 1, "Include displacement maps")
        self.AddCheckbox(ID.DIALOG_MAP_16B_DISPL_CB, c4d.BFH_SCALEFIT, 1, 1, "Use 16 bit displacement maps (when available)")
        self.AddCheckbox(ID.DIALOG_MAP_16B_NORMAL_CB, c4d.BFH_SCALEFIT, 1, 1, "Use 16 bit normal maps (when available)")
        strErr = self.AddStaticText(ID.DIALOG_ERROR, c4d.BFH_SCALEFIT, 64, 10, "", 0)
        
        customgui = c4d.BaseContainer()
        customgui.SetBool(c4d.TREEVIEW_BORDER, c4d.BORDER_THIN_IN)
        customgui.SetBool(c4d.TREEVIEW_HAS_HEADER, True)
        customgui.SetBool(c4d.TREEVIEW_HIDE_LINES, False)
        customgui.SetBool(c4d.TREEVIEW_MOVE_COLUMN, True)
        customgui.SetBool(c4d.TREEVIEW_RESIZE_HEADER, True)
        customgui.SetBool(c4d.TREEVIEW_FIXED_LAYOUT, True)
        customgui.SetBool(c4d.TREEVIEW_ALTERNATE_BG, True)
        customgui.SetBool(c4d.TREEVIEW_CURSORKEYS, True)
        customgui.SetBool(c4d.TREEVIEW_NOENTERRENAME, False)

        self.AddButton(ID.DIALOG_LIST_BUTTON, c4d.BFH_SCALEFIT, 1, 1, "Load selected materials")
        self.GroupBegin(ID.DIALOG_LIST_MINI_BUTTONS, c4d.BFH_LEFT, 4,1, "Mini buttons", 0, 10, 10)
        self.AddButton(ID.DIALOG_SELECT_ALL_BUTTON, c4d.BFH_LEFT, 70, 5, "Select All")
        self.AddButton(ID.DIALOG_REFRESH_ALL_BUTTON, c4d.BFH_LEFT, 60, 5, "Refresh")
        self.AddButton(ID.DIALOG_ADD_TO_QUEUE_BUTTON, c4d.BFH_LEFT, 110, 5, "Add To Queue")
        self.AddButton(ID.DIALOG_CLEAN_BUTTON, c4d.BFH_CENTER, 60, 5, "Clean")
        self.GroupEnd()

        self._treegui = self.AddCustomGui(9300, c4d.CUSTOMGUI_TREEVIEW, "",  c4d.BFH_SCALEFIT, 300, 300, customgui)
        if not self._treegui:
            # print ("[ERROR]: Could not create TreeView")
            return False

        if self.GroupBegin(ID.DIALOG_HIDDEN_PREVIEW, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT):
            self.GroupBorderSpace(5, 10, 0, 0)

            # Existing DIALOG_PREVIEW_GROUP wrapped inside the parent group
            if self.GroupBegin(ID.DIALOG_PREVIEW_GROUP, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, title="Material Preview"):
                # self.GroupBorderSpace(5, 5, 5, 0)

                # The rest of your DIALOG_PREVIEW_GROUP content goes here
                self.AddUserArea(ID.DIALOG_MATERIAL_PREVIEW, c4d.BFH_CENTER, 60, 60)
                self.AttachUserArea(self._area, ID.DIALOG_MATERIAL_PREVIEW)
                self.AddStaticText(ID.DIALOG_PREVIEW_TEXT, c4d.BFH_SCALEFIT, 0, 0, "Material preview", 0)

                self.GroupEnd()  # End of DIALOG_PREVIEW_GROUP

            self.GroupEnd()
    
        # self.GroupBegin(ID.DIALOG_SCROLL_GROUP, c4d.BFH_SCALEFIT, 2, 1, "Material folder", 0, 10, 10)
        self.GroupEnd()
        self.GroupEnd()
        self.GroupEnd()
        self.Reset()

        self.SetTimer(1000)
        
        return True
    
    def InitValues(self):
        self.material_folder = None
    
        self.has_16b_disp = False
        self.has_16b_normal = False
        self.has_disp = False
        self.has_AO = False
        self.has_Ior = False

        if(os.name == "posix"):
            text_file_path = os.path.join(ROOT_DIR, "renderer_posix.txt")
        if(os.name == "nt"):
            text_file_path = os.path.join(ROOT_DIR, "renderer_nt.txt")

        f = open(text_file_path, "r")
        renderer = f.read()
        if renderer == "Physical":
            self.SetInt32(ID.DIALOG_RENDERER_COMBOBOX, 6400)
        if renderer == "Corona":
            self.SetInt32(ID.DIALOG_RENDERER_COMBOBOX, 6401)
        if renderer == "V-ray":
            self.SetInt32(ID.DIALOG_RENDERER_COMBOBOX, 6402)
        if renderer == "Redshift":
            self.SetInt32(ID.DIALOG_RENDERER_COMBOBOX, 6403)
        if renderer == "Octane":
            self.SetInt32(ID.DIALOG_RENDERER_COMBOBOX, 6404)
        
        self.SetBool(ID.DIALOG_MAP_AO_CB, False)
        self.Enable(ID.DIALOG_MAP_AO_CB, False)
        self.SetBool(ID.DIALOG_MAP_DISPL_CB, False)
        self.Enable(ID.DIALOG_MAP_DISPL_CB, False)
        self.SetBool(ID.DIALOG_MAP_16B_DISPL_CB, False)
        self.Enable(ID.DIALOG_MAP_16B_DISPL_CB, False)
        self.SetBool(ID.DIALOG_MAP_16B_NORMAL_CB, False)
        self.Enable(ID.DIALOG_MAP_16B_NORMAL_CB, False)
        self.SetBool(ID.DIALOG_MAP_IOR_CB, False)
        self.Enable(ID.DIALOG_MAP_IOR_CB, False)

        self.Enable(ID.DIALOG_LOAD_BUTTON, False)

        self.Enable(ID.DIALOG_LIST_BUTTON, False)
        self.Enable(ID.DIALOG_SELECT_ALL_BUTTON, False)
        self.Enable(ID.DIALOG_REFRESH_ALL_BUTTON, False)
        self.Enable(ID.DIALOG_ADD_TO_QUEUE_BUTTON, False)
        self.Enable(ID.DIALOG_CLEAN_BUTTON, False)
        self.Enable(ID.DIALOG_RENDERER_COMBOBOX, False)

        layout = c4d.BaseContainer()
        layout.SetLong(ID_CHECKBOX, c4d.LV_CHECKBOX)
        layout.SetLong(ID_NAME, c4d.LV_TREE)
        self._treegui.SetLayout(2, layout)
 
        self._treegui.SetHeaderText(ID_CHECKBOX, "Check")
        self._treegui.SetHeaderText(ID_NAME, "Name")
        self._treegui.Refresh()
 
        self._treegui.SetRoot(self._treegui, self._listView, None)
        
        while len(self._listView.listOfTexture) > 0:
            tex = self._listView.listOfTexture[0]
            self._listView.listOfTexture.remove(tex)
        self._treegui.Refresh()

        # self._listView.UpdateMaterialPreview(os.path.join(ROOT_DIR, "res", "images", "default_preview.png"))
        self.HideElement(ID.DIALOG_PREVIEW_GROUP, True)
        self.LayoutChanged(ID.DIALOG_HIDDEN_PREVIEW)

        return True

    def GetFileAssetUrl(path: str) -> maxon.Url:
        return maxon.Url(path)
    
    def set_preview_material(self, path):
        self.MaterialPreviewBmpTmp.InitWith(path)
        if (self.MaterialPreviewBmpTmp.GetBw()-1 > 41 and self.MaterialPreviewBmpTmp.GetBh()-1 > 61):
            self.MaterialPreviewBmpTmp.ScaleBicubic(self.MaterialPreviewBmp,
             0, 0, self.MaterialPreviewBmpTmp.GetBw()-1, self.MaterialPreviewBmpTmp.GetBh()-1,
             0, 0, 61, 61)
        else:
            self.MaterialPreviewBmpTmp.ScaleIt(self.MaterialPreviewBmp, 256, True, False)
        self._area.setBitmap(self.MaterialPreviewBmp)
        self._area.Redraw()
        self.LayoutChanged(ID.DIALOG_PREVIEW_GROUP)
        self.LayoutChanged(30)

        return

        
    def Command(self, id, msg,):
        
        if id == ID.DIALOG_SETTINGS_BUTTON:
            settings_dialog = SettingsDialog.get_dialog()
            if settings_dialog is None:
                SettingsDialog.__res__ = __res__
                SettingsDialog.main()
            elif settings_dialog.IsOpen():
                settings_dialog.Close()
            else:
                settings_dialog.Open(dlgtype=c4d.DLG_TYPE_ASYNC,
                                  pluginid=REAWOTE_PLUGIN_ID,
                                  defaultw=360,
                                  defaulth=380,
                                  subid=1)

        # function for filling up the listview with materials
        if id == ID.DIALOG_FOLDER_BUTTON:
            path = c4d.storage.LoadDialog(title="Choose material folder", flags=c4d.FILESELECT_DIRECTORY)
            if path == None:
                return True
            #python2
            try:
                path = path.decode("utf-8")
            except: 
                pass
            self.Reset() 

            self._listView.listOfTexture.clear()
            path_list.clear()
            path_lists.clear()
            checkbox_list.clear()
            
            self._treegui.Refresh()

            path_lists.append(path)
            target_folders = ["1K", "2K", "3K", "4K", "5K", "6K", "7K", "8K", "9K", "10K", "11K", "12K", "13K", "14K", "15K", "16K"]
            self.SetString(ID.DIALOG_FOLDER_LIST, path)
            # print(path)
            dir = os.listdir(path)

            #bitmaps = [file for file in dir if os.path.isfile(os.path.join(path, file))]

            same_path_dirs = []
            folder_dict = {}
            for root, dirs, files in os.walk(path):
                for dir in dirs:
                    if dir in target_folders:
                        # print(dir)
                        same_path_dirs.append(os.path.join(root, dir))
            # print(f"These are same_path_dirs:", same_path_dirs)

            for index, folder in enumerate(sorted(same_path_dirs)):
                files = os.listdir(folder)
                if files:
                    file_name_parts = files[0].split("_")
                    folder_name = "_".join(file_name_parts[:3])
                else:
                    # print("Files not found")
                    continue
                folder_path = os.path.join(path, folder)
                subdirs = [subdir for subdir in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, subdir))]
                folder_dict[folder] = True
                newID = len(self._listView.listOfTexture) + 1
                tex = TextureObject(folder_name.format(newID))
                self._listView.listOfTexture.append(tex)
                checkbox_list.append(tex)
                path_list.append(folder_path)
                # print(tex)
                # print(folder_path)
                # print(f"{folder} checkbox was created and added to list.")
                # print(path_list)
                # print(" ")
                self._treegui.Refresh()
                if folder_path:
                    dir_path = os.listdir(folder_path)
                    has_color = False
                    for file in dir_path:
                            try: 
                                parts = file.split(".")[0].split("_")
                                manufacturer = parts[0]
                                product_number = parts[1]
                                product = parts[2]
                                mapID = parts[3]
                                resolution = parts[4]
                                if mapID == "DIFF" or mapID == "COLOR" or mapID == "COL":
                                    has_color = True
                                if mapID == "DISP16":
                                    self.has_16b_disp = True
                                    self.has_disp = True
                                if mapID == "DISP":
                                    self.has_disp = True
                                if mapID == "AO":
                                    self.has_AO = True
                                if mapID == "IOR":
                                    self.has_Ior = True
                                if mapID == "NRM16":
                                    self.has_16b_normal = True
                            except:
                                pass
                    if self.has_AO:
                        self.SetBool(ID.DIALOG_MAP_AO_CB, True)
                        self.Enable(ID.DIALOG_MAP_AO_CB, True)
                    if self.has_disp:
                        self.SetBool(ID.DIALOG_MAP_DISPL_CB, True)
                        self.Enable(ID.DIALOG_MAP_DISPL_CB, True)
                    if self.has_16b_disp:
                        self.SetBool(ID.DIALOG_MAP_16B_DISPL_CB, True)
                        self.Enable(ID.DIALOG_MAP_16B_DISPL_CB, True)
                    if self.has_16b_normal:
                        self.SetBool(ID.DIALOG_MAP_16B_NORMAL_CB, True)
                        self.Enable(ID.DIALOG_MAP_16B_NORMAL_CB, True)
                    if self.has_Ior:
                        self.SetBool(ID.DIALOG_MAP_IOR_CB, False)
                        self.Enable(ID.DIALOG_MAP_IOR_CB, True)
                    if has_color:
                        self.material_folder = path
                        self.Enable(ID.DIALOG_LOAD_BUTTON, True)
                        self.SetError("")
                    # else:
                    #     self.SetError("One or more folders do not contain the correct Reawote material.")
            self.Enable(ID.DIALOG_LIST_BUTTON, True)
            self.Enable(ID.DIALOG_SELECT_ALL_BUTTON, True)
            self.Enable(ID.DIALOG_REFRESH_ALL_BUTTON, True)
            self.Enable(ID.DIALOG_ADD_TO_QUEUE_BUTTON, True)
            self.Enable(ID.DIALOG_CLEAN_BUTTON, True)
            self.Enable(ID.DIALOG_RENDERER_COMBOBOX, True)
            # self.SetInt32(ID.DIALOG_RENDERER_COMBOBOX, 6400)

            active_checkbox_list = []

        if id == ID.DIALOG_FOLDER_SECONDARY_BUTTON:
            path = c4d.storage.LoadDialog(title="Choose material folder", flags=c4d.FILESELECT_DIRECTORY)
            if path == None:
                return True
            #python2
            try:
                path = path.decode("utf-8")
            except: 
                pass
            self.Reset() 

            self._listView.listOfTexture.clear()
            path_list.clear()
            path_lists.clear()
            checkbox_list.clear()

            all_mat_list = []
            material_dict = {}
            mat_count = 0

            path_lists.append(path)
            target_folders = ["1K", "2K", "3K", "4K", "5K", "6K", "7K", "8K", "9K", "10K", "11K", "12K", "13K", "14K", "15K", "16K"]
            self.SetString(ID.DIALOG_FOLDER_LIST, path)
            # print(path)
            dir = os.listdir(path)
            dir.sort()
            print(f"Tohle je serazeny dir : {dir}")
            print("")
            print("")

            for file in dir:
                print(f"Tohle je file {file}")
                if os.path.isfile(os.path.join(path, file)):
                    try:
                        parts = file.split("_")
                        if len(parts) >= 3:
                            material_base_name = "_".join(parts[:3])
                        file_full_path = os.path.join(path, file)
                        print(f"Tohle je file_full_path {file_full_path}")
                        print(f"Tohle je material_base_name {material_base_name}")
                        if material_base_name not in material_dict:
                            material_dict[material_base_name] = [file_full_path]
                        else:
                            material_dict[material_base_name].append(file_full_path)
                    except:
                        print("Tak tohle passuju")
                        pass
                    print(" ")

            print(f"Tohle je material_dict a ne material_dict: {material_dict}")
            for file in material_dict.keys():
                newID = len(self._listView.listOfTexture) + 1
                tex = TextureObject(file.format(newID))
                self._listView.listOfTexture.append(tex)
                self._treegui.Refresh()
                print(f"pridavam tenhle key: {file}")

            for files in material_dict.values():
                all_mat_list.append(files)
            print(f"Tohle je all_mat_list: {all_mat_list}")

        if id == ID.DIALOG_SELECT_ALL_BUTTON:

            self.HideElement(ID.DIALOG_PREVIEW_GROUP, True)
            self.LayoutChanged(ID.DIALOG_HIDDEN_PREVIEW)
            
            select_all = True
            for item in checkbox_list:
                if item.IsSelected == False:
                    select_all = False
        
            if select_all == True:
                for item in checkbox_list:
                    item.Deselect()
            else:
                for item in checkbox_list:
                    item.Select()
            self._treegui.Refresh()

        if id == ID.DIALOG_ADD_TO_QUEUE_BUTTON:
            path = c4d.storage.LoadDialog(title="Choose material folder", flags=c4d.FILESELECT_DIRECTORY)
            path_lists.append(path)
            # print(path_lists)
            self.SetString(ID.DIALOG_FOLDER_LIST, path)
            # print(path)
            dir = os.listdir(path)
            target_folders = ["1K", "2K", "3K", "4K", "5K", "6K", "7K", "8K", "9K", "10K", "11K", "12K", "13K", "14K", "15K", "16K"]
            same_path_dirs = []
            folder_dict = {}

            for root, dirs, files in os.walk(path):
                for dir in dirs:
                    if dir in target_folders:
                        same_path_dirs.append(os.path.join(root, dir))
            # print(f"These are same_path_dirs:", same_path_dirs)
            for index, folder in enumerate(sorted(same_path_dirs)):
                files = os.listdir(folder)
                if files:
                    file_name_parts = files[0].split("_")
                    folder_name = "_".join(file_name_parts[:3])
                else:
                    # print("Files not found")
                    continue
                folder_path = os.path.join(path, folder)
                subdirs = [subdir for subdir in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, subdir))]
                folder_dict[folder] = True
                newID = len(self._listView.listOfTexture) + 1
                tex = TextureObject(folder_name.format(newID))
                self._listView.listOfTexture.append(tex)
                checkbox_list.append(tex)
                path_list.append(folder_path)
                # print(f"{folder} checkbox was created and added to list.")
                self._treegui.Refresh()
                if folder_path:
                    dir_path = os.listdir(folder_path)
                    has_color = False
                    for file in dir_path:
                            try: 
                                parts = file.split(".")[0].split("_")
                                manufacturer = parts[0]
                                product_number = parts[1]
                                product = parts[2]
                                mapID = parts[3]
                                resolution = parts[4]
                                if mapID == "DIFF" or mapID == "COLOR" or mapID == "COL":
                                    has_color = True
                                if mapID == "DISP16":
                                    self.has_16b_disp = True
                                    self.has_disp = True
                                if mapID == "DISP":
                                    self.has_disp = True
                                if mapID == "AO":
                                    self.has_AO = True
                                if mapID == "IOR":
                                    self.has_Ior = True
                                if mapID == "NRM16":
                                    self.has_16b_normal = True
                            except:
                                pass
                    if self.has_AO:
                        self.SetBool(ID.DIALOG_MAP_AO_CB, True)
                        self.Enable(ID.DIALOG_MAP_AO_CB, True)
                    if self.has_disp:
                        self.SetBool(ID.DIALOG_MAP_DISPL_CB, True)
                        self.Enable(ID.DIALOG_MAP_DISPL_CB, True)
                    if self.has_16b_disp:
                        self.SetBool(ID.DIALOG_MAP_16B_DISPL_CB, True)
                        self.Enable(ID.DIALOG_MAP_16B_DISPL_CB, True)
                    if self.has_16b_normal:
                        self.SetBool(ID.DIALOG_MAP_16B_NORMAL_CB, True)
                        self.Enable(ID.DIALOG_MAP_16B_NORMAL_CB, True)
                    if self.has_Ior:
                        self.SetBool(ID.DIALOG_MAP_IOR_CB, False)
                        self.Enable(ID.DIALOG_MAP_IOR_CB, True)
                    if has_color:
                        self.material_folder = path
                        self.Enable(ID.DIALOG_LOAD_BUTTON, True)
                        self.SetError("")
                    else:
                        self.SetError("One or more folders do not contain the correct Reawote material.")
                self.Enable(ID.DIALOG_LIST_BUTTON, True)
                self.Enable(ID.DIALOG_SELECT_ALL_BUTTON, True)
                self.Enable(ID.DIALOG_REFRESH_ALL_BUTTON, True)
                self.Enable(ID.DIALOG_ADD_TO_QUEUE_BUTTON, True)
                self.Enable(ID.DIALOG_CLEAN_BUTTON, True)
            active_checkbox_list = []

        if id == ID.DIALOG_REFRESH_ALL_BUTTON:
            while len(self._listView.listOfTexture) > 0:
                tex = self._listView.listOfTexture[0]
                self._listView.listOfTexture.remove(tex)
                checkbox_list.clear()
                path_list.clear()
            self._treegui.Refresh()
            # print(f"Path list: {path_list}")
            for path in path_lists:
                dir = os.listdir(path)
                target_folders = ["1K", "2K", "3K", "4K", "5K", "6K", "7K", "8K", "9K", "10K", "11K", "12K", "13K", "14K", "15K", "16K"]
                same_path_dirs = []
                folder_dict = {}
                for root, dirs, files in os.walk(path):
                    for dir in dirs:
                        if dir in target_folders:
                            same_path_dirs.append(os.path.join(root, dir))
                for index, folder in enumerate(sorted(same_path_dirs)):
                    files = os.listdir(folder)
                    if files:
                        file_name_parts = files[0].split("_")
                        folder_name = "_".join(file_name_parts[:3])
                    folder_path = os.path.join(path, folder)
                    subdirs = [subdir for subdir in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, subdir))]
                    folder_dict[folder] = True
                    newID = len(self._listView.listOfTexture) + 1
                    tex = TextureObject(folder_name.format(newID))
                    self._listView.listOfTexture.append(tex)
                    checkbox_list.append(tex)
                    path_list.append(folder_path)
                    # print(f"{folder} checkbox was created and added to list.")
                    self._treegui.Refresh()
                    if folder_path:
                        dir_path = os.listdir(folder_path)
                        has_color = False
                        for file in dir_path:
                                try: 
                                    parts = file.split(".")[0].split("_")
                                    manufacturer = parts[0]
                                    product_number = parts[1]
                                    product = parts[2]
                                    mapID = parts[3]
                                    resolution = parts[4]
                                    if mapID == "DIFF" or mapID == "COLOR" or mapID == "COL":
                                        has_color = True
                                    if mapID == "DISP16":
                                        self.has_16b_disp = True
                                        self.has_disp = True
                                    if mapID == "DISP":
                                        self.has_disp = True
                                    if mapID == "AO":
                                        self.has_AO = True
                                    if mapID == "IOR":
                                        self.has_Ior = True
                                    if mapID == "NRM16":
                                        self.has_16b_normal = True
                                except:
                                    pass
                        if self.has_AO:
                            self.SetBool(ID.DIALOG_MAP_AO_CB, True)
                            self.Enable(ID.DIALOG_MAP_AO_CB, True)
                        if self.has_disp:
                            self.SetBool(ID.DIALOG_MAP_DISPL_CB, True)
                            self.Enable(ID.DIALOG_MAP_DISPL_CB, True)
                        if self.has_16b_disp:
                            self.SetBool(ID.DIALOG_MAP_16B_DISPL_CB, True)
                            self.Enable(ID.DIALOG_MAP_16B_DISPL_CB, True)
                        if self.has_16b_normal:
                            self.SetBool(ID.DIALOG_MAP_16B_NORMAL_CB, True)
                            self.Enable(ID.DIALOG_MAP_16B_NORMAL_CB, True)
                        if self.has_Ior:
                            self.SetBool(ID.DIALOG_MAP_IOR_CB, False)
                            self.Enable(ID.DIALOG_MAP_IOR_CB, True)
                        if has_color:
                            self.material_folder = path
                            self.Enable(ID.DIALOG_LOAD_BUTTON, True)
                            self.SetError("")
                        else:
                            self.SetError("One or more folders do not contain the correct Reawote material.")
                    self.Enable(ID.DIALOG_LIST_BUTTON, True)
                    self.Enable(ID.DIALOG_SELECT_ALL_BUTTON, True)
                    self.Enable(ID.DIALOG_REFRESH_ALL_BUTTON, True)
                    self.Enable(ID.DIALOG_ADD_TO_QUEUE_BUTTON, True)
                    self.Enable(ID.DIALOG_CLEAN_BUTTON, True)
                active_checkbox_list = []
                self._treegui.Refresh()
                self.HideElement(ID.DIALOG_PREVIEW_GROUP, True)
                self.LayoutChanged(ID.DIALOG_HIDDEN_PREVIEW)
        
        if id == ID.DIALOG_CLEAN_BUTTON:
            self.HideElement(ID.DIALOG_PREVIEW_GROUP, True)
            self.LayoutChanged(ID.DIALOG_HIDDEN_PREVIEW)
            self._listView.listOfTexture.clear()
            path_list.clear()
            path_lists.clear()
            checkbox_list.clear()
            mapID_list.clear()
            self._treegui.Refresh()
            self.Reset()

        # the main function for importing materials
        if id == ID.DIALOG_LIST_BUTTON:
            active_checkbox_list = []
            target_folders = ["1K", "2K", "3K", "4K", "5K", "6K", "7K", "8K", "9K", "10K", "11K", "12K", "13K", "14K", "15K", "16K"]
            folder_dict = {}
            for index, checkbox in enumerate(checkbox_list):
                if checkbox.IsSelected:
                    self.SetError("")
                    active_checkbox_list.append(index)
                    folder_path = path_list[index]
                    if folder_path:
                            # print(checkbox_list)
                            # print(checkbox)
                            has_color = False
                            load_AO = self.GetBool(ID.DIALOG_MAP_AO_CB)
                            load_displ = self.GetBool(ID.DIALOG_MAP_DISPL_CB)
                            load_16displ = self.GetBool(ID.DIALOG_MAP_16B_DISPL_CB)
                            load_ior = self.GetBool(ID.DIALOG_MAP_IOR_CB)
                            load_16nrm = self.GetBool(ID.DIALOG_MAP_16B_NORMAL_CB)

                            ############
                            # Physical #
                            ############    

                            if self.GetInt32(ID.DIALOG_RENDERER_COMBOBOX) == 6400:
                                mat = c4d.BaseMaterial(c4d.Mmaterial)
                                mat[c4d.MATERIAL_PREVIEWSIZE] = 10
                                bitmap = c4d.BaseShader(c4d.Xbitmap)
                                fusion_shader = None
                                dir = os.listdir(folder_path)
                                mapID_list.clear()
                                # tex folder
                                
                                for file in dir:
                                    if not file[0].isalpha():
                                        continue
                                    parts = file.split(".")[0].split("_")
                                    mapID = parts[3]   
                                    mapID_list.append(mapID)

                                for file in dir:
                                    if not file[0].isalpha():
                                        continue
                                    fullpath = os.path.join(folder_path, file)
                                    # print(f"MapID list: {mapID_list}")
                                    parts = file.split(".")[0].split("_")
                                    mat.SetName("_".join(parts[0:3]))
                                    mapID = parts[3]

                                    if mapID == "COL" or mapID == "COLOR":
                                        if not load_AO or "AO" not in mapID_list:
                                            bitmap[c4d.BITMAPSHADER_FILENAME] = fullpath
                                            mat.InsertShader(bitmap)
                                            mat[c4d.MATERIAL_COLOR_SHADER] = bitmap
                                        else:
                                            if not fusion_shader:
                                                fusion_shader = c4d.BaseShader(c4d.Xfusion)
                                                fusion_shader.SetParameter(c4d.SLA_FUSION_MODE, c4d.SLA_FUSION_MODE_MULTIPLY, c4d.DESCFLAGS_SET_NONE)
                                                fusion_shader.SetParameter(c4d.SLA_FUSION_BLEND, 1.0, c4d.DESCFLAGS_SET_NONE)
                                                mat.InsertShader(fusion_shader)
                                                mat[c4d.MATERIAL_COLOR_SHADER] = fusion_shader
                                            bitmap = c4d.BaseShader(c4d.Xbitmap)
                                            bitmap.SetParameter(c4d.BITMAPSHADER_FILENAME, fullpath, c4d.DESCFLAGS_SET_NONE)
                                            fusion_shader.InsertShader(bitmap)
                                            fusion_shader.SetParameter(c4d.SLA_FUSION_BASE_CHANNEL, bitmap, c4d.DESCFLAGS_SET_NONE)

                                    elif load_AO and mapID == "AO":
                                        if not fusion_shader:
                                            fusion_shader = c4d.BaseShader(c4d.Xfusion)
                                            fusion_shader.SetParameter(c4d.SLA_FUSION_MODE, c4d.SLA_FUSION_MODE_MULTIPLY, c4d.DESCFLAGS_SET_NONE)
                                            fusion_shader[c4d.SLA_FUSION_BLEND] = 1.0
                                            mat.InsertShader(fusion_shader)
                                            mat[c4d.MATERIAL_COLOR_SHADER] = fusion_shader
                                        bitmap = c4d.BaseShader(c4d.Xbitmap)
                                        bitmap.SetParameter(c4d.BITMAPSHADER_FILENAME, fullpath, c4d.DESCFLAGS_SET_NONE)
                                        fusion_shader.InsertShader(bitmap)
                                        fusion_shader[c4d.SLA_FUSION_BLEND_CHANNEL] = bitmap

                                    elif mapID == "NRM" and (not load_16nrm or "NRM16" not in mapID_list):
                                        normal_shader = c4d.BaseShader(c4d.Xbitmap)
                                        mat[c4d.MATERIAL_USE_NORMAL] = True
                                        normal_shader[c4d.BITMAPSHADER_FILENAME] = fullpath
                                        mat[c4d.MATERIAL_NORMAL_SHADER] = normal_shader
                                        normal_shader[c4d.BITMAPSHADER_COLORPROFILE] = 1
                                        mat.InsertShader(normal_shader)

                                    elif mapID == "NRM16" and load_16nrm:
                                        normal_shader = c4d.BaseShader(c4d.Xbitmap)
                                        mat[c4d.MATERIAL_USE_NORMAL] = True
                                        normal_shader[c4d.BITMAPSHADER_FILENAME] = fullpath
                                        mat[c4d.MATERIAL_NORMAL_SHADER] = normal_shader
                                        normal_shader[c4d.BITMAPSHADER_COLORPROFILE] = 1
                                        mat.InsertShader(normal_shader)

                                    elif mapID == "BUMP":
                                        bump_shader = c4d.BaseShader(c4d.Xbitmap)
                                        bump_shader[c4d.BITMAPSHADER_FILENAME] = fullpath
                                        mat[c4d.MATERIAL_BUMP_SHADER] = bump_shader
                                        mat.InsertShader(bump_shader)
                                        mat[c4d.MATERIAL_USE_BUMP] = True

                                    elif mapID == "ROUGH":
                                        rough_shader = c4d.BaseShader(c4d.Xbitmap)
                                        rough_shader.SetParameter(c4d.BITMAPSHADER_FILENAME, fullpath, c4d.DESCFLAGS_SET_NONE)
                                        rough_shader[c4d.BITMAPSHADER_FILENAME] = fullpath
                                        mat.InsertShader(rough_shader)
                                        bases = [c4d.REFLECTION_LAYER_LAYER_DATA + c4d.REFLECTION_LAYER_LAYER_SIZE * 4]
                                        for base in bases:
                                            mat[base + c4d.REFLECTION_LAYER_MAIN_DISTRIBUTION] = 3
                                            mat[base + c4d.REFLECTION_LAYER_MAIN_VALUE_ROUGHNESS] = 100
                                            mat[base + c4d.REFLECTION_LAYER_MAIN_SHADER_ROUGHNESS] = rough_shader

                                    elif mapID == "DISP" and (not load_16displ or "DISP16" not in mapID_list) and load_displ:
                                        disp_shader = c4d.BaseShader(c4d.Xbitmap)
                                        disp_shader[c4d.BITMAPSHADER_FILENAME] = fullpath
                                        mat[c4d.MATERIAL_DISPLACEMENT_SHADER] = disp_shader
                                        disp_shader[c4d.BITMAPSHADER_COLORPROFILE] = 1
                                        mat.InsertShader(disp_shader)
                                        mat[c4d.MATERIAL_USE_DISPLACEMENT] = True

                                    elif mapID == "DISP16" in file and load_displ and load_16displ:
                                        disp_shader = c4d.BaseShader(c4d.Xbitmap)
                                        disp_shader[c4d.BITMAPSHADER_FILENAME] = fullpath
                                        mat[c4d.MATERIAL_DISPLACEMENT_SHADER] = disp_shader
                                        disp_shader[c4d.BITMAPSHADER_COLORPROFILE] = 1
                                        mat.InsertShader(disp_shader)
                                        mat[c4d.MATERIAL_USE_DISPLACEMENT] = True

                                    elif mapID == "OPAC":
                                        opac_shader = c4d.BaseShader(c4d.Xbitmap)
                                        opac_shader[c4d.BITMAPSHADER_FILENAME] = fullpath
                                        mat[c4d.MATERIAL_ALPHA_SHADER] = opac_shader
                                        mat.InsertShader(opac_shader)
                                        mat[c4d.MATERIAL_USE_ALPHA] = True

                                doc = c4d.documents.GetActiveDocument()
                                doc.StartUndo()
                                doc.InsertMaterial(mat)
                                doc.AddUndo(c4d.UNDOTYPE_NEW, mat)
                                doc.EndUndo()
                                material_to_add.append(mat)                                   
                                self.SetString(ID.DIALOG_ERROR, "")

                            ##########
                            # Corona #
                            ##########
                    
                            if self.GetInt32(ID.DIALOG_RENDERER_COMBOBOX) == 6401:

                                if not c4d.plugins.FindPlugin(1030480):
                                    c4d.gui.MessageDialog("Corona is not installed")
                                    return

                                mat = c4d.BaseMaterial(ID.CORONA_STR_MATERIAL_PHYSICAL)
                                mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_ROUGHNESS_MODE, ID.CORONA_PHYSICAL_MATERIAL_ROUGHNESS_MODE_GLOSSINESS, c4d.DESCFLAGS_SET_NONE)
                                mat.SetParameter(ID.CORONA_MATERIAL_PREVIEWSIZE, ID.CORONA_MATERIAL_PREVIEWSIZE_1024, c4d.DESCFLAGS_SET_NONE)
                                mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_BASE_IOR_VALUE, 1.56, c4d.DESCFLAGS_SET_NONE)
                                fusion_shader = None
                                dir = os.listdir(folder_path)
                                mapID_list.clear()

                                displ_loaded = False
                                nrm_loaded = False

                                for file in dir:
                                    if not file[0].isalpha():
                                        continue
                                    parts = file.split(".")[0].split("_")
                                    mapID = parts[3]   
                                    mapID_list.append(mapID)

                                for file in dir:
                                    if not file[0].isalpha():
                                        continue
                                    fullpath = os.path.join(folder_path, file)
                                    # print(f"MapID list: {mapID_list}")
                                    parts = file.split(".")[0].split("_")
                                    mat.SetName("_".join(parts[0:3]))
                                    mapID = parts[3]

                                    if mapID == "COL" or mapID == "COLOR":
                                        mat.SetName("_".join(parts[0:3]))
                                        if not load_AO:
                                            bitmap = c4d.BaseShader(c4d.Xbitmap)
                                            bitmap.SetParameter(c4d.BITMAPSHADER_FILENAME, fullpath, c4d.DESCFLAGS_SET_NONE)
                                            mat.InsertShader(bitmap)
                                            mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_BASE_COLOR_TEXTURE, bitmap, c4d.DESCFLAGS_SET_NONE)
                                        else:
                                            if not fusion_shader:
                                                fusion_shader = c4d.BaseShader(c4d.Xfusion)
                                                fusion_shader.SetParameter(c4d.SLA_FUSION_MODE, c4d.SLA_FUSION_MODE_MULTIPLY, c4d.DESCFLAGS_SET_NONE)
                                                fusion_shader.SetParameter(c4d.SLA_FUSION_BLEND, 1.0, c4d.DESCFLAGS_SET_NONE)
                                                mat.InsertShader(fusion_shader)
                                                mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_BASE_COLOR_TEXTURE, fusion_shader, c4d.DESCFLAGS_SET_NONE)
                                            bitmap = c4d.BaseShader(c4d.Xbitmap)
                                            bitmap.SetParameter(c4d.BITMAPSHADER_FILENAME, fullpath, c4d.DESCFLAGS_SET_NONE)
                                            fusion_shader.InsertShader(bitmap)
                                            fusion_shader.SetParameter(c4d.SLA_FUSION_BASE_CHANNEL, bitmap, c4d.DESCFLAGS_SET_NONE)

                                    elif mapID == "NRM" and nrm_loaded == False:
                                        bitmap = c4d.BaseShader(c4d.Xbitmap)
                                        bitmap.SetParameter(c4d.BITMAPSHADER_FILENAME, fullpath, c4d.DESCFLAGS_SET_NONE)
                                        texture = c4d.BaseShader(ID.PLUGINID_CORONA4D_NORMALSHADER)
                                        texture.SetParameter(ID.CORONA_NORMALMAP_TEXTURE, bitmap, c4d.DESCFLAGS_SET_NONE)
                                        texture.SetParameter(ID.CORONA_NORMALMAP_FLIP_G, True, c4d.DESCFLAGS_SET_NONE)
                                        mat.InsertShader(bitmap)
                                        mat.InsertShader(texture)
                                        mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_BASE_BUMPMAPPING_ENABLE, True, c4d.DESCFLAGS_SET_NONE)
                                        mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_BASE_BUMPMAPPING_VALUE, 1.0, c4d.DESCFLAGS_SET_NONE)
                                        mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_BASE_BUMPMAPPING_TEXTURE, texture, c4d.DESCFLAGS_SET_NONE)

                                    elif load_displ and mapID == "DISP" and not load_16displ:
                                        bitmap = c4d.BaseShader(c4d.Xbitmap)
                                        bitmap.SetParameter(c4d.BITMAPSHADER_FILENAME, fullpath, c4d.DESCFLAGS_SET_NONE)
                                        mat.InsertShader(bitmap)
                                        mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_DISPLACEMENT, True, c4d.DESCFLAGS_SET_NONE)
                                        mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_DISPLACEMENT_TEXTURE, bitmap, c4d.DESCFLAGS_SET_NONE)
                                        mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_DISPLACEMENT_MIN_LEVEL, 0, c4d.DESCFLAGS_SET_NONE)
                                        mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_DISPLACEMENT_MAX_LEVEL, 1, c4d.DESCFLAGS_SET_NONE)

                                    elif load_AO and mapID == "AO":
                                        if not fusion_shader:
                                            fusion_shader = c4d.BaseShader(c4d.Xfusion)
                                            fusion_shader.SetParameter(c4d.SLA_FUSION_MODE, c4d.SLA_FUSION_MODE_MULTIPLY, c4d.DESCFLAGS_SET_NONE)
                                            fusion_shader.SetParameter(c4d.SLA_FUSION_BLEND, 1.0, c4d.DESCFLAGS_SET_NONE)
                                            mat.InsertShader(fusion_shader)
                                            mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_BASE_COLOR_TEXTURE, fusion_shader, c4d.DESCFLAGS_SET_NONE)
                                        bitmap = c4d.BaseShader(c4d.Xbitmap)
                                        bitmap.SetParameter(c4d.BITMAPSHADER_FILENAME, fullpath, c4d.DESCFLAGS_SET_NONE)
                                        fusion_shader.InsertShader(bitmap)
                                        fusion_shader.SetParameter(c4d.SLA_FUSION_BLEND_CHANNEL, bitmap, c4d.DESCFLAGS_SET_NONE)

                                    elif mapID == "OPAC":
                                        bitmap = c4d.BaseShader(c4d.Xbitmap)
                                        bitmap.SetParameter(c4d.BITMAPSHADER_FILENAME, fullpath, c4d.DESCFLAGS_SET_NONE)
                                        mat.InsertShader(bitmap)
                                        mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_ALPHA, True, c4d.DESCFLAGS_SET_NONE)
                                        mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_ALPHA_TEXTURE, bitmap, c4d.DESCFLAGS_SET_NONE)

                                    elif mapID == "GLOSS":
                                        bitmap = c4d.BaseShader(c4d.Xbitmap)
                                        bitmap.SetParameter(c4d.BITMAPSHADER_FILENAME, fullpath, c4d.DESCFLAGS_SET_NONE)
                                        mat.InsertShader(bitmap)
                                        mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_BASE_ROUGHNESS_TEXTURE, bitmap, c4d.DESCFLAGS_SET_NONE)
                                        mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_BASE_ROUGHNESS_VALUE, 100.0, c4d.DESCFLAGS_SET_NONE)

                                    elif mapID == "REFL":
                                        bitmap = c4d.BaseShader(c4d.Xbitmap)
                                        bitmap.SetParameter(c4d.BITMAPSHADER_FILENAME, fullpath, c4d.DESCFLAGS_SET_NONE)
                                        mat.InsertShader(bitmap)
                                        mat.SetParameter(ID.CORONA_MATERIAL_REFLECT, True, c4d.DESCFLAGS_SET_NONE)
                                        mat.SetParameter(ID.CORONA_REFLECT_TEXTURE, bitmap, c4d.DESCFLAGS_SET_NONE)

                                    elif mapID == "SSS":
                                        bitmap = c4d.BaseShader(c4d.Xbitmap)
                                        bitmap.SetParameter(c4d.BITMAPSHADER_FILENAME, fullpath, c4d.DESCFLAGS_SET_NONE)
                                        mat.InsertShader(bitmap)
                                        mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_SSS, True, c4d.DESCFLAGS_SET_NONE)
                                        mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_VOLUME_SSS_TEXTURE, bitmap, c4d.DESCFLAGS_SET_NONE)

                                    elif mapID == "SSSABSORB":
                                        bitmap = c4d.BaseShader(c4d.Xbitmap)
                                        bitmap.SetParameter(c4d.BITMAPSHADER_FILENAME, fullpath, c4d.DESCFLAGS_SET_NONE)
                                        mat.InsertShader(bitmap)
                                        mat.SetParameter(ID.CORONA_MATERIAL_VOLUME, True, c4d.DESCFLAGS_SET_NONE)
                                        mat.SetParameter(ID.CORONA_VOLUME_ABSORPTION_TEXTURE, bitmap, c4d.DESCFLAGS_SET_NONE)

                                    elif load_ior and mapID == "IOR":
                                        bitmap = c4d.BaseShader(c4d.Xbitmap)
                                        bitmap.SetParameter(c4d.BITMAPSHADER_FILENAME, fullpath, c4d.DESCFLAGS_SET_NONE)
                                        mat.InsertShader(bitmap)
                                        mat.SetParameter(ID.CORONA_REFLECT_FRESNELLOR_TEXTURE, bitmap, c4d.DESCFLAGS_SET_NONE)

                                    elif mapID == "METAL":
                                        bitmap = c4d.BaseShader(c4d.Xbitmap)
                                        bitmap.SetParameter(c4d.BITMAPSHADER_FILENAME, fullpath, c4d.DESCFLAGS_SET_NONE)
                                        mat.InsertShader(bitmap)
                                        mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_METALLIC_MODE_TEXTURE, bitmap, c4d.DESCFLAGS_SET_NONE)

                                    elif load_16nrm and mapID == "NRM16" or mapID == "NRM":
                                        if mapID == "NRM16":
                                            bitmap = c4d.BaseShader(c4d.Xbitmap)
                                            bitmap.SetParameter(c4d.BITMAPSHADER_FILENAME, fullpath, c4d.DESCFLAGS_SET_NONE)
                                            texture = c4d.BaseShader(ID.PLUGINID_CORONA4D_NORMALSHADER)
                                            texture.SetParameter(ID.CORONA_NORMALMAP_TEXTURE, bitmap, c4d.DESCFLAGS_SET_NONE)
                                            texture.SetParameter(ID.CORONA_NORMALMAP_FLIP_G, True, c4d.DESCFLAGS_SET_NONE)
                                            mat.InsertShader(bitmap)
                                            mat.InsertShader(texture)
                                            mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_BASE_BUMPMAPPING_ENABLE, True, c4d.DESCFLAGS_SET_NONE)
                                            mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_BASE_BUMPMAPPING_VALUE, 1.0, c4d.DESCFLAGS_SET_NONE)
                                            mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_BASE_BUMPMAPPING_TEXTURE, texture, c4d.DESCFLAGS_SET_NONE)
                                            nrm_loaded = True
                                        elif mapID == "NRM" and nrm_loaded == False:
                                            bitmap = c4d.BaseShader(c4d.Xbitmap)
                                            bitmap.SetParameter(c4d.BITMAPSHADER_FILENAME, fullpath, c4d.DESCFLAGS_SET_NONE)
                                            texture = c4d.BaseShader(ID.PLUGINID_CORONA4D_NORMALSHADER)
                                            texture.SetParameter(ID.CORONA_NORMALMAP_TEXTURE, bitmap, c4d.DESCFLAGS_SET_NONE)
                                            texture.SetParameter(ID.CORONA_NORMALMAP_FLIP_G, True, c4d.DESCFLAGS_SET_NONE)
                                            mat.InsertShader(bitmap)
                                            mat.InsertShader(texture)
                                            mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_BASE_BUMPMAPPING_ENABLE, True, c4d.DESCFLAGS_SET_NONE)
                                            mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_BASE_BUMPMAPPING_VALUE, 1.0, c4d.DESCFLAGS_SET_NONE)
                                            mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_BASE_BUMPMAPPING_TEXTURE, texture, c4d.DESCFLAGS_SET_NONE)

                                    elif load_displ and load_16displ and mapID == "DISP16" or mapID == "DISP":
                                        if mapID == "DISP16":
                                            bitmap = c4d.BaseShader(c4d.Xbitmap)
                                            bitmap.SetParameter(c4d.BITMAPSHADER_FILENAME, fullpath, c4d.DESCFLAGS_SET_NONE)
                                            mat.InsertShader(bitmap)
                                            mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_DISPLACEMENT, True, c4d.DESCFLAGS_SET_NONE)
                                            mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_DISPLACEMENT_TEXTURE, bitmap, c4d.DESCFLAGS_SET_NONE)
                                            mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_DISPLACEMENT_MIN_LEVEL, 0, c4d.DESCFLAGS_SET_NONE)
                                            mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_DISPLACEMENT_MAX_LEVEL, 1, c4d.DESCFLAGS_SET_NONE)
                                            displ_loaded = True
                                        elif mapID == "DISP" and load_displ and displ_loaded == False:
                                            bitmap = c4d.BaseShader(c4d.Xbitmap)
                                            bitmap.SetParameter(c4d.BITMAPSHADER_FILENAME, fullpath, c4d.DESCFLAGS_SET_NONE)
                                            mat.InsertShader(bitmap)
                                            mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_DISPLACEMENT, True, c4d.DESCFLAGS_SET_NONE)
                                            mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_DISPLACEMENT_TEXTURE, bitmap, c4d.DESCFLAGS_SET_NONE)
                                            mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_DISPLACEMENT_MIN_LEVEL, 0, c4d.DESCFLAGS_SET_NONE)
                                            mat.SetParameter(ID.CORONA_PHYSICAL_MATERIAL_DISPLACEMENT_MAX_LEVEL, 1, c4d.DESCFLAGS_SET_NONE)

                                    doc = c4d.documents.GetActiveDocument()
                                    doc.StartUndo()
                                    doc.InsertMaterial(mat)
                                    doc.AddUndo(c4d.UNDOTYPE_NEW, mat)
                                    doc.EndUndo()
                                    material_to_add.append(mat)                                   
                                    self.SetString(ID.DIALOG_ERROR, "")

                            #########
                            # V-ray #
                            #########

                            if self.GetInt32(ID.DIALOG_RENDERER_COMBOBOX) == 6402:

                                if not c4d.plugins.FindPlugin(1053272):
                                    c4d.gui.MessageDialog("V-ray is not installed")
                                    return

                                mat = c4d.BaseMaterial(ID.VRAY_MATERIAL)
                                fusion_shader = None
                                dir = os.listdir(folder_path)
                                mapID_list.clear()
                                mat[c4d.VRAY_SETTINGS_MATERIAL_PREVIEW_OVERRIDE] = True
                                mat[c4d.VRAY_SETTINGS_MATERIAL_PREVIEW_VIEWPORT_SIZE] = 10
                                
                                for file in dir:
                                    if not file[0].isalpha():
                                        continue
                                    parts = file.split(".")[0].split("_")
                                    mapID = parts[3]   
                                    mapID_list.append(mapID)

                                for file in dir:
                                    if not file[0].isalpha():
                                        continue
                                    fullpath = os.path.join(folder_path, file)
                                    # print(f"MapID list: {mapID_list}")
                                    parts = file.split(".")[0].split("_")
                                    mat.SetName("_".join(parts[0:3]))
                                    mapID = parts[3]

                                    if mapID == "COL":
                                        if not load_AO or "AO" not in mapID_list:
                                            bitmap = c4d.BaseShader(ID.VRAY_BITMAP)
                                            bitmap[c4d.BITMAPSHADER_FILENAME] = fullpath
                                            mat.InsertShader(bitmap)
                                            mat[c4d.BRDFVRAYMTL_DIFFUSE_TEXTURE] = bitmap
                                        else:
                                            if not fusion_shader:
                                                fusion_shader = c4d.BaseShader(c4d.Xfusion)
                                                fusion_shader[c4d.SLA_FUSION_MODE] = c4d.SLA_FUSION_MODE_MULTIPLY
                                                mat.InsertShader(fusion_shader)
                                                mat[c4d.BRDFVRAYMTL_DIFFUSE_TEXTURE] = fusion_shader
                                            bitmap = c4d.BaseShader(ID.VRAY_BITMAP)
                                            bitmap[c4d.BITMAPSHADER_FILENAME] = fullpath
                                            fusion_shader.InsertShader(bitmap)
                                            fusion_shader[c4d.SLA_FUSION_BASE_CHANNEL] = bitmap
                                    
                                    elif load_AO and mapID == "AO":
                                        if not fusion_shader:
                                            fusion_shader = c4d.BaseShader(c4d.Xfusion)
                                            fusion_shader[c4d.SLA_FUSION_MODE] = c4d.SLA_FUSION_MODE_MULTIPLY
                                            mat.InsertShader(fusion_shader)
                                            mat[c4d.BRDFVRAYMTL_DIFFUSE_TEXTURE] = fusion_shader
                                        bitmap = c4d.BaseShader(ID.VRAY_BITMAP)
                                        bitmap[c4d.BITMAPSHADER_FILENAME] = fullpath
                                        fusion_shader.InsertShader(bitmap)
                                        fusion_shader[c4d.SLA_FUSION_BLEND_CHANNEL] = bitmap

                                    elif mapID == "NRM" and (not load_16nrm or "NRM16" not in mapID_list):
                                        bitmap = c4d.BaseShader(ID.VRAY_BITMAP)
                                        bitmap[c4d.BITMAPSHADER_FILENAME] = fullpath
                                        bitmap[c4d.BITMAPSHADER_COLORPROFILE] = 1
                                        mat.InsertShader(bitmap)
                                        texture = c4d.BaseShader(ID.VRAY_NORMAL_MAP)
                                        texture[c4d.TEXNORMALBUMP_BUMP_TEX_COLOR] = bitmap
                                        texture[c4d.TEXNORMALBUMP_MAP_TYPE] = 1
                                        mat.InsertShader(texture)
                                        mat[c4d.BRDFVRAYMTL_BUMP_MAP] = texture
                                    
                                    elif mapID == "NRM16" and load_16nrm:
                                        bitmap = c4d.BaseShader(ID.VRAY_BITMAP)
                                        bitmap[c4d.BITMAPSHADER_FILENAME] = fullpath
                                        bitmap[c4d.BITMAPSHADER_COLORPROFILE] = 1
                                        mat.InsertShader(bitmap)
                                        texture = c4d.BaseShader(ID.VRAY_NORMAL_MAP)
                                        texture[c4d.TEXNORMALBUMP_BUMP_TEX_COLOR] = bitmap
                                        texture[c4d.TEXNORMALBUMP_MAP_TYPE] = 1
                                        mat.InsertShader(texture)
                                        mat[c4d.BRDFVRAYMTL_BUMP_MAP] = texture

                                    elif mapID == "GLOSS":
                                        bitmap = c4d.BaseShader(ID.VRAY_BITMAP)
                                        bitmap[c4d.BITMAPSHADER_FILENAME] = fullpath
                                        mat.InsertShader(bitmap)
                                        mat[c4d.BRDFVRAYMTL_REFLECT_GLOSSINESS_TEXTURE] = bitmap
                                        vec = c4d.Vector(255,255,255)
                                        mat[c4d.BRDFVRAYMTL_REFLECT_VALUE] = vec

                                    elif mapID == "METAL":
                                        bitmap = c4d.BaseShader(ID.VRAY_BITMAP)
                                        bitmap[c4d.BITMAPSHADER_FILENAME] = fullpath
                                        mat.InsertShader(bitmap)
                                        mat[c4d.BRDFVRAYMTL_METALNESS_TEXTURE] = bitmap

                                    elif mapID == "OPAC":
                                        bitmap = c4d.BaseShader(ID.VRAY_BITMAP)
                                        bitmap[c4d.BITMAPSHADER_FILENAME] = fullpath
                                        mat.InsertShader(bitmap)
                                        mat[c4d.BRDFVRAYMTL_OPACITY_COLOR_TEXTURE] = bitmap

                                    elif mapID == "SSS":
                                        bitmap = c4d.BaseShader(ID.VRAY_BITMAP)
                                        bitmap[c4d.BITMAPSHADER_FILENAME] = fullpath
                                        mat.InsertShader(bitmap)
                                        mat[c4d.BRDFVRAYMTL_TRANSLUCENCY_COLOR_TEXTURE] = bitmap
                                        mat[c4d.BRDFVRAYMTL_TRANSLUCENCY] = 6
                                    
                                    elif mapID == "SHEEN":
                                        bitmap = c4d.BaseShader(ID.VRAY_BITMAP)
                                        bitmap[c4d.BITMAPSHADER_FILENAME] = fullpath
                                        mat.InsertShader(bitmap)
                                        mat[c4d.BRDFVRAYMTL_SHEEN_COLOR_TEXTURE] = bitmap

                                    elif mapID == "SHEENGLOSS":
                                        bitmap = c4d.BaseShader(ID.VRAY_BITMAP)
                                        bitmap[c4d.BITMAPSHADER_FILENAME] = fullpath
                                        mat.InsertShader(bitmap)
                                        mat[c4d.BRDFVRAYMTL_SHEEN_GLOSSINESS_TEXTURE] = bitmap

                                doc = c4d.documents.GetActiveDocument()
                                doc.StartUndo()
                                doc.InsertMaterial(mat)
                                doc.AddUndo(c4d.UNDOTYPE_NEW, mat)
                                doc.EndUndo()
                                material_to_add.append(mat)                                   
                                self.SetString(ID.DIALOG_ERROR, "")

                            ############
                            # Redshift #
                            ############
                            
                            if self.GetInt32(ID.DIALOG_RENDERER_COMBOBOX) == 6403:

                                if not c4d.plugins.FindPlugin(1036219):
                                    c4d.gui.MessageDialog("Redshift is not installed")
                                    return

                                color_layer_node = None
                                color_layer_added = False
                                dir = os.listdir(folder_path)
                                doc = c4d.documents.GetActiveDocument()
                                render_data = doc.GetActiveRenderData()
                                render_data[c4d.RDATA_RENDERENGINE] = 1036219
                                c4d.EventAdd()

                                rs_node_space_id: maxon.Id = maxon.Id("com.redshift3d.redshift4c4d.class.nodespace")
                                output_node_id: maxon.Id = maxon.Id(("com.redshift3d.redshift4c4d.nodes.core.standardmaterial"))
                                displacement_node_id: maxon.Id = maxon.Id("com.redshift3d.redshift4c4d.nodes.core.displacement")

                                displacement_tex_map_input_port_node_id: maxon.String = "com.redshift3d.redshift4c4d.nodes.core.displacement.texmap"
                                displacement_out_port_id: maxon.String = "com.redshift3d.redshift4c4d.nodes.core.displacement.out"

                                color_input_port_in_output_node_id: maxon.String = "com.redshift3d.redshift4c4d.nodes.core.standardmaterial.base_color"
                                roughness_input_port_in_output_node_id: maxon.String = "com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refl_roughness"
                                metalness_input_port_in_output_node_id: maxon.String = "com.redshift3d.redshift4c4d.nodes.core.standardmaterial.metalness"
                                opacity_input_port_in_output_node_id: maxon.String = "com.redshift3d.redshift4c4d.nodes.core.standardmaterial.opacity_color"
                                subsurface_input_port_in_output_node_id: maxon.String = "com.redshift3d.redshift4c4d.nodes.core.standardmaterial.ms_color"
                                sheen_input_port_in_output_node_id: maxon.String = "com.redshift3d.redshift4c4d.nodes.core.standardmaterial.sheen_color"
                                sheengloss_input_port_in_output_node_id: maxon.String = "com.redshift3d.redshift4c4d.nodes.core.standardmaterial.sheen_roughness"
                                bumpmap_input_port_in_output_node_id: maxon.String = "com.redshift3d.redshift4c4d.nodes.core.standardmaterial.bump_input"
                                

                                texture_node_id: maxon.Id = maxon.Id("com.redshift3d.redshift4c4d.nodes.core.texturesampler")
                                texture_node_port_id: maxon.String = "com.redshift3d.redshift4c4d.nodes.core.texturesampler.tex0"
                                texture_nodepath_port_id: maxon.String = "path"
                                texture_nodepath_colorspace_id: maxon.String = "colorspace"
                                texture_color_out_port_id: maxon.String = "com.redshift3d.redshift4c4d.nodes.core.texturesampler.outcolor"


                                bump_node_id: maxon.Id = maxon.Id("com.redshift3d.redshift4c4d.nodes.core.bumpmap")
                                bump_in_port_id: maxon.String = "com.redshift3d.redshift4c4d.nodes.core.bumpmap.input"
                                bump_out_port_id: maxon.String = "com.redshift3d.redshift4c4d.nodes.core.bumpmap.out"
                                bump_type_in_port_id: maxon.String = "com.redshift3d.redshift4c4d.nodes.core.bumpmap.inputtype"

                                color_layer_node_id: maxon.Id = maxon.Id("com.redshift3d.redshift4c4d.nodes.core.rscolorlayer")
                                color_layer_color_in_port_id: maxon.String = "com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.base_color"
                                colorlayer_layer_one_in_port_id: maxon.String = "com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer1_color"
                                colorlayer_layer_one_blend_mode_in_port_id : maxon.String = "com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer1_blend_mode"
                                color_layer_color_out_port_id: maxon.String = "com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.outcolor"

                                mat: c4d.BaseMaterial = c4d.BaseMaterial(c4d.Mmaterial)
                                # parts = file.split(".")[0].split("_")
                                mat.SetName(checkbox)
                                mat[c4d.MATERIAL_PREVIEWSIZE] = 10
                                if not mat:
                                    raise MemoryError(f"{mat = }")
                                node_material: c4d.node_material = mat.GetNodeMaterialReference()
                                graph: maxon.GraphModelRef = node_material.CreateDefaultGraph(rs_node_space_id)
                                
                                doc.InsertMaterial(mat)
                                result: list[maxon.GraphNode] = []
                                maxon.GraphModelHelper.FindNodesByAssetId(graph, output_node_id, True, result)
                                if len(result) < 1:
                                    raise RuntimeError("Could not find standard node in material.")
                                output_node: maxon.GraphNode = result[0]
                                mapID_list.clear()
                                        
                                for file in dir:
                                    if not file[0].isalpha():
                                        continue
                                    parts = file.split(".")[0].split("_")
                                    mapID = parts[3]   
                                    mapID_list.append(mapID)

                                for file in dir:
                                    if not file[0].isalpha():
                                        continue
                                    # print(f"MapID list: {mapID_list}")
                                    parts = file.split(".")[0].split("_")
                                    mapID = parts[3]
                                    fullpath = os.path.join(folder_path, file)
                                    
                                    with graph.BeginTransaction() as transaction:
                                        
                                        if mapID == "COL" or mapID == "AO":
                                            if mapID == "COL" and (not load_AO or "AO" not in mapID_list):
                                                texture_node = graph.AddChild(maxon.Id(), texture_node_id)
                                                
                                                path_port = texture_node.GetInputs().FindChild(texture_node_port_id).FindChild(texture_nodepath_port_id)
                                                path_port.SetDefaultValue(maxon.Url(fullpath))

                                                texture_out_port: maxon.GraphNode = texture_node.GetOutputs().FindChild(texture_color_out_port_id)
                                                color_input_port_in_output_node : maxon.GraphNode = output_node.GetInputs().FindChild(color_input_port_in_output_node_id)
                                                texture_out_port.Connect(color_input_port_in_output_node)
                                                
                                                transaction.Commit()
                                            
                                            elif mapID == "COL":
                                                if color_layer_added == False:
                                                    color_layer_node = graph.AddChild(maxon.Id(), color_layer_node_id)
                                                    color_layer_out_port_node: maxon.GraphNode = color_layer_node.GetOutputs().FindChild(color_layer_color_out_port_id)
                                                    color_layer_input_port_in_output_node : maxon.GraphNode = output_node.GetInputs().FindChild(color_input_port_in_output_node_id)
                                                    color_layer_out_port_node.Connect(color_layer_input_port_in_output_node)
                                                    color_layer_added = True
                                                
                                                texture_node = graph.AddChild(maxon.Id(), texture_node_id)
                                                path_port = texture_node.GetInputs().FindChild(texture_node_port_id).FindChild(texture_nodepath_port_id)
                                                path_port.SetDefaultValue(maxon.Url(fullpath))
                                                texture_out_port: maxon.GraphNode = texture_node.GetOutputs().FindChild(texture_color_out_port_id)
                                                color_layer_color_in_port: maxon.GraphNode = color_layer_node.GetInputs().FindChild(color_layer_color_in_port_id)
                                                texture_out_port.Connect(color_layer_color_in_port)
                                                
                                                transaction.Commit()
                                            
                                            elif mapID == "AO" and load_AO:
                                                if color_layer_added == False:
                                                    color_layer_node = graph.AddChild(maxon.Id(), color_layer_node_id)
                                                    color_layer_out_port_node: maxon.GraphNode = color_layer_node.GetOutputs().FindChild(color_layer_color_out_port_id)
                                                    color_layer_input_port_in_output_node : maxon.GraphNode = output_node.GetInputs().FindChild(color_input_port_in_output_node_id)
                                                    color_layer_out_port_node.Connect(color_layer_input_port_in_output_node)
                                                    color_layer_added = True
                                                
                                                texture_node = graph.AddChild(maxon.Id(), texture_node_id)
                                                path_port = texture_node.GetInputs().FindChild(texture_node_port_id).FindChild(texture_nodepath_port_id)
                                                path_port.SetDefaultValue(maxon.Url(fullpath))
                                                texture_out_port: maxon.GraphNode = texture_node.GetOutputs().FindChild(texture_color_out_port_id)
                                                colorlayer_layer_one_in_port: maxon.GraphNode = color_layer_node.GetInputs().FindChild(colorlayer_layer_one_in_port_id)
                                                colorlayer_layer_one_blend_mode_in_port: maxon.GraphNode = color_layer_node.GetInputs().FindChild(colorlayer_layer_one_blend_mode_in_port_id)
                                                colorlayer_layer_one_blend_mode_in_port.SetDefaultValue(4)
                                                texture_out_port.Connect(colorlayer_layer_one_in_port)
                                                
                                                transaction.Commit()
                                            else:
                                                continue
                                        
                                        elif mapID == "ROUGH":
                                            texture_node = graph.AddChild(maxon.Id(), texture_node_id)
                                            path_port = texture_node.GetInputs().FindChild(texture_node_port_id).FindChild(texture_nodepath_port_id)
                                            path_port.SetDefaultValue(maxon.Url(fullpath))
                                            texture_out_port: maxon.GraphNode = texture_node.GetOutputs().FindChild(texture_color_out_port_id)
                                            roughness_input_port_in_output_node : maxon.GraphNode = output_node.GetInputs().FindChild(roughness_input_port_in_output_node_id)
                                            texture_out_port.Connect(roughness_input_port_in_output_node)
                                            
                                            transaction.Commit()
                                        
                                        elif mapID == "METAL":
                                            texture_node = graph.AddChild(maxon.Id(), texture_node_id)
                                            path_port = texture_node.GetInputs().FindChild(texture_node_port_id).FindChild(texture_nodepath_port_id)
                                            path_port.SetDefaultValue(maxon.Url(fullpath))
                                            texture_out_port: maxon.GraphNode = texture_node.GetOutputs().FindChild(texture_color_out_port_id)
                                            metalness_input_port_in_output_node : maxon.GraphNode = output_node.GetInputs().FindChild(metalness_input_port_in_output_node_id)
                                            texture_out_port.Connect(metalness_input_port_in_output_node)
                                            
                                            transaction.Commit()
                                        
                                        elif mapID == "OPAC":
                                            texture_node = graph.AddChild(maxon.Id(), texture_node_id)
                                            path_port = texture_node.GetInputs().FindChild(texture_node_port_id).FindChild(texture_nodepath_port_id)
                                            path_port.SetDefaultValue(maxon.Url(fullpath))
                                            texture_out_port: maxon.GraphNode = texture_node.GetOutputs().FindChild(texture_color_out_port_id)
                                            opacity_input_port_in_output_node : maxon.GraphNode = output_node.GetInputs().FindChild(opacity_input_port_in_output_node_id)
                                            texture_out_port.Connect(opacity_input_port_in_output_node)
                                            
                                            transaction.Commit()
                                        
                                        elif mapID == "SSS":
                                            texture_node = graph.AddChild(maxon.Id(), texture_node_id)
                                            path_port = texture_node.GetInputs().FindChild(texture_node_port_id).FindChild(texture_nodepath_port_id)
                                            path_port.SetDefaultValue(maxon.Url(fullpath))
                                            texture_out_port: maxon.GraphNode = texture_node.GetOutputs().FindChild(texture_color_out_port_id)
                                            subsurface_input_port_in_output_node : maxon.GraphNode = output_node.GetInputs().FindChild(subsurface_input_port_in_output_node_id)
                                            texture_out_port.Connect(subsurface_input_port_in_output_node)
                                            
                                            transaction.Commit()
                                        
                                        elif mapID == "SHEEN":
                                            texture_node = graph.AddChild(maxon.Id(), texture_node_id)
                                            path_port = texture_node.GetInputs().FindChild(texture_node_port_id).FindChild(texture_nodepath_port_id)
                                            path_port.SetDefaultValue(maxon.Url(fullpath))
                                            texture_out_port: maxon.GraphNode = texture_node.GetOutputs().FindChild(texture_color_out_port_id)
                                            sheen_input_port_in_output_node : maxon.GraphNode = output_node.GetInputs().FindChild(sheen_input_port_in_output_node_id)
                                            texture_out_port.Connect(sheen_input_port_in_output_node)
                                            
                                            transaction.Commit()
                                        
                                        elif mapID == "SHEENGLOSS":
                                            texture_node = graph.AddChild(maxon.Id(), texture_node_id)
                                            path_port = texture_node.GetInputs().FindChild(texture_node_port_id).FindChild(texture_nodepath_port_id)
                                            path_port.SetDefaultValue(maxon.Url(fullpath))
                                            texture_out_port: maxon.GraphNode = texture_node.GetOutputs().FindChild(texture_color_out_port_id)
                                            sheengloss_input_port_in_output_node : maxon.GraphNode = output_node.GetInputs().FindChild(sheengloss_input_port_in_output_node_id)
                                            texture_out_port.Connect(sheengloss_input_port_in_output_node)
                                            
                                            transaction.Commit()

                                        elif mapID == "NRM" and (not load_16nrm or "NRM16" not in mapID_list):
                                            bump_node = graph.AddChild(maxon.Id(), bump_node_id)
                                            bump_out_port_node: maxon.GraphNode = bump_node.GetOutputs().FindChild(bump_out_port_id)
                                            bumpmap_input_port_in_output_node : maxon.GraphNode = output_node.GetInputs().FindChild(bumpmap_input_port_in_output_node_id)
                                            bump_out_port_node.Connect(bumpmap_input_port_in_output_node)
                                            
                                            texture_node = graph.AddChild(maxon.Id(), texture_node_id)
                                            path_port = texture_node.GetInputs().FindChild(texture_node_port_id).FindChild(texture_nodepath_port_id)
                                            path_port.SetDefaultValue(maxon.Url(fullpath))
                                            colorspace_port = texture_node.GetInputs().FindChild(texture_node_port_id).FindChild(texture_nodepath_colorspace_id)
                                            colorspace_port.SetDefaultValue("RS_INPUT_COLORSPACE_SRGB_LINEAR")
                                            
                                            texture_out_port: maxon.GraphNode = texture_node.GetOutputs().FindChild(texture_color_out_port_id)
                                            bumpmap_input_port_in_output_node : maxon.GraphNode = bump_node.GetInputs().FindChild(bump_in_port_id)
                                            bumpmapTypeInputPortInoutput_node: maxon.GraphNode = bump_node.GetInputs().FindChild(bump_type_in_port_id)
                                            bumpmapTypeInputPortInoutput_node.SetDefaultValue(1)
                                            texture_out_port.Connect(bumpmap_input_port_in_output_node)
                                            
                                            transaction.Commit()
                                        
                                        elif mapID == "NRM16" and load_16nrm:
                                            bump_node = graph.AddChild(maxon.Id(), bump_node_id)
                                            bump_out_port_node: maxon.GraphNode = bump_node.GetOutputs().FindChild(bump_out_port_id)
                                            bumpmap_input_port_in_output_node : maxon.GraphNode = output_node.GetInputs().FindChild(bumpmap_input_port_in_output_node_id)
                                            bump_out_port_node.Connect(bumpmap_input_port_in_output_node)

                                            texture_node = graph.AddChild(maxon.Id(), texture_node_id)
                                            path_port = texture_node.GetInputs().FindChild(texture_node_port_id).FindChild(texture_nodepath_port_id)
                                            path_port.SetDefaultValue(maxon.Url(fullpath))

                                            colorspace_port = texture_node.GetInputs().FindChild(texture_node_port_id).FindChild(texture_nodepath_colorspace_id)
                                            colorspace_port.SetDefaultValue("RS_INPUT_COLORSPACE_SRGB_LINEAR")
                                            texture_out_port: maxon.GraphNode = texture_node.GetOutputs().FindChild(texture_color_out_port_id)
                                            bumpmap_input_port_in_output_node : maxon.GraphNode = bump_node.GetInputs().FindChild(bump_in_port_id)
                                            bumpmapTypeInputPortInoutput_node: maxon.GraphNode = bump_node.GetInputs().FindChild(bump_type_in_port_id)
                                            bumpmapTypeInputPortInoutput_node.SetDefaultValue(1)
                                            texture_out_port.Connect(bumpmap_input_port_in_output_node)

                                            transaction.Commit()
                                        
                                        elif mapID == "DISP" and (not load_16displ or "DISP16" not in mapID_list) and load_displ:
                                            displacement_node = graph.AddChild(maxon.Id(), displacement_node_id)
                                            displacementOutPortNode: maxon.GraphNode = displacement_node.GetOutputs().FindChild(displacement_out_port_id)

                                            node_material = mat.GetNodeMaterialReference()
                                            nodespaceId = maxon.Id("com.redshift3d.redshift4c4d.class.nodespace")
                                            nimbusRef = mat.GetNimbusRef(nodespaceId)
                                            graph = nimbusRef.GetGraph()
                                            endNodePath = nimbusRef.GetPath(maxon.NIMBUS_PATH.MATERIALENDNODE)
                                            endNode = graph.GetNode(endNodePath)
                                            toKamStrcit = endNode.GetInputs().FindChild("com.redshift3d.redshift4c4d.node.output.displacement")
                                            displacementOutPortNode.Connect(toKamStrcit)
                                            
                                            texture_node = graph.AddChild(maxon.Id(), texture_node_id)
                                            path_port = texture_node.GetInputs().FindChild(texture_node_port_id).FindChild(texture_nodepath_port_id)
                                            path_port.SetDefaultValue(maxon.Url(fullpath))
                                            texture_out_port: maxon.GraphNode = texture_node.GetOutputs().FindChild(texture_color_out_port_id)
                                            texMapInputPortInoutput_node: maxon.GraphNode = displacement_node.GetInputs().FindChild(displacement_tex_map_input_port_node_id)
                                            texture_out_port.Connect(texMapInputPortInoutput_node)

                                            transaction.Commit()

                                        elif mapID == "DISP16" and load_16displ and load_displ:
                                            displacement_node = graph.AddChild(maxon.Id(), displacement_node_id)
                                            displacementOutPortNode: maxon.GraphNode = displacement_node.GetOutputs().FindChild(displacement_out_port_id)

                                            node_material = mat.GetNodeMaterialReference()
                                            nodespaceId = maxon.Id("com.redshift3d.redshift4c4d.class.nodespace")
                                            nimbusRef = mat.GetNimbusRef(nodespaceId)
                                            graph = nimbusRef.GetGraph()
                                            endNodePath = nimbusRef.GetPath(maxon.NIMBUS_PATH.MATERIALENDNODE)
                                            endNode = graph.GetNode(endNodePath)
                                            toKamStrcit = endNode.GetInputs().FindChild("com.redshift3d.redshift4c4d.node.output.displacement")
                                            displacementOutPortNode.Connect(toKamStrcit)
                                            
                                            texture_node = graph.AddChild(maxon.Id(), texture_node_id)
                                            path_port = texture_node.GetInputs().FindChild(texture_node_port_id).FindChild(texture_nodepath_port_id)
                                            path_port.SetDefaultValue(maxon.Url(fullpath))
                                            texture_out_port: maxon.GraphNode = texture_node.GetOutputs().FindChild(texture_color_out_port_id)
                                            texMapInputPortInoutput_node: maxon.GraphNode = displacement_node.GetInputs().FindChild(displacement_tex_map_input_port_node_id)
                                            texture_out_port.Connect(texMapInputPortInoutput_node)

                                            transaction.Commit()

                                    c4d.EventAdd()

                                doc.InsertMaterial(mat)
                            
                            ##########
                            # Octane #
                            ##########
                            
                            if self.GetInt32(ID.DIALOG_RENDERER_COMBOBOX) == 6404:

                                if not c4d.plugins.FindPlugin(1029525):
                                    c4d.gui.MessageDialog("Octane is not installed")
                                    return

                                doc = c4d.documents.GetActiveDocument()
                                dir = os.listdir(folder_path)
                                mat = c4d.BaseMaterial(ID.OCTANE_MATERIAL)
                                mat[c4d.OCT_MATERIAL_TYPE] = 2516
                                mat[ID.OCTANE_BSDF_MODEL] = 2
                                mat[c4d.OCT_MATERIAL_PREVIEWSIZE] = 10
                                mat.SetName(checkbox)
                                mapID_list.clear()

                                multiply_loaded = False
                                multiply = None
                                
                                for file in dir:
                                    if not file[0].isalpha():
                                        continue
                                    parts = file.split(".")[0].split("_")
                                    mapID = parts[3]   
                                    mapID_list.append(mapID)

                                for file in dir:
                                    if not file[0].isalpha():
                                        continue
                                    fullpath = os.path.join(folder_path, file)
                                    # print(f"MapID list: {mapID_list}")
                                    parts = file.split(".")[0].split("_")
                                    mat.SetName("_".join(parts[0:3]))
                                    mapID = parts[3]
                                
                                    if mapID == "COL":
                                        if not load_AO or "AO" not in mapID_list:
                                            bitmap = c4d.BaseShader(ID.OCTANE_TEXTURE)
                                            bitmap[c4d.IMAGETEXTURE_FILE] = fullpath
                                            mat.InsertShader(bitmap)
                                            mat[c4d.OCT_MATERIAL_DIFFUSE_LINK] = bitmap
                                        else:
                                            bitmap = c4d.BaseShader(ID.OCTANE_TEXTURE)
                                            if multiply_loaded == False:
                                                multiply = c4d.BaseShader(ID.OCTANE_MULTIPLY)
                                                mat.InsertShader(multiply)
                                                multiply_loaded = True
                                            multiply[c4d.MULTIPLY_TEXTURE1] = bitmap
                                            bitmap[c4d.IMAGETEXTURE_FILE] = fullpath
                                            mat.InsertShader(bitmap)  
                                            mat[c4d.OCT_MATERIAL_DIFFUSE_LINK] = multiply
                                    
                                    elif load_AO and mapID == "AO":
                                        bitmap = c4d.BaseShader(ID.OCTANE_TEXTURE)
                                        if multiply_loaded == False:
                                            multiply = c4d.BaseShader(ID.OCTANE_MULTIPLY)
                                            mat.InsertShader(multiply)
                                            multiply_loaded = True
                                        multiply[c4d.MULTIPLY_TEXTURE2] = bitmap
                                        bitmap[c4d.IMAGETEXTURE_FILE] = fullpath
                                        mat.InsertShader(bitmap)
                                        mat[c4d.OCT_MATERIAL_DIFFUSE_LINK] = multiply
                                    
                                    elif mapID == "ROUGH":
                                        bitmap = c4d.BaseShader(ID.OCTANE_TEXTURE)
                                        bitmap[c4d.IMAGETEXTURE_FILE] = fullpath
                                        bitmap[c4d.IMAGETEXTURE_GAMMA] = 1.0
                                        bitmap[c4d.IMAGETEXTURE_MODE] = 1
                                        mat.InsertShader(bitmap)
                                        mat[c4d.OCT_MATERIAL_ROUGHNESS_LINK] = bitmap

                                    elif mapID == "NRM" and (not load_16nrm or "NRM16" not in mapID_list):
                                        bitmap = c4d.BaseShader(ID.OCTANE_TEXTURE)
                                        bitmap[c4d.IMAGETEXTURE_FILE] = fullpath
                                        mat.InsertShader(bitmap)
                                        mat[c4d.OCT_MATERIAL_NORMAL_LINK] = bitmap
                                        
                                    elif mapID == "NRM16" and load_16nrm:
                                        bitmap = c4d.BaseShader(ID.OCTANE_TEXTURE)
                                        bitmap[c4d.IMAGETEXTURE_FILE] = fullpath
                                        mat.InsertShader(bitmap)
                                        mat[c4d.OCT_MATERIAL_NORMAL_LINK] = bitmap
                                    
                                    elif mapID == "DISP" and (not load_16displ or "DISP16" not in mapID_list) and load_displ:
                                        bitmap = c4d.BaseShader(ID.OCTANE_TEXTURE)
                                        displacement = c4d.BaseShader(ID.OCTANE_DISPLACEMENT)
                                        displacement[c4d.DISPLACEMENT_AMOUNT] = 1.0
                                        displacement[c4d.DISPLACEMENT_LEVELOFDETAIL] = 10
                                        displacement[c4d.DISPLACEMENT_TEXTURE] = bitmap
                                        bitmap[c4d.IMAGETEXTURE_FILE] = fullpath
                                        bitmap[c4d.IMAGETEXTURE_GAMMA] = 1.0
                                        bitmap[c4d.IMAGETEXTURE_MODE] = 1
                                        mat.InsertShader(displacement)
                                        mat.InsertShader(bitmap)
                                        mat[c4d.OCT_MATERIAL_DISPLACEMENT_LINK] = displacement
                                    
                                    elif mapID == "DISP16" and load_16displ and load_displ:
                                        bitmap = c4d.BaseShader(ID.OCTANE_TEXTURE)
                                        displacement = c4d.BaseShader(ID.OCTANE_DISPLACEMENT)
                                        displacement[c4d.DISPLACEMENT_AMOUNT] = 1.0
                                        displacement[c4d.DISPLACEMENT_LEVELOFDETAIL] = 10
                                        displacement[c4d.DISPLACEMENT_TEXTURE] = bitmap
                                        bitmap[c4d.IMAGETEXTURE_FILE] = fullpath
                                        bitmap[c4d.IMAGETEXTURE_GAMMA] = 1.0
                                        bitmap[c4d.IMAGETEXTURE_MODE] = 1
                                        mat.InsertShader(displacement)
                                        mat.InsertShader(bitmap)
                                        mat[c4d.OCT_MATERIAL_DISPLACEMENT_LINK] = displacement
                                    
                                    elif mapID == "OPAC":
                                        bitmap = c4d.BaseShader(ID.OCTANE_TEXTURE)
                                        bitmap[c4d.IMAGETEXTURE_FILE] = fullpath
                                        bitmap[c4d.IMAGETEXTURE_GAMMA] = 1.0
                                        bitmap[c4d.IMAGETEXTURE_MODE] = 1
                                        mat.InsertShader(bitmap)
                                        mat[c4d.OCT_MATERIAL_OPACITY_LINK] = bitmap
                                    
                                    elif mapID == "METAL":
                                        bitmap = c4d.BaseShader(ID.OCTANE_TEXTURE)
                                        bitmap[c4d.IMAGETEXTURE_FILE] = fullpath
                                        bitmap[c4d.IMAGETEXTURE_GAMMA] = 1.0
                                        bitmap[c4d.IMAGETEXTURE_MODE] = 1
                                        mat.InsertShader(bitmap)
                                        mat[c4d.OCT_MAT_SPECULAR_MAP_LINK] = bitmap

                                    elif mapID == "SHEEN":
                                        bitmap = c4d.BaseShader(ID.OCTANE_TEXTURE)
                                        bitmap[c4d.IMAGETEXTURE_FILE] = fullpath
                                        mat.InsertShader(bitmap)
                                        mat[c4d.OCT_MAT_SHEEN_LINK] = bitmap

                                doc.InsertMaterial(mat)
                                

                elif len(active_checkbox_list) == 0:
                    self.SetError("No materials were selected.")
                c4d.EventAdd()
            return True
        
    def SetError(self, message):
        if not message:
            message = ""
        self.SetString(ID.DIALOG_ERROR, message)

    def SetListItems(self, message):
        if not message:
            message= ""
            self.SetString(ID.DIALOG_FOLDER_LIST, message)

    def Reset(self):
        
        self.SetString(ID.DIALOG_FOLDER_LIST, "")
        self.Enable(ID.DIALOG_SELECT_ALL_BUTTON, False)
        self.Enable(ID.DIALOG_REFRESH_ALL_BUTTON, False)
        self.Enable(ID.DIALOG_LIST_BUTTON, False)
        self.Enable(ID.DIALOG_ADD_TO_QUEUE_BUTTON, False)
        self.Enable(ID.DIALOG_CLEAN_BUTTON, False)

        self.has_16b_disp = False
        self.has_16b_normal = False
        self.has_disp = False
        self.has_AO = False
        self.has_Ior = False
        
        self.SetBool(ID.DIALOG_MAP_AO_CB, False)
        self.Enable(ID.DIALOG_MAP_AO_CB, False)
        self.SetBool(ID.DIALOG_MAP_DISPL_CB, False)
        self.Enable(ID.DIALOG_MAP_DISPL_CB, False)
        self.SetBool(ID.DIALOG_MAP_16B_DISPL_CB, False)
        self.Enable(ID.DIALOG_MAP_16B_DISPL_CB, False)
        self.SetBool(ID.DIALOG_MAP_16B_NORMAL_CB, False)
        self.Enable(ID.DIALOG_MAP_16B_NORMAL_CB, False)
        self.SetBool(ID.DIALOG_MAP_IOR_CB, False)
        self.Enable(ID.DIALOG_MAP_IOR_CB, False)
        self.Enable(ID.DIALOG_RENDERER_COMBOBOX, False)

        self.Enable(ID.DIALOG_LOAD_BUTTON, False)
        # self.Enable(ID.DIALOG_LIST_BUTTON, False)
        

class ReawoteMaterialLoader(plugins.CommandData):
    
    thread = None

    def __init__(self) -> None:
        super().__init__()
        global dialog
        if not dialog:
            dialog = ReawoteMaterialDialog()

    def Execute(self, doc):
        dialog.Open(dlgtype=c4d.DLG_TYPE_ASYNC, pluginid=REAWOTE_PLUGIN_ID, defaultw=475, defaulth=830, subid=1)
        return True
        
    def CoreMessage(self, id, msg):
        if id==REAWOTE_PLUGIN_ID:
            # print("Command received!")
            # print("Path is: " + self.thread.path)
            return True

        return gui.GeDialog.CoreMessage(self, id, msg)