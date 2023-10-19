from twilio.rest import Client
import phonenumbers
from tkinter import *
from tkinter import messagebox

client = Client("ACcda7c51273b7a4585f20cdecffcb953a", "b7a8bdd24b5a22e433a6283d68df152a")

verify = client.verify.services("VAb4b4c016ac478ccb3e07ec26089d566e")

def is_valid_number(phone_number):
  try:
    parsed_number = phonenumbers.parse(phone_number)
    return phonenumbers.is_possible_number(parsed_number) and phonenumbers.is_valid_number(parsed_number)
  except:
    return False

def send_otp():
  phone_number = phone_entry.get()
  if is_valid_number(phone_number):
    verification = verify.verifications.create(to=phone_number, channel="sms")
    messagebox.showinfo("OTP SENDED", f"OTP has been sent to {phone_number}. Enter it below and click Verify")
  else:
    messagebox.showerror("INVALID PHONE NUMBER", f"{phone_number} is not a valid phone number.")

def verify_otp():
  phone_number = phone_entry.get()
  otp_code = otp_entry.get()
  verification_check = verify.verification_checks.create(to=phone_number, code=otp_code)
  if verification_check.status == "approved":
    messagebox.showinfo("OTP VERIFIED", "OTP is verified. You are logged in.")
  else:
    messagebox.showerror("INCORRECT OTP", "OTP is incorrect. Try again.")

window = Tk()
window.title("OTP Verification")
window.geometry("600x400")

label = Label(window, text="Enter your phone number and click Send OTP",font=("Times New Roman",17),fg="blue")
label.pack()

phone_entry = Entry(window,font=("Times New Roman",15))
phone_entry.pack(pady=20)

resend_button = Button(window, text="Resend OTP", command=send_otp, bg="green", width=10, font=("Times New Roman",12))
resend_button.pack(pady=10)

send_button = Button(window, text="Send OTP", command=send_otp, bg="green", width=10, font=("Times New Roman",12))
send_button.pack(pady=10)

label = Label(window, text="Verify the OTP",font=("Times New Roman",17),fg="blue")
label.pack(pady=10)

otp_entry = Entry(window,font=("Times New Roman",15))
otp_entry.pack(pady=20)

verify_button = Button(window, text="Verify OTP", command=verify_otp, bg="green", width=10, font=("Times New Roman",12))
verify_button.pack(pady=10)

window.mainloop()