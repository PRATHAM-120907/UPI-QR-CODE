import qrcode 

upi_id = input("ENTER YOUR -UPI ID- :")

phonePay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
google_Pay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
fam_Pay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"



phonePay_qr = qrcode.make(phonePay_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_Pay_url)
fam_Pay_qr = qrcode.make(fam_Pay_url)



phonePay_qr.save("phonePay_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")
fam_Pay_qr.save("fam_Pay_qr.png")

phonePay_qr.show()
paytm_qr.show()
google_pay_qr.show()
fam_Pay_qr.show()
