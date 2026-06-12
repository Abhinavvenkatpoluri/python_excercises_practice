def color_code(color):
    array_1=[0,1,2,3,4,5,6,7,8,9]
    dict_1=dict(zip(colors(),array_1))
    try:
          return dict_1[color]
    except:
           raise ValueError("")
        
    
def colors():
     expected = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
     return expected
