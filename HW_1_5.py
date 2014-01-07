Python 3.3.3 (v3.3.3:c3896275c0f6, Nov 18 2013, 21:18:40) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
def nfsmaccepts(current, edges, accepting, visited): 
    word = ""
    if current in visited:
        return None
    if current in accepting:        
        return ''
    else:
        visited.append(current)
        for edge, destination_state in edges.items():             
            state, letter = edge        
            if state == current:
                for destination in destination_state:
                    current =  destination
                    nfsmaccepts(current, edges, accepting, visited)
                    return word + letter   
        else:
        
            return None
