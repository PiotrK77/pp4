items = [["Clean Code, Robert C. Martin", 100.00, 0.08], ["Applying UML and Patterns, C. Larman", 300.00, 0.08], ["Shipping", 50, 0.23]]

def calculateTotalNet(products):
    global dictNet
    global dictGross
    dictNet = {}
    dictGross = {}
    for i in products:
        vat = i[2]
        net = i[1]
        if vat not in dictNet:
            dictNet[vat] = net
            dictGross[vat] = net * (1+vat)
        else:
            dictNet[vat] += net
            dictGross[vat] += net * (1+vat)
    print (dictNet, dictGross)




def createTable():
    table = (["", "Total net", "Total gross"], ["VAT 8%", dictNet[0.08], dictGross[0.08]], ["VAT 23%", dictNet[0.23], dictGross[0.23]])
    return table

def printTable(table):
    print(table)

calculateTotalNet(items)
table = createTable()
printTable(table)



