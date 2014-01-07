edges = { (1, 'a') : [2, 3],
          (2, 'a') : [2],
          (3, 'b') : [4, 2],
          (4, 'c') : [5] }
accepting = [5] #'abc'
edges2 = { (1, 'a') : [1],
           (2, 'a') : [2] }
accepting2 = [2] #'none'

def nfsmaccepts(current, edges, accepting, visited): 
     
    if current in accepting:  
        return '' 
    
    else:
        for edge in edges: 
            visited.append(edge[0]) 
        
        if (current, letter) in edges:
            destinations = edges[current, letter]
            new_string = string[1:]
            for destination in destinations:                
                if nfsmsim(new_string,destination,edges,accepting):
                    return True
        
        return 'z'
  
print nfsmaccepts(1, edges, accepting, [])    
 
