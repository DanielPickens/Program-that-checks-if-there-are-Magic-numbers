def isMagic(cool_variable): 
    sum = 0; 
    while (cool_variable > 0 or sum > 9): 
        if (cool_variable == 0): 
            cool_variable = sum; 
            sum = 0; 
        sum = sum + cool_variable % 10; 
        cool_variable = int(cool_variable / 10); 
    return True if (sum == 1) else False; 
 
 
cool_variable = 1234; 
if (isMagic(cool_variable)): 
    print("Magic Number"); 
else: 
    print("Not a magic Number");
    
    
    
     # Note that the loop  
    # continues if Cool_variable is 0  
    # and sum is non-zero. 
    # It stops when Cool_variable becomes  
    # 0 and sum becomes single 
    # digit. 
