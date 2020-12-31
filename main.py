# importing modules

import datetime
import googlesearch
import math
import random
import re
import requests
import shutil
import smtplib
import webbrowser
import string
import os
from bs4 import BeautifulSoup
from pyowm.owm import OWM
import json
currentDT = datetime.datetime.now()


# defining Time function

def time():
    print("Today is %s" % (currentDT.strftime("%A")))
    print(currentDT.strftime("%B %d, %Y"))
    print(currentDT.strftime("%Y/%m/%d"))
    print("current time is %ss" % currentDT.strftime("%H:%M:%S"))
    print(currentDT.strftime("%I:%M:%S %p"))


# defining sending email function

def send_Email(email, password):
    try:
        a = smtplib.SMTP('smtp.mail.yahoo.com', 587)
        a.ehlo()
        a.starttls()
        sender_email = email
        sender_pass = password
        receiver_email = str(input("receiver email : "))
        subject = str(input("Subject : "))
        body = str(input("Body : "))
        a.login(sender_email, sender_pass)
        a.sendmail(sender_email, receiver_email, 'Subject:%s\n%s' % (subject, body))
        print("Email successfully sent")
        a.quit()
    except smtplib.SMTPAuthenticationError:
        print("""Authentication went wrong:
Most probably the server didn't accept the username/password combination provided,
or your internet connection failed""")
    except:
        print("An error occurred")


# defining sending gmail function

def send_Gmail(gmail, password):
    try:
        a = smtplib.SMTP('smtp.gmail.com', 587)
        a.ehlo()
        a.starttls()
        sender_gmail = gmail
        sender_pass = password
        receiver_gmail = str(input("receiver Gmail : "))
        subject = str(input("Subject : "))
        body = str(input("Body : "))
        a.login(sender_gmail, sender_pass)
        a.sendmail(sender_gmail, receiver_gmail, 'Subject:%s\n%s' % (subject, body))
        print("Gmail successfully sent")
        a.quit()
    except smtplib.SMTPAuthenticationError:
        print("""Authentication went wrong:
Most probably the server didn't accept the username/password combination provided,
or your internet connection failed""")
    except:
        print("An error occurred")


# defining BMI function

def bmi(height, weight):
    height = float(height)
    weight = float(weight)
    BMI = weight / (height ** 2)
    print("""\n00 =< BMI < 18 : lack of weight
18 =< BMI < 25 : Normal
25 =< BMI < 30 : overweight
30 =< BMI      : Fat

your Body-Mass-Index(BMI) is %f""" % BMI)
    if BMI < 18:
        l = (height ** 2) * (25 - BMI)
        print("""you have lack of weight
you should have %f kilogram more weight""" % l)
    if BMI >= 18:
        if BMI < 25:
            print("your weight is normal")
        if BMI >= 25:
            if BMI < 30:
                h = (height ** 2) * (BMI - 25)
                print("""you are overweight
you have %f kilogram overweight""" % h)
            else:
                h = (height ** 2) * (BMI - 25)
                print("""you are fat
you have %f kilogram overweight""" % h)


# defining joke function

def say_joke():
    joke_list = (open("jokes.txt", "r").read()).split("\\")
    print(random.choice(joke_list))


# defining calculator function

def calculator():
    # defining calculator commands input regex

    add_regex = re.compile(r"^calc add\(([-?\d+.?\d*,?]+)\)$")
    sub_regex = re.compile(r"^calc sub\(([-?\d+.?\d*,?]+)\)$")
    mult_regex = re.compile(r"^calc mult\(([-?\d+.?\d*,?]+)\)$")
    div_regex = re.compile(r"^calc div\(([-?\d+.?\d*,?]+)\)$")
    pow_regex = re.compile(r"^calc pow\((-?\d+.?\d*),(-?\d+.?\d*)\)$")
    ar_sq_regex = re.compile(r"^calc area square\(([\d+.?\d*])\)$")
    ar_re_regex = re.compile(r"^calc area rectangular\((\d+.?\d*),(\d+.?\d*)\)$")
    ar_tr_regex = re.compile(r"^calc area triangle\((\d+.?\d*),(\d+.?\d*)\)$")
    ar_cr_regex = re.compile(r"^calc area circle\((\d+.?\d*)\)$")
    ar_trp_regex = re.compile(r"^calc area trapeze\((\d+.?\d*),(\d+.?\d*),(\d+.?\d*)\)$")
    ar_el_regex = re.compile(r"^calc area ellipse\((\d+.?\d*),(\d+.?\d*)\)$")
    vo_sph_regex = re.compile(r"^calc volume sphere\(([\d+.?\d*])\)$")
    vo_cu_regex = re.compile(r"^calc volume cube\(([\d+.?\d*])\)$")
    vo_rcu_regex = re.compile(r"^calc volume rectangular cube\((\d+.?\d*),(\d+.?\d*),(\d+.?\d*)\)$")
    vo_co_regex = re.compile(r"^calc volume cone\((\d+.?\d*),(\d+.?\d*)\)$")
    vo_sq_py_regex = re.compile(r"^calc volume square pyramid\((\d+.?\d*),(\d+.?\d*)\)$")
    vo_re_py_regex = re.compile(r"^calc volume rectangular pyramid\((\d+.?\d*),(\d+.?\d*),(\d+.?\d*)\)$")
    vo_tr_py_regex = re.compile(r"^calc volume triangle pyramid\((\d+.?\d*),(\d+.?\d*),(\d+.?\d*)\)$")
    vo_el_regex = re.compile(r"^calc volume ellipsoid\((\d+.?\d*),(\d+.?\d*),(\d+.?\d*)\)$")
    cos_regex = re.compile(r"^calc cos\((-?\d+.?\d*)\)$")
    r_cos_regex = re.compile(r"^calc r cos\((-?\d+.?\d*)\)$")
    sin_regex = re.compile(r"^calc sin\((-?\d+.?\d*)\)$")
    r_sin_regex = re.compile(r"^calc r sin\((-?\d+.?\d*)\)$")
    tan_regex = re.compile(r"^calc tan\((-?\d+.?\d*)\)$")
    r_tan_regex = re.compile(r"^calc r tan\((-?\d+.?\d*)\)$")
    cot_regex = re.compile(r"^calc cot\((-?\d+.?\d*)\)$")
    r_cot_regex = re.compile(r"^calc r cot\((-?\d+.?\d*)\)$")
    acos_regex = re.compile(r"^calc arccos\((-?\d+.?\d*)\)$")
    asin_regex = re.compile(r"^calc arcsin\((-?\d+.?\d*)\)$")
    atan_regex = re.compile(r"^calc arctan\((-?\d+.?\d*)\)$")
    acot_regex = re.compile(r"^calc arccot\((-?\d+.?\d*)\)$")
    cosh_regex = re.compile(r"^calc cosh\((-?\d+.?\d*)\)$")
    acosh_regex = re.compile(r"^calc arccosh\((-?\d+.?\d*)\)$")
    sinh_regex = re.compile(r"^calc sinh\((-?\d+.?\d*)\)$")
    asinh_regex = re.compile(r"^calc arcsinh\((-?\d+.?\d*)\)$")
    tanh_regex = re.compile(r"^calc tanh\((-?\d+.?\d*)\)$")
    atanh_regex = re.compile(r"^calc arctanh\((-?\d+.?\d*)\)$")
    coth_regex = re.compile(r"^calc coth\((-?\d+.?\d*)\)$")
    acoth_regex = re.compile(r"^calc arccoth\((-?\d+.?\d*)\)$")
    log10_regex = re.compile(r"^calc log10\((\d+.?\d*)\)$")
    log2_regex = re.compile(r"^calc log2\((\d+.?\d*)\)$")
    ln_regex = re.compile(r"^calc ln\((\d+.?\d*)\)$")
    log_regex = re.compile(r"^calc log\((-?\d+.?\d*),(-?\d+.?\d*)\)$")
    fact_regex = re.compile(r"^calc fact\((\d+.?\d*)\)$")
    sqrt_regex = re.compile(r"^calc sqrt\((\d+.?\d*)\)$")
    floor_regex = re.compile(r"^calc log10\((-?\d+.?\d*)\)$")
    ceil_regex = re.compile(r"^calc log10\((-?\d+.?\d*)\)$")
    abs_regex = re.compile(r"^calc log10\((-?\d+.?\d*)\)$")

    # defining add function

    def add(add_string):
        try:
            nums = add_string.split(",")
            for i in range(len(nums)):
                nums[i] = float(nums[i])
            print(nums, "\naddition of above numbers = %f" % (sum(nums)))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining sub function

    def sub(sub_string):
        try:
            nums = sub_string.split(",")
            for i in range(len(nums)):
                nums[i] = float(nums[i])
            if len(nums) < 2:
                nums[1] = 0
            ans = nums[0] - nums[1]
            if len(nums) > 2:
                for i in range(2, len(nums)):
                    ans -= nums[i]
            print(nums, "\nsubmission of above numbers = %f" % ans)
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining multiple function

    def mult(mult_string):
        try:
            nums = mult_string.split(",")
            for i in range(len(nums)):
                nums[i] = float(nums[i])
            ans = 1
            for i in range(len(nums)):
                ans *= nums[i]
            print(nums, "\nmultiplication of above numbers = %f" % ans)
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining division function

    def div(div_string):
        try:
            nums = div_string.split(",")
            for i in range(len(nums)):
                nums[i] = float(nums[i])
            for i in range(1, len(nums)):
                if nums[i] == 0:
                    print("zero is not accepted for devision")
                    raise ZeroDivisionError
            if len(nums) < 2:
                nums[1] = 1
            ans = nums[0]
            if len(nums) >= 2:
                for i in range(1, len(nums)):
                    ans /= nums[i]
            print(nums, "\ndivision of above numbers = %f" % ans)
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining power function

    def pow(base, pow):
        try:
            base, pow = float(base), float(pow)
            print("""base = %f
power = %f
(base) ^ (power) = base x base x base x ... (POWER times)
%f ^ %f = %f""" % (base, pow, base, pow, base ** pow))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining area of square function

    def ar_sq(side):
        try:
            side = float(side)
            print("""side = %f
square area formula = side x side
square area = %f""" % (side, side ** 2))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining area of rectangular function

    def ar_re(length, width):
        try:
            length, width = float(length), float(width)
            print("""width = %f
length = %f
rectangular area formula = length x width
rectangular area = %f""" % (width, length, width * length))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining area of triangle function

    def ar_tr(height, base):
        try:
            height, base = float(height), float(base)
            print("""base = %f
height = %f
triangle area formula = base x height / 2
triangle area = %f""" % (base, height, base * height / 2))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining area of circle function

    def ar_cr(radius):
        try:
            radius = float(radius)
            print("""radius = %f
circle area formula = pi * (radius ^ 2)
circle area = %f""" % (radius, math.pi * radius * radius))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining area of trapeze function

    def ar_trp(base1, base2, height):
        try:
            base1, base2, height = float(base1), float(base2), float(height)
            print("""base 1 = %f
base 2 %f
height = %f
trapeze area formula = (base1 + base2) x height / 2
trapeze area = %f""" % (base1, base2, height, ((base1 + base2) * height / 2)))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining area of ellipse function

    def ar_el(axis1, axis2):
        try:
            axis1, axis2 = float(axis1), float(axis2)
            print("""axis 1 = %f
axis 2 = %f
ellipse area formula = pi x axis 1 x axis 2
ellipse area = %f""" % (axis1, axis2, math.pi * axis1 * axis2))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining volume of sphere function

    def vo_sph(radius):
        try:
            radius = float(radius)
            print("""radius = %f
sphere volume formula = 4 x math.pi x (radius ^ 2 ) / 3
sphere volume = %f""" % (radius, 4 * math.pi * radius * radius * radius / 3))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining volume of cube function

    def vo_cu(side):
        try:
            side = float(side)
            print("""side = %f
cube volume = side ^ 3
cube volume = %f """ % (side, side ** 3))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining volume of rectangular cube function

    def vo_rcu(side1, side2, side3):
        try:
            side1, side2, side3 = float(side1), float(side2), float(side3)
            print("""side1, side2, side3 = %f, %f, %f
rectangular cube formula = side 1 x side 2 x side 3
rectangular cube = %f""" % (side1, side2, side3, side1 * side2 * side3))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining volume of cone function

    def vo_co(radius, height):
        try:
            radius, height = float(radius), float(height)
            print("""base radius = %f
height = %f
cone volume formula = (pi x radis^2)x(height)/3
cone volume = %f""" % (radius, height, math.pi * (radius ** 2) * height / 3))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining volume of square pyramid function

    def vo_sq_py(b_side, height):
        try:
            b_side, height = float(b_side), float(height)
            print("""base side = %f
height = %f
square pyramid volume formula = (base side)^2 x (height)/3
square pyramid volume = %f""" % (b_side, height, (b_side ** 2) * height / 3))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining volume of rectangular pyramid function

    def vo_re_py(b_width, b_length, height):
        try:
            b_width, b_length, height = float(b_width), float(b_length), float(height)
            print("""base width = %f
base length = %f
height = %f
rectangular pyramid volume formula = (base width) x (base length) x (height) / 3
rectangular pyramid volume = %f""" % (b_width, b_length, height, (b_width * b_length) * height / 3))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining volume of triangle pyramid function

    def vo_tr_py(b_side, b_height, height):
        try:
            b_side, b_height, height = float(b_side), float(b_height), float(height)
            print("""base side = %f
base height = %f
height = %f
triangle pyramid volume formula = (base side) x (base heigth) x (height) / 6
triangle pyramid volume = %f""" % (b_side, b_height, height, (b_side * b_height) * height / 6))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining volume of ellipsoid function

    def vo_el(axis1, axis2, axis3):
        try:
            axis1, axis2, axis3 = float(axis1), float(axis2), float(axis3)
            print("""axis 1 = %f
axis 2 = %f
axis 3 = %f
ellipsoid volume formula = 4 pi x (axis 1) x (axis 2) x (axis 3) / 3
ellipsoid volume = %f""" % (axis1, axis2, axis3, (4 * math.pi * axis1 * axis2 * axis3 / 3)))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining cosines in degree function

    def cos(degree):
        try:
            degree = float(degree)
            print("""degree = %f deg
cos(%f) = %f""" % (degree, degree, math.cos(math.radians(degree))))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining cosines in radian function

    def r_cos(radian):
        try:
            radian = float(radian)
            print("""degree = %f rad
cos(%f) = %f""" % (radian, radian, math.cos(radian)))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining arc cosine function

    def acos(y):
        try:
            y = float(y)
            print("""cos(x) = %f
x = %f deg
x = %f rad""" % (y, math.acos(y), math.radians(math.acos(y))))
        except:
            print("wri=ong input, try again...")

    # defining sine in degree function

    def sin(degree):
        try:
            degree = float(degree)
            print("""degree = %f deg
sin(%f) = %f""" % (degree, degree, math.sin(math.radians(degree))))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining sine in radian function

    def r_sin(radian):
        try:
            radian = float(radian)
            print("""degree = %f rad
cos(%f) = %f""" % (radian, radian, math.sin(radian)))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining arc sine function

    def asin(y):
        try:
            y = float(y)
            print("""sin(x) = %f
x = %f deg
x = %f rad""" % (y, math.asin(y), math.radians(math.asin(y))))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining tangent in degree function

    def tan(degree):
        try:
            degree = float(degree)
            print("""degree = %f deg
tan(%f) = %f""" % (degree, degree, math.tan(math.radians(degree))))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining tangent in radian function

    def r_tan(radian):
        try:
            radian = float(radian)
            print("""degree = %f rad
tan(%f) = %f""" % (radian, radian, math.tan(radian)))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining arc tangent function

    def atan(y):
        try:
            y = float(y)
            print("""tan(x) = %f
x = %f deg
x = %f rad""" % (y, math.atan(y), math.radians(math.atan(y))))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining cotangent in degree function

    def cot(degree):
        try:
            degree = float(degree)
            print("""degree = %f deg
cot(%f) = %f""" % (degree, degree, 1 / math.tan(math.radians(degree))))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining cotangent in radian function

    def r_cot(radian):
        try:
            radian = float(radian)
            print("""degree = %f rad
cot(%f) = %f""" % (radian, radian, 1 / math.tan(radian)))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining arc cotangent function

    def acot(y):
        try:
            y = float(y)
            print("""cot(x) = %f
x = %f deg
x = %f rad""" % (y, math.atan(1 / y), math.radians(math.atan(1 / y))))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining hyperbolic cosine function

    def cosh(x):
        try:
            x = float(x)
            print("""x = %f
cosh(x) = ( exp(x) + exp(-x) ) / 2
cosh(%f) = %f""" % (x, x, math.cosh(x)))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining hyperbolic arc cosine function

    def acosh(y):
        try:
            y = float(y)
            print("""cosh(x) = %f
x = ln | y + sqrt( y^2 - 1 ) |
x = %f""" % (y, math.acosh(y)))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining hyperbolic sine function

    def sinh(x):
        try:
            x = float(x)
            print("""x = %f
sinh(x) = ( exp(x) - exp(-x) ) / 2
sinh(%f) = %f""" % (x, x, math.sinh(x)))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining hyperbolic arc sine function

    def asinh(y):
        try:
            y = float(y)
            print("""sinh(x) = %f
x = ln | y + sqrt( y^2 + 1 ) |
x = %f""" % (y, math.asinh(y)))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining hyperbolic tangent function

    def tanh(x):
        try:
            x = float(x)
            print("""x = %f
tanh(x) = ( exp(x) - exp(-x) ) / ( exp(x) + exp(-x) )
tanh(%f) = %f""" % (x, x, math.tanh(x)))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining hyperbolic arc tangent function

    def atanh(y):
        try:
            y = float(y)
            print("""tanh(x) = %f
x = ( ln | (x + 1)/(1 - x) | ) / 2
x = %f""" % (y, math.atanh(y)))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining hyperbolic cotangent function

    def coth(x):
        try:
            x = float(x)
            print("""x = %s
coth(x) = ( exp(x) + exp(-x) ) / ( exp(x) - exp(-x) )
coth(%s) = %s""" % (str(x), str(x), str(1 / math.tanh(x))))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining hyperbolic arc cotangent function

    def acoth(y):
        try:
            y = float(y)
            print("""coth(x) = %s
x = ( ln | (x + 1)/(x - 1) | ) / 2
x = %s""" % (str(y), str(math.atanh(1 / y))))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining log10 function

    def log10(num):
        try:
            num = float(num)
            print("""log10 (x) = %s
10^x = %s
x = %s""" % (str(num), str(num), str(math.log10(num))))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining log2 function

    def log2(num):
        try:
            num = float(num)
            print("""log2 (x) = %s
 2^x = %s
x = %s""" % (str(num), str(num), str(math.log2(num))))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining log function

    def log(num1, num2):
        try:
            num1, num2 = float(num1), float(num2)
            print("""log%s (x) = %s
%s^x = %s
x = %s""" % (str(num1), str(num2), str(num1), str(num2), str(math.log(num2, num1))))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining ln function

    def ln(num):
        try:
            num = float(num)
            print("""ln(x) = %f
e^x = %f
x = %f""" % (num, num, math.log(num, math.e)))
        except:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    # defining calculator commands analyzer

    if re.match(r"^calc add.*", command) is not None:
        if re.match(add_regex, command) is not None:
            add(add_regex.search(command).group(1))
        else:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    if re.match(r"^calc sub.*", command) is not None:
        if re.match(sub_regex, command) is not None:
            sub(sub_regex.search(command).group(1))
        else:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    if re.match(r"^calc mult.*", command) is not None:
        if re.match(mult_regex, command) is not None:
            mult(mult_regex.search(command).group(1))
        else:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    if re.match(r"^calc div.*", command) is not None:
        if re.match(div_regex, command) is not None:
            div(div_regex.search(command).group(1))
        else:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    if re.match(r"^calc pow.*", command):
        if re.match(pow_regex, command):
            pow(pow_regex.search(command).group(1), pow_regex.search(command).group(2))
        else:
            print("""wrong input, try again...\nor you can use VI documentation to learn right syntax""")

    if re.match(ar_sq_regex, command) is not None:
        ar_sq(ar_sq_regex.search(command).group(1))

    if re.match(ar_re_regex, command) is not None:
        ar_re(ar_re_regex.search(command).group(1), ar_re_regex.search(command).group(2))

    if re.match(ar_tr_regex, command) is not None:
        ar_tr(ar_tr_regex.search(command).group(1), ar_tr_regex.search(command).group(2))

    if re.match(ar_cr_regex, command) is not None:
        ar_cr(ar_cr_regex.search(command).group(1))

    if re.match(ar_trp_regex, command) is not None:
        ar_trp(ar_trp_regex.search(command).group(1), ar_trp_regex.search(command).group(2),
               ar_trp_regex.search(command).group(3))

    if re.match(ar_el_regex, command) is not None:
        ar_el(ar_el_regex.search(command).group(1), ar_el_regex.search(command).group(2))

    if re.match(vo_sph_regex, command) is not None:
        vo_sph(vo_sph_regex.search(command).group(1))

    if re.match(vo_cu_regex, command) is not None:
        vo_cu(vo_cu_regex.search(command).group(1))

    if re.match(vo_rcu_regex, command) is not None:
        vo_rcu(vo_rcu_regex.search(command).group(1), vo_rcu_regex.search(command).group(2),
               vo_rcu_regex.search(command).group(3))

    if re.match(vo_co_regex, command) is not None:
        vo_co(vo_co_regex.search(command).group(1), vo_co_regex.search(command).group(2))

    if re.match(vo_sq_py_regex, command) is not None:
        vo_sq_py(vo_sq_py_regex.search(command).group(1), vo_sq_py_regex.search(command).group(2))

    if re.match(vo_re_py_regex, command) is not None:
        vo_re_py(vo_re_py_regex.search(command).group(1), vo_re_py_regex.search(command).group(2),
                 vo_re_py_regex.search(command).group(3))

    if re.match(vo_tr_py_regex, command) is not None:
        vo_tr_py(vo_tr_py_regex.search(command).group(1), vo_tr_py_regex.search(command).group(2),
                 vo_tr_py_regex.search(command).group(3))

    if re.match(vo_el_regex, command) is not None:
        vo_el(vo_el_regex.search(command).group(1), vo_el_regex.search(command).group(2),
              vo_el_regex.search(command).group(3))

    if re.match(cos_regex, command) is not None:
        cos(cos_regex.search(command).group(1))

    if re.match(r_cos_regex, command) is not None:
        r_cos(r_cos_regex.search(command).group(1))

    if re.match(acos_regex, command) is not None:
        acos(acos_regex.search(command).group(1))

    if re.match(sin_regex, command) is not None:
        sin(sin_regex.search(command).group(1))

    if re.match(r_sin_regex, command) is not None:
        r_sin(r_sin_regex.search(command).group(1))

    if re.match(asin_regex, command) is not None:
        asin(asin_regex.search(command).group(1))

    if re.match(tan_regex, command) is not None:
        tan(tan_regex.search(command).group(1))

    if re.match(r_tan_regex, command) is not None:
        r_tan(r_tan_regex.search(command).group(1))

    if re.match(atan_regex, command) is not None:
        atan(atan_regex.search(command).group(1))

    if re.match(cot_regex, command) is not None:
        cot(cot_regex.search(command).group(1))

    if re.match(r_cot_regex, command) is not None:
        r_cot(r_cot_regex.search(command).group(1))

    if re.match(acot_regex, command) is not None:
        acot(acot_regex.search(command).group(1))

    if re.match(cosh_regex, command) is not None:
        cosh(cosh_regex.search(command).group(1))

    if re.match(acosh_regex, command) is not None:
        acosh(acosh_regex.search(command).group(1))

    if re.match(sinh_regex, command) is not None:
        sinh(sinh_regex.search(command).group(1))

    if re.match(asinh_regex, command) is not None:
        asinh(asinh_regex.search(command).group(1))

    if re.match(tanh_regex, command) is not None:
        tanh(tanh_regex.search(command).group(1))

    if re.match(atanh_regex, command) is not None:
        atanh(atanh_regex.search(command).group(1))

    if re.match(coth_regex, command) is not None:
        coth(coth_regex.search(command).group(1))

    if re.match(acoth_regex, command) is not None:
        acoth(acoth_regex.search(command).group(1))

    if re.match(log10_regex, command) is not None:
        log10(log10_regex.search(command).group(1))

    if re.match(log2_regex, command) is not None:
        log2(log2_regex.search(command).group(1))

    if re.match(log_regex, command) is not None:
        log(log_regex.search(command).group(1), log_regex.search(command).group(2))

    if re.match(ln_regex, command) is not None:
        ln(ln_regex.search(command).group(1))


# defining map function

def MapAddress(address):
    try:
        webbrowser.open('https://www.google.com/maps/place/' + address)
    except:
        print("Connection Error, check your internet connection and try again...")


# defining google_search function

def GoogleBrowse(search):
    try:
        res = list(googlesearch.search(search, num=20, stop=20, pause=2))
        print("Here are the results for your search : ")
        for i in res:
            j = res.index(i)
            print(j + 1, ".", i, "\n")
        while True:
            try:
                target = int(input("enter the number of search result you want to open in browser : "))
                try:
                    webbrowser.open(str(res[target - 1]))
                    break
                except:
                    print("Wrong number input, try again...")
            except:
                print("unsupported input, try again...")
    except:
        print("Connection Error, check your internet connection and try again...")


# defining forecast function

def forecast(city):
    cities_URL = "http://dataservice.accuweather.com/locations/v1/cities/search?apikey=9vmZO6KUP3RsL1RJoW4YVmlzjOb5CL90&&q=%s" % city
    cities = json.loads(requests.get(cities_URL).text)
    # list of all weather api keys
    keys = (open("accua_api_key.txt", "r").read()).split("\\")
    # getting input city matches and printing them
    global city_num
    cities = []
    for i in range(len(keys)):
        key = keys[i]
        cities_URL = "http://dataservice.accuweather.com/locations/v1/cities/search?apikey=%s&&q=%s" % (key, city)
        cities = json.loads(requests.get(cities_URL).text)
        if type(cities) == dict and cities["Message"] == "The allowed number of requests has been exceeded.":
            pass
        else:
            break
    if len(cities) == 0:
        print("No city found")
    else:
        for i in range(len(cities)):
            print(i + 1, ": ", cities[i]["EnglishName"], ",", cities[i]["AdministrativeArea"]["EnglishName"], ",", cities[i]["Country"]["EnglishName"])
    # choosing the city
    while True:
        if len(cities) == 0:
            break
        try:
            city_num = int(input("enter the number of city : "))
            if city_num > len(cities) or city_num == 0:
                raise IndexError
            else:
                city = cities[city_num-1]
                break
        except ValueError:
            print("wrong format, try again...")
        except IndexError:
            print("number out of range, try again...")
    while True:
        if len(cities) == 0:
            break
        C_key = cities[city_num-1]["Key"]
        current_URL = "http://dataservice.accuweather.com/currentconditions/v1/%s?apikey=%s" % (C_key, key)
        # print(json.loads(requests.get(current_URL).text))
        current_data = json.loads(requests.get(current_URL).text)
        current_co = current_data[0]["WeatherText"]
        current_C_temp = current_data[0]["Temperature"]["Metric"]["Value"]
        current_F_temp = current_data[0]["Temperature"]["Imperial"]["Value"]
        current_pre = current_data[0]["PrecipitationType"]
        break
    while True:
        if len(cities) == 0:
            break
        print("\n")
        print(city["EnglishName"], ",", city["AdministrativeArea"]["EnglishName"], ",", city["Country"]["EnglishName"])
        print(current_data[0]["LocalObservationDateTime"][:10], " ", current_data[0]["LocalObservationDateTime"][11:16])
        print("""\n    %s
    Temp : %sC (%sF)
    precipitation : %s""" % (current_co, current_C_temp, current_F_temp, current_pre))
        break


# defining copy function

def copy(tar, des):
    while True:
        try:
            shutil.copy(tar, des)
            print("Done!")
            break
        except:
            print("An error occurred, try again and be careful to use the correct syntax")


# defining move function

def move(tar, des):
    while True:
        try:
            shutil.move(tar, des)
            print("Done!")
            break
        except:
            print("An error occurred, try again and be careful to use the correct syntax")


# defining go_to function

def go_to(path):
    try:
        os.startfile(path)
    except FileNotFoundError:
        print("file not found, try again...")


# defining commands input regex

map_regex = re.compile(r"^map\.(.*)$")
search_regex = re.compile(r"^search for (.*)$")
bmi_regex = re.compile(r"^bmi\((\d+\.?\d*),(\d+\.?\d*)\)$")
copy_regex = re.compile(r"^copy ([a-zA-Z]+:\\\\.*) to ([a-zA-Z]+:\\\\.*)$")
move_regex = re.compile(r"^move ([a-zA-Z]+:\\\\.*) to ([a-zA-Z]+:\\\\.*)$")
calc_regex = re.compile(r"^calc (.*)")
gmail_regex = re.compile(r"^send gmail\((.*),(.*)\)$")
email_regex = re.compile(r"^send email\((.*),(.*)\)$")
time_regex = re.compile(r"^time$")
forecast_regex = re.compile(r"^weather\((.*)\)$")
go_to_regex = re.compile(r"^go to (.*)$")
# main section of code

print("""Hi, my name is Alex.I\'m a Virtual-Assistant(VA). I developed by Pedram Monazami
I\'m not high-developed so I can do simple things, though I\'m becoming more useful more and more,
so you can get later versions of me from my developer by emailing him : pedram.monazzami@gmail.com
or visit www.github.com/pedram-mn/PVA.git to see full project

enter \\help to see the full documentation of my functions""")

while True:
    command = input(">>").lower()

    if command == "exit_":
        break
    if re.match(bmi_regex, command) is not None:
        bmi(bmi_regex.search(command).group(1), bmi_regex.search(command).group(2))
    if re.match(map_regex, command) is not None:
        MapAddress(map_regex.search(command).group(1))
    if re.match(search_regex, command) is not None:
        GoogleBrowse(search_regex.search(command).group(1))
    if re.match(copy_regex, command) is not None:
        copy(copy_regex.search(command).group(1), copy_regex.search(command).group(2))
    if re.match(copy_regex, command) is not None:
        move(move_regex.search(command).group(1), move_regex.search(command).group(2))
    if re.match(calc_regex, command) is not None:
        calculator()
    if re.match(time_regex, command) is not None:
        time()
    if command == "joke":
        say_joke()
    if re.match(gmail_regex, command) is not None:
        send_Gmail(gmail_regex.search(command).group(1), gmail_regex.search(command).group(2))
    if re.match(email_regex, command) is not None:
        send_Email(email_regex.search(command).group(1), email_regex.search(command).group(2))
    if re.match(go_to_regex, command) is not None:
        go_to(go_to_regex.search(command).group(1))
    if re.match(forecast_regex, command) is not None:
        forecast(forecast_regex.search(command).group(1))