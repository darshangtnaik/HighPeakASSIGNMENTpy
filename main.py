#Reading input from file
def read_input():
    file1 = open('sample_input.txt', 'r')
    goodies=[]
    prices=[]
    for i in (file1.readlines()):
        splitline = i.rstrip('\n').split(":")
        if len(splitline) > 1:
            goodies.append((splitline[0]))
            prices.append((splitline[1]))
    goodies=goodies[2:]
    prices = ' '.join(prices).split()
    prices = list(map(int, prices))
    file1.close()

    main(goodies,prices)

def main(goodies,prices):
    NOE = prices[0]     #Number of employees
    prices=prices[1:]
    temp_price = prices.copy()
    min_list = []
    prices.sort()
    for i in range(len(prices)):
        if i + (NOE - 1) < len(prices):
            min_list.append(abs(prices[i] - prices[i + (NOE - 1)]))
    final_list = []
    for i in range(len(prices)):
        if (i + (NOE - 1) < len(prices)) and (abs(prices[i] - prices[i + (NOE - 1)]) == min(min_list)):
            final_list = (prices[i:i + NOE])

    write_output(NOE,final_list,goodies,temp_price,min_list)


#writing output to file
def write_output(NOE,final_list,goodies,temp_price,min_list):
    file2 = open('sample_output.txt', 'w')
    file2.write("Number of the employees:")
    file2.write(str(NOE))
    file2.write("\n")
    file2.write("\n")
    for i in range(len(final_list)):
        file2.write(("{}: {}".format(goodies[temp_price.index(final_list[i])],final_list[i])))
        file2.write("\n")
    file2.write("\n")
    file2.write("\n")
    file2.write("And the difference between the chosen goodie with highest price and the lowest price is ")
    file2.write(str(min(min_list)))
    file2.close()


read_input()     #calling read_input() function