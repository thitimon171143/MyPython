import matplotlib.pyplot as plt
def main():
    sales = [100,400,300,600]
    slice_labels = ['1st Qtr','2st Qtr','3st Qtr','4st Qtr']
    plt.pie(sales,labels=slice_labels)
    plt.title('Sales by Quarter')
    plt.show()
main()