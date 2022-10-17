from django.shortcuts import render
# Create your views here.

def make_payment(request):
    if request.method == "POST":
        form = request.POST
        payment_status = "Payment KO"
        payment_message =''
        print(form)
        if form['number'] == '4485184053242274':
            payment_message = "ERROR: Insufficient funds on the account."
        elif form['number'] == '4485184053242273':
            payment_message = "ERROR: Time out from the bank"
        elif len(form['number']) == 16:
            payment_status = "Payment OK"
            payment_message = "Thank you for your order ! See you very soon."
        else:
            payment_message = "ERROR: Unable to process payment due to unknown error"
        # Send Payment result
        print(f"{form['number']} {payment_status}: {payment_message}")
        return render(request, 'home/payment_result.html', {"status": payment_status, "message": payment_message})
    return render(request, 'home/home.html')



