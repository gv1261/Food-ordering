from flask import Flask,render_template,request
import request
app= Flask(__name__)

@app.route('/')
def index():
    return render_template("html.html")   

@app.route('/new',methods=['GET','POST'])
def new():

    return render_template("index.html")  

@app.route('/starter',methods=['GET','POST'])
def starter():
    
    return render_template("stater.html") 

@app.route('/veg',methods=['GET','POST'])
def veg():
    
    return render_template("veg.html") 

@app.route('/non',methods=['GET','POST'])
def non():
    
    return render_template("non_veg.html") 

@app.route('/dest',methods=['GET','POST'])
def dest():
    
    return render_template("desert.html") 

# @app.route('/pay')
# def payment():
#     return render_template("pay.html")
    

add_to_source=[]
add_to_name=[]
add_to_price=[]
add_to_quan=[]
total=[]
Result_price = []


@app.route('/add', methods=['POST','GET'])
def cart():
    Result_price.clear()
    global total1,name
    img=request.form['food']
    try:
        quan=request.form['quantity']

    except:
        quan=1
    # print(img)
    x=img.split()
    # print(x)
    total.append(x)
    add_to_source.append(x[0])
    add_to_name.append(x[1])
    add_to_price.append(x[2])
    add_to_quan.append(quan)
    # print(total)
    # print(add_to_source)
    # print("Name  : ",add_to_name)
    
    # print("Price : ",add_to_price)
    
    
   
        # total1 += num

    # s = add_to_name
    # name = ' '.join([str(elem) for elem in s])
    # print("Name : ",name)
    # Q = add_to_quan
    # q = ' '.join([str(eleme) for eleme in Q])
    # print("Quantity : ",q)
    return render_template('stater.html')
    
@app.route('/add1', methods=['POST','GET'])
def cart1():
    Result_price.clear()
    global total1,name
    img=request.form['food']
    try:
        quan=request.form['quantity']

    except:
        quan=1
    # print(img)
    x=img.split()
    # print(x)
    total.append(x)
    add_to_source.append(x[0])
    add_to_name.append(x[1])
    add_to_price.append(x[2])
    add_to_quan.append(quan)
    # print(total)
    # print(add_to_source)
    # print("Name  : ",add_to_name)
    
    # print("Price : ",add_to_price)
    
    
   
        # total1 += num

    # s = add_to_name
    # name = ' '.join([str(elem) for elem in s])
    # print("Name : ",name)
    # Q = add_to_quan
    # q = ' '.join([str(eleme) for eleme in Q])
    # print("Quantity : ",q)
    return render_template('veg.html')
    


@app.route('/add2', methods=['POST','GET'])
def cart2():
    Result_price.clear()
    global total1,name
    img=request.form['food']
    try:
        quan=request.form['quantity']

    except:
        quan=1
    # print(img)
    x=img.split()
    # print(x)
    total.append(x)
    add_to_source.append(x[0])
    add_to_name.append(x[1])
    add_to_price.append(x[2])
    add_to_quan.append(quan)
    # print(total)
    # print(add_to_source)
    # print("Name  : ",add_to_name)
    
    # print("Price : ",add_to_price)
    
    
   
        # total1 += num

    # s = add_to_name
    # name = ' '.join([str(elem) for elem in s])
    # print("Name : ",name)
    # Q = add_to_quan
    # q = ' '.join([str(eleme) for eleme in Q])
    # print("Quantity : ",q)
    return render_template('non_veg.html')
    

@app.route('/add3', methods=['POST','GET'])
def cart3():
    Result_price.clear()
    global total1,name
    img=request.form['food']
    try:
        quan=request.form['quantity']

    except:
        quan=1
    # print(img)
    x=img.split()
    # print(x)
    total.append(x)
    add_to_source.append(x[0])
    add_to_name.append(x[1])
    add_to_price.append(x[2])
    add_to_quan.append(quan)
    # print(total)
    # print(add_to_source)
    # print("Name  : ",add_to_name)
    
    # print("Price : ",add_to_price)

    
    
    return render_template('desert.html')
    



@app.route('/carts')
def added():
    

#     print(add_to_quan)
    for i1, i2 in zip(add_to_price, add_to_quan):
        Result_price.append(int(i1)*int(i2))
    
    
#     print("The product of 2 lists is: ", Result_price)

    my_list = Result_price
    # print(my_list)
    total1 = 0

    for num in my_list:
        # print(num)
        total1 += int(num)

    print("Amount : ",total1)  


    # for a in total:
    #     b=a

    # print(b)    
   
    return render_template('cart.html',list=add_to_source,list2=add_to_name,list3=Result_price,list4=total1,list5=add_to_quan)    



@app.route('/pay')
def pay():
    s = add_to_name
    name = ' '.join([str(elem) for elem in s])
    print("Name : ",name)
    Q = add_to_quan
    q = ' '.join([str(eleme) for eleme in Q])
    print("Quantity : ",q)
    Result_price.clear()

    Result_price.clear()

    print(add_to_quan)
    for i1, i2 in zip(add_to_price, add_to_quan):
        Result_price.append(int(i1)*int(i2))
    
    
    print("The product of 2 lists is: ", Result_price)

    my_list = Result_price
    # print(my_list)
    total1 = 0

    for num in my_list:
        # print(num)
        total1 += int(num)

    print("Amount : ",total1)  

    img='static\myqr.png'
    # for a in total:
    #     b=a

    # print(b)    
    Response=requests.get("https://iotcloud22.in/iot2/post_value.php?value1="+name+"&value2="+q)
    print("HTTP Response : ",Response.status_code)
    return render_template('cart1.html',list=add_to_source,list2=add_to_name,list3=Result_price,list4=total1,list5=add_to_quan,img=img)    


@app.route('/gif')
def added1():
    return render_template("gif.html")


if __name__=="__main__":
    app.run(debug=True)    