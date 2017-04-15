import sys
import os.path
from donjon_module import fix_paths     # fix_paths(htmlCode)
from donjon_module import remove_hrefs  # remove_hrefs(htmlCode)
from donjon_module import add_footnote    # add_footnote(htmlCode, newFootnote)

# 1. INPUT VALIDATION
if sys.argv.__len__() < 2:
    print('No filenames found.')
    raise ValueError('Not enough arguments')

# 2. PARSE FILENAMES
## 2.1. Fetch list
filenames = sys.argv[1:]

## 2.2. Verify existence
for originalAbsFile in filenames:
    if os.path.isfile(originalAbsFile) is False:
        print('The following file is mission:\t{}'.format(originalAbsFile))
        raise ValueError('File missing')

# 3. MODIFY FILES
for originalAbsFile in filenames:
    ## 3.0. Reset reused variables
    originalHTML = ''
    modifiedHTML = ''
    orinalPath = ''
    originalFilename = ''
    newFilename = ''
    fileExtension = ''
    newFile = ''
    newAbsFile = ''

    ## 3.1. Open original file
    with open(originalAbsFile, 'r') as currentFile:
        originalHTML = currentFile.read()

    ## 3.2. Do the real work 

    ######################    
    ## 3.2.1. Fix paths ##
    ######################
    try:
        modifiedHTML = fix_paths(originalHTML)
    except Exception as err:
        print(repr(err)) # DEBUGGING
        raise err
    
    #############################
    ## 3.2.2. Remove any hrefs ##
    #############################
    try:
        modifiedHTML = remove_hrefs(modifiedHTML)
    except Exception as err:
        print(repr(err)) # DEBUGGING
        raise err

    #########################
    ## 3.2.3. Add footnote ##
    #########################
    try:
        newFootnote = '\n<br />\n<br />Results modified by the Donjon_Cleanup project\n<br />Repository:  https://github.com/hark130/Donjon_Cleanup.git'        
        modifiedHTML = add_footnote(modifiedHTML, newFootnote)
    except Exception as err:
        print(repr(err)) # DEBUGGING
        raise err

    ## 3.3. Deconstruct absolute filename
    originalPath, originalFilename = os.path.split(originalAbsFile)

    ## 3.4. Construct new filename
    newFilename = originalFilename

    ### 3.4.1. Determine file extension
    if newFilename.find('.') == 0:
        if newFilename.count('.') == 2:
            fileExtension = newFilename[1:]
            fileExtension = fileExtension[fileExtension.find('.'):]
        else:
            print('Too many filename/extension delimiters in file:\t{}'.format(originalAbsFile))
            raise ValueError('Too many file delimiters') 
    elif newFilename.find('.') > 0:
        fileExtension = newFilename[newFilename.find('.'):]
    else:
        fileExtension = ''

    ### 3.4.2. Strip off file extension
    if fileExtension.__len__() > 0:
        newFilename = newFilename[:newFilename.find(fileExtension)]

    ### 3.4.3. Create new filename
    newFilename = newFilename + '_modified'

    ### 3.4.4. Replace file extension
    newFilename = newFilename + fileExtension

    ## 3.5. Reconstruct absolute filename
    newAbsFile = os.path.join(originalPath, newFilename)

    ## 3.6. Create new file
    with open(newAbsFile, 'w') as newFile:
        newFile.write(modifiedHTML)

    ## 3.7. Feedback
    print('HTML code found in {} has been successfully modified and saved in {}'.format(originalAbsFile, newAbsFile))
