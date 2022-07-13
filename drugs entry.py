## Thema 1 ##

# import Drug data
name= str(input("Enter Drug name: "))
ingredient = str(input("Enter the active ingredient of the drug: "))
oz = float(input("Enter drug's dosage in oz: "))

# oz to gr conversion
grams = oz / 0.035274 
print(ingredient,"dosage is ",grams,"gr")

 # Monthly quantity calculation
month = grams * 30
if month > 100 :
    print("The total quantity of ",ingredient,"is more than 100gr") ;

## Thema 1- end ##





## Thema 2 ##

L3=[] #empty list

# entries for the first drug
drug1 = str(input("Enter the active ingredient of the first drug: "))
drug1_meas1 =  float(input("Enter first measurement in gr: "))
drug1_meas2 = float(input("Enter second measurement in gr: "))

# L3 list with drug1 sublist
L3 += [[drug1, drug1_meas1, drug1_meas2]] 

# entries for the second drug
drug2 = str(input("Enter the active ingredient of the second drug: "))
drug2_meas1 =  float(input("Enter first measurement in gr: "))
drug2_meas2 = float(input("Enter second measurement in gr: "))

# new L3 list with drug1 and drug2 sublists
L3 += [[drug2, drug2_meas1, drug2_meas2]]

# search if 10 is in L3
x = any(10 in i for i in L3)
if x:
    print("Yes, 10 is in L3")
else:
    print("10 is not in L3")
    
# entries for the third drug  
drug3 = str(input("Enter the active ingredient of the third drug: "))
drug3_meas1 =  float(input("Enter first measurement in gr: "))
drug3_meas2 = float(input("Enter second measurement in gr: "))

# new L3 list with drug1, drug2 and drug3 sublists
L3 += [[drug3, drug3_meas1, drug3_meas2]]
print(L3)

# remove the first list(drug1) and print L3
del L3[0]
print(L3)

# reverse and print  L3 list
L3.reverse()
print(L3)

## Thema 2-end ##
