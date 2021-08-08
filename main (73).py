print("Welcome to Dhruv's Currency Converter!")
val=str(input('Enter the output currency code:'))
if(val=='INR'):
    USD=float(input('Enter the amount in USD:'))
    INR=USD*74.24
    print('%0.3f USD is equal to %0.3f INR' %(USD, INR))
elif(val=='MXN'):
    USD=float(input('Enter the amount in USD:'))
    MXN=USD*20.02
    print('%0.3f dollars is equal to %0.3f Mexican Pesos' %(USD, MXN))
elif(val=='EUR'):
    USD=float(input('Enter the amount in USD:'))
    EUR=USD*0.85
    print('%0.3f dollars is equal to %0.3f euros' %(USD, EUR))
elif(val=='JPY'):
    USD=float(input('Enter the amount in USD:'))
    JPY=USD*110.25
    print('%0.3f dollars is equal to %0.3f Japanese Yen' %(USD, JPY))
elif(val=='AUD'):
    USD=float(input('Enter the amount in USD:'))
    AUD=USD*1.36
    print('%0.3f dollars is equal to %0.3f Australian Dollars' %(USD, AUD))
elif(val=='BTC'):
    USD=float(input('Enter the amount in USD:'))
    BTC=USD*0.000022
    print('%0.3f dollars is equal to %0.3f Bitcoin' %(USD, BTC))
