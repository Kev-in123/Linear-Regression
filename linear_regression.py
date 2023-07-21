def mean(data):
    return sum(data)/len(data)

def var(data):
    '''
    variance
    '''
    mean_=mean(data)
    difference=[i-mean_ for i in data]
    square=[i*i for i in difference]
    variance = mean(square)
    return variance

def std(data):
    '''
    standard deviation
    '''
    return var(data)**0.5
    
def pcc(x_data,y_data):
    '''
    Pearson’s Correlation Coefficient
    '''
    mean_x=mean(x_data)
    difference_x=[i-mean_x for i in x_data]
    square_x=[i*i for i in difference_x]
    
    mean_y=mean(y_data)
    difference_y=[i-mean_y for i in y_data]
    square_y=[i*i for i in difference_y]
    
    multiply=[]
    for i in range(len(x_data)):
        multiply.append(difference_x[i]*difference_y[i])
        
    return sum(multiply)/(sum(square_x)*sum(square_y))**0.5    

def slope(x_data,y_data):
    '''
    b=r(Sy/Sx)
    slope=(pearsons correlation)(Standard deviation y/Standard deviation x)
    '''
    std_x=std(x_data)
    std_y=std(y_data)
    correlation=pcc(x_data,y_data)
    return correlation*std_y/std_x    
    
def y_int(x_data,y_data):
    '''
    a=SlopeY-bSlopeX
    y-int of regression = (mean y) - (slope of regression)(mean x)
    '''
    correlation=pcc(x_data,y_data)
    return mean(y_data)-slope(x_data,y_data)*mean(x_data)

def linear_regression_formula(x_data,y_data):
   '''
   y=a+bx (y=b+mx or mx+b  (a=b,b=m))
   y=y-intercept + slope * x
   '''
   y_inter=y_int(x_data,y_data)
   slope_=slope(x_data,y_data)
   if str(y_inter)[0]=='-':
      return f'y={slope_:.3e} x {y_inter:.3e}'.replace(' -',' - ')
   return f'y={slope_:.3e} x + {y_inter:.3e}'

def linear_regression_value(x_data,y_data,x_value):
   '''
   y=a+bx (y=b+mx or mx+b  (a=b,b=m))
   y=y-intercept + slope * x
   '''
   y_inter=y_int(x_data,y_data)
   slope_=slope(x_data,y_data)
   return y_inter + slope_*x_value


     
