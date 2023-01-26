#******************************************************************************
# content     = 'TextureTransferTool'
#
# date        = 2022-06-05
# author      = Padmacumar Prabhaharan (PC)
# contact     = padmacumar@gmail.com
#******************************************************************************

import os
import maya.cmds as cmds
import shutil


#******************************************************************************
# Texture Transfer UI
#******************************************************************************


IMG_PATH = r"E:\Textures\img"


def textransfer_ui():
    ui_title = 'texture_transfer'
    if cmds.window(ui_title, exists=True):
        print('CLOSE duplicate window')
        cmds.deleteUI(ui_title)

    window = cmds.window(ui_title, title='Texture Transfer', width=400)

    cmds.columnLayout(adjustableColumn=True)

    # IMAGE
    cmds.image(image=IMG_PATH +"\\"+'texturetransfer_title.jpg')

    cmds.separator(height=20)

    cmds.text(label='Texture Path Here:', width=400, height=40)

    cmds.textField('loc_path', height=30)

    cmds.separator(height=20)

    cmds.rowLayout(numberOfColumns=2)

    cmds.button(label="Copy All",
                annotation="copies all the texture files in the scene to the given folder location",
                width=200, command=("copylink_all_confirm()"))
    cmds.button(label="Copy Selected",
                annotation="copies only the seleted texture files in the scene to the given folder location",
                width=200, command=("copylink_selected_confirm()"))
   
    cmds.setParent('..')

    cmds.separator(height=10)

    cmds.rowLayout(numberOfColumns=2)

    cmds.button(label="Link All",
                annotation="Links all the texture files in the scene to the given folder location",
                width=200, command=("link_all()"))
    cmds.button(label="Link Selected",
                annotation="Links only the selected texture files in the scene to the given folder location",
                width=200, command=("link_selected()")) 
   
    cmds.setParent('..')

    cmds.showWindow(window)
    
textransfer_ui()


#******************************************************************************
# Functions for Link options
#******************************************************************************
# 'Link Selected' Function

def link_selected():
    sel = cmds.ls(selection=True, type='file')
    for files in sel:
        inserted_path = cmds.textField("loc_path", query=True, text= True)
        source = (cmds.getAttr(files+ '.fileTextureName'))
        source_strip = source.split('/')
        img_name = source_strip[-1]
        #source_path = '/'.join(source_strip[:-1])
        new_path = (inserted_path + '/' + img_name)
        cmds.setAttr(files+'.fileTextureName' , new_path , type='string')
        print(new_path)
    link_confirm()

        
#******************************************************************************
# 'Link All' Function

def link_all():
    sel = cmds.ls(type='file')
    for files in sel:
        inserted_path = cmds.textField("loc_path", query=True, text= True)
        source = (cmds.getAttr(files+ '.fileTextureName'))
        source_strip = source.split('/')
        img_name = source_strip[-1]
        #source_path = '/'.join(source_strip[:-1])
        new_path = (inserted_path + '/' + img_name)
        cmds.setAttr(files+'.fileTextureName' , new_path , type='string')
        print(new_path)
    link_confirm()

        
#******************************************************************************
# Pop up for 'Link' Confirm

def link_confirm():
    result = cmds.confirmDialog(title='Link Complete!',
                                message='Texture files successfully linked to the path',
                                button=['OK'],
                                cancelButton='OK')
    print(result)


#******************************************************************************
# Functions for Copy / link options
#******************************************************************************
# 'Copy All' Function

def copy_all():
    sel = cmds.ls(type='file')
    for files in sel:
        inserted_path = cmds.textField("loc_path", query=True, text= True)
        source = (cmds.getAttr(files+ '.fileTextureName'))
        source_strip = source.split('/')
        img_name = source_strip[-1]
        source_path = '/'.join(source_strip[:-1])
        old_path = (source_path + '/' + img_name)
        new_path = (inserted_path + '/' + img_name)
        shutil.copy(old_path,new_path)
        print(new_path)
    copy_confirm()

#******************************************************************************
# 'Copy and Link All' Function

def copy_link_all():
    sel = cmds.ls(type='file')
    for files in sel:
        inserted_path = cmds.textField("loc_path", query=True, text= True)
        source = (cmds.getAttr(files+ '.fileTextureName'))
        source_strip = source.split('/')
        img_name = source_strip[-1]
        source_path = '/'.join(source_strip[:-1])
        old_path = (source_path + '/' + img_name)
        new_path = (inserted_path + '/' + img_name)
        shutil.copy(old_path,new_path)
        cmds.setAttr(files+'.fileTextureName' , new_path , type='string')
        print(new_path)
    copy_link_confirm()
    
#******************************************************************************
# 'Copy Selected' Function

def copy_selected():
    sel = cmds.ls(selection =True, type='file')
    for files in sel:
        inserted_path = cmds.textField("loc_path", query=True, text= True)
        source = (cmds.getAttr(files+ '.fileTextureName'))
        source_strip = source.split('/')
        img_name = source_strip[-1]
        source_path = '/'.join(source_strip[:-1])
        old_path = (source_path + '/' + img_name)
        new_path = (inserted_path + '/' + img_name)
        shutil.copy(old_path,new_path)
        print(new_path)
    copy_confirm()

#******************************************************************************
# 'Copy and Link' Selected Function

def copy_link_selected():
    sel = cmds.ls(selection =True, type='file')
    for files in sel:
        inserted_path = cmds.textField("loc_path", query=True, text= True)
        source = (cmds.getAttr(files+ '.fileTextureName'))
        source_strip = source.split('/')
        img_name = source_strip[-1]
        source_path = '/'.join(source_strip[:-1])
        old_path = (source_path + '/' + img_name)
        new_path = (inserted_path + '/' + img_name)
        shutil.copy(old_path,new_path)
        cmds.setAttr(files+'.fileTextureName' , new_path , type='string')
        print(new_path)
    copy_link_confirm()


#******************************************************************************
# Pop up for 'Copy and Link all' Option Confirmation

def copylink_all_confirm():
    result = cmds.confirmDialog(title='Copy and Link?',
                                message='Would you also like to link the textures?',
                                button=['Yes, Also Link', 'No, Just Copy', 'Cancel'],
                                defaultButton='No, Just Copy',
                                cancelButton='Cancel')

    print(result)

    # EXECUTE button
    if result == 'No, Just Copy':
        copy_all()

    elif result == 'Yes, Also Link':
        copy_link_all()

#******************************************************************************
# Pop up for 'Copy and Link selected' Option Confirmation

def copylink_selected_confirm():
    result = cmds.confirmDialog(title='Copy and Link?',
                                message='Would you also like to link the textures?',
                                button=['Yes, Also Link', 'No, Just Copy', 'Cancel'],
                                defaultButton='No, Just Copy',
                                cancelButton='Cancel')

    print(result)

    # EXECUTE button
    if result == 'No, Just Copy':
        copy_selected()

    elif result == 'Yes, Also Link':
        copy_link_selected()

#******************************************************************************
# Pop up for 'Copy' Confirm
def copy_confirm():
    result = cmds.confirmDialog(title='Copying Complete!',
                                message='Texture files successfully copied to the path',
                                button=['OK'],
                                cancelButton='OK')
    print(result)

#******************************************************************************
# Pop up for 'Copy and Link' Confirm
def copy_link_confirm():
    result = cmds.confirmDialog(title='Copy and Link Complete!',
                                message='Texture files successfully copied and linked to the path',
                                button=['OK'],
                                cancelButton='OK')
    print(result)



#******************************************************************************
#******************************************************************************