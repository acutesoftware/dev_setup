# deploy.py     written by Duncan Murray  25/8/2014
# (OLD - no longer used) quick and dirty script to make sure AIKIF programs
# are updated to LOCAL folder in order to assist with
# development of module from separate folders.

import os
import shutil 
import aikif.lib.cls_filelist as mod_fl



def main():

    print('Dont run this - use Anaconda')
    exit(1)

    # AIKIF
    src_root  = "T:\\user\\dev\\src\\python\\AIKIF\\" 
    dest_root = "C:\\Python34\\Lib\\site-packages\\aikif\\"
    files_to_synch = get_files_to_sync(src_root, 'aikif')
    copy_files_to_local_package(files_to_synch, src_root, dest_root, 'aikif')
    
    """
    # VAIS
    src_root  = "T:\\user\\dev\\src\\python\\virtual-AI-simulator\\" 
    dest_root = "C:\\Python34\\Lib\\site-packages\\vais\\"
    files_to_synch = get_files_to_sync(src_root, 'vais')
    copy_files_to_local_package(files_to_synch, src_root, dest_root, 'vais')
    """
    
def get_files_to_sync(src_root, txt_srch):
    flist = []
    with open(src_root + 'MANIFEST', 'r') as f:
        for line in f:
            if line[0:len(txt_srch)] == txt_srch: # 'aikif':
                flist.append(line[len(txt_srch)+1:].strip('\n'))
    return flist

def copy_files_to_local_package(files_to_synch, src_root, dest_root, txt):  
    files_copied = 0
    for tot_files, f in enumerate(files_to_synch):
        src = src_root + txt + os.sep +  f
        dst = dest_root +  f
        print("Checking " + f )
        if os.path.isfile(dst):
            try:
                if os.path.getmtime(src) > os.path.getmtime(dst):
                    shutil.copy2(src, dst)
                    print('Copied ' + f + '')
                    files_copied += 1
            except:
                print('HALTED - ERROR copying file "' + f + '"')
                #exit(1)
                
            
        else:
            print("WARNING - dest file doesnt exist, meaning you shouldn't deploy it")
            print(dst)
            #exit(1)
        
    print("Finished copying " + str(files_copied) + " to " + dest_root)
        
        #files = mod_fl.FileList([src], ['*.py'], [], '')
        #files.save_filelist(src_root + f + "_deployed.csv", ['name'], ', ', '')
        #print (files.get_list())
main()