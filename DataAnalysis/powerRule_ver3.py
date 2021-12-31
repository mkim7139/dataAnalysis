# powerRule_ver3.py (version 3)
# Max Kim
# , 2021
# Takes polynomial as input and converts to derivative
# through power rule and string analysis

# takes a polynomial expression as a string and a variable value
# returns derivative at specified variable value
def derive(raw, var):
    line = create_list(raw)
    coefs=derivCoefficients(line)
    print(coefs)
    result=listToExpression(var, coefs)
    print(result)
    return result

# extracts coefficients and exponents from a polynomial written as a string.
def create_list(line):
    list=[]
    for i in range(len(line)):
        if i==0:  # asumes first item in list will be number
            list.append(line[i])
        elif (isFloat(line[i]) or line[i]=='.') and (isFloat(line[i-1]) or line[i-1]=='.' or line[i-1]=='-'): #condenses numbers, decimals, and signs
            list[-1]+=line[i]
        elif isFloat(line[i]):
            list.append(line[i])
        elif line[i]=='-':
            list.append(line[i])
    return numberify(list)

# can a value be converted to a float?
def isFloat(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

# switch all possible items in a list float type
def numberify(list):
    for i in range(len(list)):
        if isFloat(list[i]):
            list[i] = float(list[i])
    return list

# takes output of create_list
# returns the coefficients and exponents of the derivative
def derivCoefficients(list):
    count = 0
    pos=0
    for i in range(len(list)):
        if isFloat(list[i]) and count%2==0:
            pos = i
            count+=1
        elif isFloat(list[i]) and count%2!=0:
            list[pos]*=list[i]
            list[i]-=1
            count+=1
    return list

# takes output of deriv
# returns the value of the derivative for a given variable value
def listToExpression(var, list):
    expression=0
    for i in range(len(list)):
        if i%2!=0:
            expression+=list[i-1] * (var**list[i])
    return expression

# test
# derive('2x^3 -3.2x^(-4)', 2)
