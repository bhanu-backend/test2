from django.shortcuts import render



def home(request):
    return render(request,"index.html")


def about_page(request):
    data = [
          [1,"krish","ujjain",9898778787],
          [2,"shubham","chandu khedi",9634634643],
          [3,"Mihir","Nepal",987767787],
          [4,"Palak","indore",4365328787],
    ]
    return render(request,"aboutus.html",{'student_info':data,'myvalue' : 90,
                                          'myvalue2' : 350
                                          
                                          }) # key (string)

def contact(request):
    data = [
          [1,"krish","ujjain",9898778787],
          [2,"shubham","chandu khedi",9634634643],
          [3,"Mihir","Nepal",987767787],
          [4,"Palak","indore",4365328787],
    ]
    data = {'student_records':data}
    return render(request,"contact.html",data)


def another_home(request):
    return render(request,"home.html")
def product(request):
    return render(request,"product.html")

def new(request):

    data = [
          [1,"krish","ujjain",9898778787],
          [2,"shubham","chandu khedi",9634634643],
          [3,"Mihir","Nepal",987767787],
          [4,"Palak","indore",4365328787],
    ]
    return render(request,"new.html",{"jobsense_data":data})

