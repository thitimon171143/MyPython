def main():
    total = 0.0
    try:
        infile = open('sales_data.txt','r')
        for line in infile:
            amount = float(line)
            total += amount
        infile.close()
        print(format(total,',.2f'))
    except IOError:
        print('An error occured trying to read thr file.')
    except ValueError:
        print('Non-numeric datat found in the file.')
    except:
        print('An error occured.')
main()