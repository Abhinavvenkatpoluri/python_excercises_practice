def value(colors):
    array_1=[0,1,2,3,4,5,6,7,8,9]
    expected = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    dict_1=dict(zip(expected,array_1))
    return (dict_1[colors[0]]*10)+dict_1[colors[1]]
    
        
    

