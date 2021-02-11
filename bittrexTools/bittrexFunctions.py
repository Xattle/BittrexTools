import hashlib
import time
import hmac
import requests
import json

class BittrexConnection:
    def __init__(self, apiKey, apiSecret, apiBaseURL) -> None:
        self.apiKey = apiKey
        self.apiSecret = apiSecret
        self.apiBaseURL = apiBaseURL

    def get_current_fee_rate(self):
        currentVolume = float(self.get_any("/account/volume")['volume30days'])
        if currentVolume <= float(25000):
            currentrate = float(.0035)
        elif currentVolume <= float(50000):
            currentrate = float(.0025)
        elif currentVolume <= float(1000000):
            currentrate = float(.0018)
        elif currentVolume <= float(10000000):
            currentrate = float(.0015)
        elif currentVolume <= float(60000000):
            currentrate = float(.001)
        elif currentVolume <= float(100000000):
            currentrate = float(.0008)
        else:
            currentrate = float(.0005)

        return currentrate
    
    def get_any(self, uriEnding, content = ""):
        timestamp = str(int(time.time()*1000))

        apiContent = content
        apiContentHash = hashlib.sha512(apiContent.encode('latin1')).hexdigest()

        thisRequestUri = self.apiBaseURL + uriEnding
        thisRequestMethod = "GET"
        thisPresign = timestamp + thisRequestUri + thisRequestMethod + apiContentHash
        thisSignature = hmac.new(self.apiSecret.encode('latin1'), thisPresign.encode('latin1'), hashlib.sha512).hexdigest()

        thisResponse = requests.get(
            thisRequestUri,
            headers={
                'Content-type' : 'application/json',
                'Api-Key' : self.apiKey,
                'Api-Timestamp' : timestamp,
                'Api-Content-Hash' : apiContentHash,
                'Api-Signature' : thisSignature,
            }
        ).json()

        return thisResponse

    #Assumes parameters for a simple limit order by default. See https://bittrex.github.io/api/v3#/definitions/NewOrder for more details.
    def place_order(self, marketSymbol, direction, orderLimit='', quantity='', orderType='LIMIT', ceiling='', timeInForce='GOOD_TIL_CANCELLED', clientOrderId='', useAwards='FALSE', content = ""):
        timestamp = str(int(time.time()*1000))

        thisOrder = {
            "marketSymbol": marketSymbol,
            "direction": direction,
            "type": orderType,
            "timeInForce": timeInForce
            }
        
        if quantity != '':
            thisOrder["quantity"] = quantity
        if ceiling != '':
            thisOrder["ceiling"] = ceiling
        if orderLimit != '':
            thisOrder["limit"] = orderLimit
        if clientOrderId != '':
            thisOrder["clientOrderId"] = clientOrderId
        if useAwards != '':
            thisOrder["useAwards"] = useAwards    

        apiContent = json.dumps(thisOrder)
        apiContentHash = hashlib.sha512(apiContent.encode('latin1')).hexdigest()

        thisRequestUri = self.apiBaseURL + "/orders"
        thisRequestMethod = "POST"
        thisPresign = timestamp + thisRequestUri + thisRequestMethod + apiContentHash
        thisSignature = hmac.new(self.apiSecret.encode('latin1'), thisPresign.encode('latin1'), hashlib.sha512).hexdigest()

        thisResponse = requests.post(
            thisRequestUri,
            headers={
                'Content-type' : 'application/json',
                'Api-Key' : self.apiKey,
                'Api-Timestamp' : timestamp,
                'Api-Content-Hash' : apiContentHash,
                'Api-Signature' : thisSignature,
            },
            data=json.dumps(thisOrder)
        ).json()

        return thisResponse

    def delete_order(self, uuid):
        timestamp = str(int(time.time()*1000))

        apiContent = ''
        apiContentHash = hashlib.sha512(apiContent.encode('latin1')).hexdigest()

        thisRequestUri = f"{self.apiBaseURL}/orders/{uuid}"
        thisRequestMethod = "DELETE"
        thisPresign = timestamp + thisRequestUri + thisRequestMethod + apiContentHash
        thisSignature = hmac.new(self.apiSecret.encode('latin1'), thisPresign.encode('latin1'), hashlib.sha512).hexdigest()

        thisResponse = requests.delete(
            thisRequestUri,
            headers={
                'Content-type' : 'application/json',
                'Api-Key' : self.apiKey,
                'Api-Timestamp' : timestamp,
                'Api-Content-Hash' : apiContentHash,
                'Api-Signature' : thisSignature,
            }
        ).json()

        return thisResponse
