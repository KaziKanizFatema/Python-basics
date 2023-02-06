num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 
            90: 'Ninety', 0: 'Zero', 100 : 'One hundred', 200 : 'Two hundred', 300 : 'Three hundred',
            400 : 'Four hundred', 500 : 'Five hundred', 600 : 'Six hundred', 700 : 'Seven hundred', 800 : 'Eight hundred',
            900 : 'Nine hundred'}

def n2w(n):
        if n in num2words:

            print(num2words[n])
        
        elif n > 100:
            print(num2words[n - n % 100] +" " + num2words[n % 100 - n % 10].lower() +" "+ num2words[n % 10].lower())

        elif n > 20:
            print(num2words[n - n % 10] +" "+ num2words[n % 10].lower())            

        else:
            print('The number is out of range')

n = int(input("Enter number: "))
n2w(n)