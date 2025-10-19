s_d={'id1' :
    {'name': ['Steve'],
     'class': ['V'],
     's_i': ['english, math, science']
     },
    'id2': 
    {'name': ['Bob'],
     'class': ['V'],
     's_i': ['english, math, science']
     },
    'id3': 
    {'name': ['Bill'],
     'class': ['V'],
     's_i': ['english, math, science']
     },
    'id4': 
    {'name': ['Jeff'],
     'class': ['V'],
     's_i': ['english, math, science']
     },
}

result={}

for key,value in s_d.items():
    if value not in result.values():
        result[key]=value
        
print(result)