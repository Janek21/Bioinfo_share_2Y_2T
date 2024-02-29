def knapsack(WL,VL, maxw):
    WL = [0] + WL
    VL = [0] + VL
    table = {}
    for weight in range(maxw+1):
        table[(0,0),weight] = 0

    for obj in range(len(WL)):
        object = (WL[obj], VL[obj])
        table[object,0] = 0
    
    for weight in range(1,maxw+1):
        for obj in range(1,len(WL)):
            obj_v = VL[obj]
            obj_w = WL[obj]

            if ( obj_w <= weight and 
                obj_v + table[(obj_w, obj_v),weight-obj_w] > 
                table[(WL[obj-1], VL[obj-1]), weight] ):
                table[(obj_w, obj_v), weight] = obj_v + table[(WL[obj-1], VL[obj-1]),weight-obj_w]
            
            else: 
               table[(obj_w, obj_v), weight] = table[(WL[obj-1], VL[obj-1]), weight]

    return table[(WL[len(WL)-1], VL[len(VL)-1]), maxw]

weights =  [7, 8, 3]
values =  [3000, 6000, 2000]
print(knapsack(weights, values, 10))

