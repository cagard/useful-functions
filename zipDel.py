import os
import zipfile as zf

def zipDel(pathlist,zipname, delete = True):
	"""
	This function takes a list of filenames, _pathlist_, and 
	zips them to a zipfile with the name provided to the argument _zipname_.  If the _delete_ option is *True* (_default_), the source files will be deleted after zipping.
	"""

    if '.zip' not in zipname:
        zipname = zipname+'.zip'
    with zf.ZipFile(zipname, 'a') as myzip:
        [myzip.write(f) for f in pathlist]
        myzip.close()
        print('Zipping Complete')
        if delete:
			[os.remove(f) for f in pathlist if os.path.exists(f)]
			print("Deleting Complete") 
		else:
			print("Files have not been deleted."
		