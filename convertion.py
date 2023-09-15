#Developer Amanuel Bantidagn
#Adam Science and technology University
try:
	import math
	while True:
		print()
		print("---------------------NUMBER CONVERTION-----------------------")
		print()
		print("Click 1.To convert Decimal to Binary ")
		print("Click 2.To convert Binary to Decimal ")
		print("Click 3.To convert decimal to hexadecimal")
		print("Click 4.To convert HexaDecimal to Decimal")
		print("Click 5.To convert HexaDecimal to Binary")
		print("Click 6.To convert Binary to Hexadecimal")
		print("Click 7.To convert Octal to Decimal")
		print("Click 8.To convert Octal to Binary")
		print("Click 9.To convert Binary to Octal")
		print("Click 10.To convert Decimal to Octal")
		print("Click 11.To convert HexaDecimal to Octal")
		print("Click 12.To convert Octal to HexaDecimal")
		print("Click 13.Exist!")

		choice=int(input())
		
		# Decimal to Binary

		def main():
			storeL=[]
			remL=[]
			num=int(input("Enter a postive number:"))
			if num==0:
				remL.append(num)


			while num!=0:
				store=num//2
				storeL.append(store)
				rem=num%2
				remL.append(rem)
				num=store

			remL.reverse()
			for i in range(len(remL)):
				print(remL[i], end=' ')

		#Binary to decimal

		def maina():
			num1=input("Enter the binary number:")
			lis=[]
			for i in range(len(num1)):
				lis.append(num1[i])
					
			lis.reverse()
			cont=[]
			for i in range(len(lis)):
				ans=((pow(2,i))*int(lis[i]))
				cont.append(int(ans))

			print(sum(cont))


		# decimal to hexadecimal

		def mainb():
			dic={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
			storec=[]
			remc=[]
			num=int(input("Enter a postive number:"))
			while num!=0:
				store=num//16
				storec.append(store)
				rem=num%16
				remc.append(rem)
				num=store

			remc.reverse()
			for i in range(len(remc)):
				if remc[i] not in dic:
					print(remc[i], end='')
				else:
					print(dic[remc[i]] , end='')
					

		# HexaDecimal to Decimal

		def mainc():
			
			num1=input("Enter the HexaDecimal number:")
			Binary_list=[]
			Binary_list1=[]
			for i in range(len(num1)):
				Binary_list.append(num1[i])
			for i in range(len(Binary_list)):
				if Binary_list[i]=='A':
					Binary_list1.append(int(10))	
				elif Binary_list[i]=='B':
					Binary_list1.append(int(11))
				elif Binary_list[i]=='C':
					Binary_list1.append(int(12))
				elif Binary_list[i]=='D':
					Binary_list1.append(int(13))
				elif Binary_list[i]=='E':
					Binary_list1.append(int(14))
				elif Binary_list[i]=='F':
					Binary_list1.append(int(15))
				else:	
					Binary_list1.append(int(Binary_list[i]))
				
			Binary_list1.reverse()
			cont=[]
			for i in range(len(Binary_list1)):
				ans=pow(16,i)*int(Binary_list1[i])
				cont.append(int(ans))


			print(sum(cont))



		#HexaDecimal to Binary
		def maind():
			hexa=input("Enter the Hexadecimal number:")
			finalhex=[]
			def hexamain(hexa):
				storeL=[]
				remL=[]

				num=int(hexa)
				while num!=0:
					store=num//2
					storeL.append(store)
					rem=num%2
					remL.append(rem)
					num=store

				remL.reverse()
				for i in range(len(remL)):
					finalhex.append(remL[i])

			def hexamainnum(hexa):
				storeL=[]
				remL=[]

				num=int(hexa)
				while num!=0:
					store=num//2
					storeL.append(store)
					rem=num%2
					remL.append(rem)
					num=store

				remL.reverse()
				return remL



			for i in range(len(hexa)):
				if hexa[i]=='A':
					hexamain(10)
				elif hexa[i]=='B':
					hexamain(11)
				elif hexa[i]=='C':
					hexamain(12)
				elif hexa[i]=='D':
					hexamain(13)
				elif hexa[i]=='E':
					hexamain(14)
				elif hexa[i]=='F':
					hexamain(15)
				elif int(hexa[i])<=9:
				
					list1=hexamainnum(hexa[i])
					while len(list1)!=4:
						list1.insert(0,0)
					for i in range(len(list1)):
						finalhex.append(list1[i])

				elif int(hexa[i])>=0:
					hexamain(hexa[i])

				else:
					print("Invalid input!")
					break;

			for i in range(len(finalhex)):
				print(finalhex[i], end=' ')

		#Binary to HexaDecimal 
		def maine():
			def hexo(binarynum):
				binarysplit=[]
				hexanum=[]
				for i in range(math.ceil(lengs)):
					binarysplit.append(binarynum[0:4])
					binarynum=binarynum[4:]


				for i in range(len(binarysplit)):
					if binarysplit[i]=='0000':
						hexanum.append(0)
					elif binarysplit[i]=='0001':
						hexanum.append(1)
					elif binarysplit[i]=='0010':
						hexanum.append(2)
					elif binarysplit[i]=='0011':
						hexanum.append(3)
					elif binarysplit[i]=='0100':
						hexanum.append(4)
					elif binarysplit[i]=='0101':
						hexanum.append(5)
					elif binarysplit[i]=='0110':
						hexanum.append(6)
					elif binarysplit[i]=='0111':
						hexanum.append(7)
					elif binarysplit[i]=='1000':
						hexanum.append(8)
					elif binarysplit[i]=='1001':
						hexanum.append(9)
					elif binarysplit[i]=='1010':
						hexanum.append('A')
					elif binarysplit[i]=='1011':
						hexanum.append('B')
					elif binarysplit[i]=='1100':
						hexanum.append('C')
					elif binarysplit[i]=='1101':
						hexanum.append('D')
					elif binarysplit[i]=='1110':
						hexanum.append('E')
					elif binarysplit[i]=='1111':
						hexanum.append('F')

				for i in range(len(hexanum)):
					print(hexanum[i],end='')
				
			binarynum=input("Enter a Binary number:")
			lengs=len(binarynum)/4
			while True:
				leng=len(binarynum)%4
				if leng==0:
					hexo(binarynum)
					break
				elif leng!=0:
					binarynum='0'+binarynum

		#Octal to decimal
		
		def mainf():
			num1=input("Enter the Octal Number:")
			lis=[]
			for i in range(len(num1)):
				lis.append(num1[i])
					
			lis.reverse()
			cont=[]
			for i in range(len(lis)):
				ans=pow(8,i)*int(lis[i])
				cont.append(int(ans))

			print(sum(cont))


		#Octal to Binary
		def maing():
			octa=input("Enter the Octal number:")
			finalocta=[]
			def hexamainnum(hexa):
				storeL=[]
				remL=[]

				num=int(hexa)
				while num!=0:
					store=num//2
					storeL.append(store)
					rem=num%2
					remL.append(rem)
					num=store

				remL.reverse()
				return remL

			for i in range(len(octa)):
				if int(octa[i])<=9:
				
					list1=hexamainnum(octa[i])
					while len(list1)!=3:
						list1.insert(0,0)
					for i in range(len(list1)):
						finalocta.append(list1[i])

				else:
					print("Invalid input!")
					break;

			for i in range(len(finalocta)):
				print(finalocta[i], end=' ')


		#Binary to Octal
		def mainh():
			def oct(binarynum):
				binarysplit=[]
				octnum=[]
				for i in range(math.ceil(lengs)):
					binarysplit.append(binarynum[0:3])
					binarynum=binarynum[3:]


				for i in range(len(binarysplit)):
					if binarysplit[i]=='000':
						octnum.append(0)
					elif binarysplit[i]=='001':
						octnum.append(1)
					elif binarysplit[i]=='010':
						octnum.append(2)
					elif binarysplit[i]=='011':
						octnum.append(3)
					elif binarysplit[i]=='100':
						octnum.append(4)
					elif binarysplit[i]=='101':
						octnum.append(5)
					elif binarysplit[i]=='110':
						octnum.append(6)
					elif binarysplit[i]=='111':
						octnum.append(7)
					

				for i in range(len(octnum)):
					print(octnum[i],end='')
					
			binarynum=input("Enter a Binary number:")
			lengs=len(binarynum)/3
			while True:
				leng=len(binarynum)%3
				if leng==0:
					oct(binarynum)
					break
				elif leng!=0:
					binarynum='0'+binarynum


		#Decimal to Octal
		def maini():
			storec=[]
			remc=[]
			num=int(input("Enter a postive number:"))
			while num!=0:
				store=num//8
				storec.append(store)
				rem=num%8
				remc.append(rem)
				num=store

			remc.reverse()
			for i in range(len(remc)):
				print(remc[i], end='')
				

		#Hexadecimal to Octal
		def mainj():
			
			num1=input("Enter the HexaDecimal number:")
			Binary_list=[]
			Binary_list1=[]
			for i in range(len(num1)):
				Binary_list.append(num1[i])
			for i in range(len(Binary_list)):
				if Binary_list[i]=='A':
					Binary_list1.append(int(10))	
				elif Binary_list[i]=='B':
					Binary_list1.append(int(11))
				elif Binary_list[i]=='C':
					Binary_list1.append(int(12))
				elif Binary_list[i]=='D':
					Binary_list1.append(int(13))
				elif Binary_list[i]=='E':
					Binary_list1.append(int(14))
				elif Binary_list[i]=='F':
					Binary_list1.append(int(15))
				else:	
					Binary_list1.append(int(Binary_list[i]))
				
			Binary_list1.reverse()
			cont=[]
			for i in range(len(Binary_list1)):
				ans=pow(16,i)*int(Binary_list1[i])
				cont.append(int(ans))


			end=sum(cont)
			storec=[]
			remc=[]
			
			while end!=0:
				store=end//8
				storec.append(store)
				rem=end%8
				remc.append(rem)
				end=store

			remc.reverse()
			for i in range(len(remc)):
				print(remc[i], end='')


		#Octal to Hexadecimal
		def maink():
			num1=input("Enter the Octal Number:")
			lis=[]
			for i in range(len(num1)):
				lis.append(num1[i])
					
			lis.reverse()
			cont=[]
			for i in range(len(lis)):
				ans=pow(8,i)*int(lis[i])
				cont.append(int(ans))

			num=sum(cont)
			dic={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
			storec=[]
			remc=[]
			while num!=0:
				store=num//16
				storec.append(store)
				rem=num%16
				remc.append(rem)
				num=store

			remc.reverse()
			for i in range(len(remc)):
				if remc[i] not in dic:
					print(remc[i], end='')
				else:
					print(dic[remc[i]] , end='')



	#Function calling

		if choice==1:
			main()
		elif choice==2:
			maina()
		elif choice==3:
			mainb()
		elif choice==4:
			mainc()
		elif choice==5:
			maind()
		elif choice==6:
			maine()
		elif choice==7:
			mainf()
		elif choice==8:
			maing()
		elif choice==9:
			mainh()
		elif choice==10:
			maini()
		elif choice==11:
			mainj()
		elif choice==12:
			maink()
		elif choice==13:
			break
			

except:
  print("Please insert valid input!")





