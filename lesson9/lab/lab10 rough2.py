def findLargestFile(path, c=0, size = None, largestFile = '/'):
            
        if (os.path.isdir(path) == False):
            #if file, get path to file
            clargestFile = path
            m = os.path.getsize(clargestFile)
        
        elif c == len(os.listdir(path)):
            return largestFile
            
        else:        
            for move in os.listdir(path):
                c += 1
                newPath = path + '/' + move
            
                if move == '.DS_Store':
                    continue

                # if folder, get path to largest file in folder
                clargestFile = findLargestFile(newPath, 0, size, newPath)
            
                if size == None or m > size:
                    # set largest file to new largest file
                    largestFile = clargestFile
                    size = os.path.getsize(clargestFile)
                    
            return largestFile
        
                


def findLargestFile(path, c=0, size = None, largestFile = '/'):
    
    
    print("path: ", path)
    print("largest File: ", largestFile)
    
    # case: no files in folders
    #if (os.path.isdir(largestFile) == True) and largestFile != '/':
        #return ""
    # when checked all files, return largest file
    if c == len(os.listdir(path)):
        if largestFile == '/':
            return ""
        #if (os.path.isdir(largestFile) == True):
            #return ""
        return largestFile
    
    else:
        print("list: ",os.listdir(path))
        for move in os.listdir(path):
            c += 1
            newPath = path + '/' + move
            
            if move == '.DS_Store':
                continue
                
            if (os.path.isdir(newPath) == True):
                # if folder, get path to largest file in folder
                clargestFile = findLargestFile(newPath, 0, size, newPath)
                
                    
            if (os.path.isdir(newPath) == False):
                # if file, get path to file
                clargestFile = newPath
            
            m = os.path.getsize(clargestFile)
            if size == None or m > size:
                # set largest file to new largest file
                largestFile = clargestFile
                size = os.path.getsize(clargestFile)
        
        if largestFile == '/':
            return ""
            
        print("largestFileReturn..: ", largestFile)
        return largestFile          