
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