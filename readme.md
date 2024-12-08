### STKPUSH: How it works;

1. Perfom Authentication via aut url - get an access token from it;
2. Extract the token form the response.
3. Create a request object as follows;
```json
{    
   "BusinessShortCode": "<<till>>",    
   "Password": "<<password generated from secret key/password as base64.encode(Shortcode+Passkey+Timestamp)>>",
   "Timestamp":"<<timestamp  as YYYYMMDDHHmmss>>",    
   "TransactionType": "CustomerPayBillOnline",    
   "Amount": "1",    
   "PartyA":"<<sending from number>>",    
   "PartyB":"<<174379/store/till etc>>",    
   "PhoneNumber":"<sending from number>>",    
   "CallBackURL": "<yourdomain/callback_end: Must allow post request",    
   "AccountReference":"<<order_id>>",    
   "TransactionDesc":"Test"
}

```

4. Sending the request (add headers as Bearer token)
5. Receive stk push success results; looks as follows
```json
{    
   "MerchantRequestID": "29115-34620561-1",    
   "CheckoutRequestID": "ws_CO_191220191020363925",    
   "ResponseCode": "0",    
   "ResponseDescription": "Success. Request accepted for processing",    
   "CustomerMessage": "Success. Request accepted for processing"
}
```
6. Receive response in the callback url (this is the callback you had on the request object), perfom actions to complete the process; Sample response;
```json
{    
   "Body": {        
      "stkCallback": {            
         "MerchantRequestID": "29115-34620561-1",            
         "CheckoutRequestID": "ws_CO_191220191020363925",            
         "ResultCode": 0,            
         "ResultDesc": "The service request is processed successfully.",            
         "CallbackMetadata": {                
            "Item": [{                        
               "Name": "Amount",                        
               "Value": 1.00                    
            },                    
            {                        
               "Name": "MpesaReceiptNumber",                        
               "Value": "NLJ7RT61SV"                    
            },                    
            {                        
               "Name": "TransactionDate",                        
               "Value": 20191219102115                    
            },                    
            {                        
               "Name": "PhoneNumber",                        
               "Value": 254708374149                    
            }]            
         }        
      }    
   }
}

```