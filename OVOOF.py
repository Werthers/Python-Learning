#一元一次方程求解(For Mrs.Qiu)
a = 0;#这个是x的系数w默认在等号左侧
b = 0;#这个是常数项的系数w默认在等号右侧
f = "";#字符串化所输入的方程

n = int(input("The number of Left Hand Side monomials: "));#请输入等号左侧单项式的数目w

count = 0;
while(count<n) :#逐个读取左侧单项式
	count=count+1;
	s=input("The "+str(count)+"th monomials is: ");

	if(s.find("-")==-1) :#
		f=f+"+"+s;
	else:
		f=f+s;

	if(s.find("x")==-1):#如果是常数项，移到等号右侧并变号
		b=b-int(s);
	else:
		a=a+int(s.strip('x'));

m=int(input("The number of Right Hand Side monomials: "));#请输入等号右侧单项式的数目w
f=f+" = ";
count = 0;
while(count<int(m)) :#逐个读取右侧单项式
	count=count+1;
	s=input("The "+str(count)+"th monomials is: ");

	if(s.find("-")==-1):
			f=f+"+"+s;
	else:
			f=f+s;

	if(s.find("x")==-1) :
			b=b+int(s);
	else:
			a=a-int(s.strip('x'));#如果是一次项，移到等号左侧并变号
print("The solution of \n"+f+" \n is: x = "+str(b/a));#输出结果
