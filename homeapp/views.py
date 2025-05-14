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
    return render(request,"aboutus.html",{'student_info':data}) # key (string)

def contact(request):
    return render(request,"contact.html")


def another_home(request):
    return render(request,"home.html")
def product(request):
    return render(request,"product.html")

