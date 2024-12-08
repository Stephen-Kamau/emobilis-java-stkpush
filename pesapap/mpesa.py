from base64 import b64encode
from datetime import datetime

import requests
from django.conf import settings
from pesapap.models import mpesaRequest


"""
ADVICE: put the variables in this class into an envrioment variable
"""
class STKPUSHSECRET:
    passkey = "XXXXXXXXXXXXXXXXX"
    business_short_code = 174379
    consumer_key = "XXXXXXXXXXXX"
    consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    onlinePayment_URL = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    auth_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    callback_url = "<yourdomain>/api/v1/stk-callback/"



STKPUSHSECRET = STKPUSHSECRET()


def access_token_mpesa(consumer_key, consumer_secret):
    credentials = f"{consumer_key}:{consumer_secret}"
    encoded_credentials = b64encode(credentials.encode('utf-8')).decode('utf-8')
    headers = {'Authorization': f"Basic {encoded_credentials}",'Content-Type': 'application/json'}
    r = requests.get(STKPUSHSECRET.auth_URL, headers=headers)
    json_response = r.json()
    access_token = json_response.get("access_token")
    return access_token


def current_time_stamp():
    unformatted_time = datetime.now()
    formatetted_time = unformatted_time.strftime("%Y%m%d%H%M%S")
    return formatetted_time


def getTime(unformatted_time):
    transation_time = str(unformatted_time)
    transation_date_time = datetime.strptime(transation_time, "%Y%m%d%H%M%S")
    return transation_date_time


def getPassword(business_short_code, passkey, timestamp):
    data = f"{business_short_code}{passkey}{timestamp}"
    encoded_string = b64encode(data.encode())
    return encoded_string.decode("utf-8")



# https://github.com/safaricom/mpesa-php-sdk/issues/51

def request_stk_push(amount,phone_number,account_reference="Zeddy Pay",transaction_description="",user=1):
    timestamp = current_time_stamp()
    password = getPassword(STKPUSHSECRET.business_short_code, STKPUSHSECRET.passkey, timestamp)
    access_token = access_token_mpesa(STKPUSHSECRET.consumer_key, STKPUSHSECRET.consumer_secret)
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": STKPUSHSECRET.business_short_code,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline", #"CustomerBuyGoodsOnline",
        "Amount": float(amount),
        "PartyA": str(phone_number),
        "PartyB": STKPUSHSECRET.business_short_code,
        "PhoneNumber": str(phone_number),
        "CallBackURL": STKPUSHSECRET.callback_url,
        "AccountReference": "Zeddy Pay Inc.",
        "TransactionReference": account_reference,
        "TransactionDesc": transaction_description,
    }
    response = requests.post(STKPUSHSECRET.onlinePayment_URL, json=request, headers=headers)
    response_data = response.json()
    if "errorCode" in response_data.keys():
        print(f"Error At the MPESA CODE  {response_data}")
        return response_data
    else:
        save_stkpush_request(response_data, phone_number, account_reference, transaction_description )
        return response_data


def save_stkpush_request(response_data, phone_number, account_reference, transaction_description):
    if "errorCode" in response_data.keys():
        print(f"we have received an error here    {response_data}")
        return response_data
    else:
        data = {}
        data["merchant_id"] = response_data["MerchantRequestID"]
        data["checkout_id"] = response_data["CheckoutRequestID"]
        data["res_code"] = response_data["ResponseCode"]
        data["res_text"] = response_data["ResponseDescription"]
        data["msg"] = response_data["CustomerMessage"]
        data["phone"] = phone_number
        data["ref"] = account_reference
        data["trans_date"] = transaction_description

        push_request_res = mpesaRequest.objects.create(**data)
        push_request_res.save()
        return response_data



