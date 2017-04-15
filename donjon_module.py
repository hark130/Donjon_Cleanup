# This module will contain functions to clean up the html of a generated system from https://donjon.bin.sh/scifi/system/

'''
    Input
        htmlCode - string representation of HTML code
    Output
        String representation of the modified HTML code
    Exceptions
        TypeError('htmlCode is not a string')
        ValueError('htmlCode is empty')
'''
def fix_paths(htmlCode):

    modifiedCode = htmlCode

    # 1. INPUT VALIDATION
    if isinstance(htmlCode, str) is False:
        raise TypeError('htmlCode is not a string')
    elif htmlCode.__len__() == 0:
        raise ValueError('htmlCode is empty')

    # 2. PATH REPLACEMENTS
    ## 2.1. Stylesheets
    modifiedCode = modifiedCode.replace('/style/','.style/')

    ## 2.2. Images
    modifiedCode = modifiedCode.replace('/scifi/system/worlds/','.images/')
    modifiedCode = modifiedCode.replace('/scifi/system/stars/','.images/')

    # 3. DONE
    return modifiedCode


'''
    Input
        htmlCode - string representation of HTML code
    Output
        String representation of the modified HTML code
    Exceptions
        TypeError('htmlCode is not a string')
        ValueError('htmlCode is empty')
'''
def remove_hrefs(htmlCode):

    modifiedCode = htmlCode

    # 1. INPUT VALIDATION
    if isinstance(htmlCode, str) is False:
        raise TypeError('htmlCode is not a string')
    elif htmlCode.__len__() == 0:
        raise ValueError('htmlCode is empty')

    # 2. HREF REPLACEMENTS
    while modifiedCode.find('<a href=') > 0:
        ## 2.0. Preserve current version of html
        currentCode = modifiedCode

        ## 2.1. Find the beginning
        hrefStart = modifiedCode.find('<a href=')

        ## 2.2. Find the end
        hrefStop = modifiedCode.find('>', hrefStart) + 1

        ## 2.3. Cut out the href
        ### 2.3.1. Copy in the beginning
        modifiedCode = currentCode[:hrefStart] 

        ### 2.3.2. Trim up the remainder 
        currentCode = currentCode[hrefStop:]

        ### 2.3.3. Remove the closing html code
        currentCode = currentCode.replace('</a>','',1)

        ### 2.3.4. Append the trimmed code
        modifiedCode = modifiedCode + currentCode

        ## 2.4. Rinse and repeat

    # 3. DONE
    return modifiedCode


    '''
	    Input
	        htmlCode - string representation of HTML code
	        newFootnote - string representation of the new footnote to add
	    Output
	        String representation of the modified HTML code
	    Exceptions
	        TypeError('htmlCode is not a string')
	        TypeError('newFootnote is not a string')
            ValueError('newFootnote is empty')
    '''
def add_footnote(htmlCode, newFootnote):

    modifiedCode = htmlCode
#    modifiedFootnote = newFootnote

    # 1. INPUT VALIDATION
    ## 1.1. htmlCode
    if isinstance(htmlCode, str) is False:
        raise TypeError('htmlCode is not a string')

    ## 1.2. newFootnote
    if isinstance(newFootnote, str) is False:
        raise TypeError('newFootnote is not a string')
    elif newFootnote.__len__() == 0:
        raise ValueError('newFootnote is empty')

    # 2. FORMAT FOOTNOTE
    ## 2.1. Look for formatting codes
    if newFootnote.find('<br') < 0 and newFootnote.find('<pre') < 0:
        ### 2.1.1. Doesn't exist
        if '\n' in newFootnote:
#            while modifiedFootnote.count('\n') != modifiedFootnote.count('<br />'):
            ### 2.1.2. Add some formatting codes
            modifiedFootnote = modifiedFootnote.replace('\n','\n<br />')
    elif newFootnote.find('<br') == 0 or newFootnote.find('<pre') == 0 or newFootnote.find('\n<br') == 0:
        # Everything is as it should be
        modifiedFootnote = newFootnote
    else:
        # Seperate existing footnote from new footnote
        modifiedFootnote = '<br />' + newFootnote

    # 3. ADD FOOTNOTE
    ## 3.0. Preserve current version of html
    currentCode = modifiedCode

    ## 3.1. Find the existing footnote
    ### 3.1.1. Doesn't exist
    if modifiedCode.find('class="footnotes"') < 0:
        print('No existing footnotes') # PLACEHOLDER
        # Write something here that places a <div class="footnotes"><p>new<br />Footnote</p>
        # ...before </body></html>
    else:
        ### 3.1.2. It does exist
        #### 3.1.2.1. Find end of paragraph
        paragraphEnd = modifiedCode.find('</p>')

        #### 3.1.2.2. Trim off the front
        modifiedCode = currentCode[:paragraphEnd]

        #### 3.1.2.3. Add new footnote
        modifiedCode = modifiedCode + modifiedFootnote

        #### 3.1.2.4. Append the end
        modifiedCode = modifiedCode + currentCode[paragraphEnd:]


    # 3. DONE
    return modifiedCode