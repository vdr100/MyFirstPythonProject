x=int (input ("Enter your weight"))
y= input ("Enter your units in Kg or pounds")
if y=='kg':
  print ("Weight in pounds is "+str(x*2.2))
elif y=='lb' :
 print ("Weight in kgs is " +str (x/2.2))
else:
  print ("incorrect weight")

