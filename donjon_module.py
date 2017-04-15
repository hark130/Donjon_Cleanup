# This module will contain functions to clean up the html of a generated system from https://donjon.bin.sh/scifi/system/

'''
    Input
        htmlCode - string representation of HTML code
    Output
        String representation of the modified HTML code
    Exceptions
        TypeError('htmlCode is not a string')
'''
def fix_paths(htmlCode):

    modifiedCode = htmlCode

    # 1. INPUT VALIDATION
    if isinstance(htmlCode, str) is False:
        raise TypeError('htmlCode is not a string')

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
'''
def remove_hrefs(htmlCode):

    modifiedCode = htmlCode

    # 1. INPUT VALIDATION
    if isinstance(htmlCode, str) is False:
        raise TypeError('htmlCode is not a string')

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