import os
import shutil
class CCompress:
    def __init__(self):
        print '[Class Compress]'
        scriptDir       = os.path.dirname(__file__)
        
        # Default Folder
        self.tmpFolder = scriptDir + r'\01_Temp_Folder'
        self.saveFolder = scriptDir + r'\02_Save_Folder'
        
        self.toolPath = r'"C:\Program Files\7-Zip\7z.exe"'
    
    # compress more folder to a zip file
    def compress_more_folders(self, FolderList, dstName):
        # copy all files to temp folder: ToDo
        
        # compress tempFolder
        dstFolder = self.saveFolder + '\\' + dstName + '.zip'
        self.compress(self.tmpFolder,dstFolder)
        
        # restore temp folders 
        if os.path.exists(self.tmpFolder):
            deleteFolder = self.tmpFolder.replace('01_Temp_Folder', 'delete')
            os.rename(self.tmpFolder, deleteFolder)
            shutil.rmtree(deleteFolder)
            os.mkdir(self.tmpFolder)
        else:
            os.mkdir(self.tmpFolder)
    
    # compress a folder
    def compress(self, folderPath, dstFolder):
        compressCmd = self.toolPath + ' a ' + dstFolder + ' ' + folderPath
        print compressCmd
        os.system(compressCmd)
    
    #def set_tmp_folder(self, tmpFolder):
    #def set_store_folder(self, storeFolder):    
    