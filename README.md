# BittrexTools
 A very basic set of API functions to be used with Bittrex API v3. Only covers the bare minimum required to setup a simple bot or controls. No tests and haven't tested if install grabs dependencies after splitting off of main bot project. See EOF for very short dependency list.

<h2><b>Inital Use</b></h2>

<h3><u>Create btxConn object</u></h3>
    
    btxConn = BittrexConnection(apiKey, apiSecret, apiBaseURL='https://api.bittrex.com/v3')
    
<li>BaseURL is the url to the api. Defaults to https://api.bittrex.com/v3 but is an option in case of future changes.
<br><br>
<h2><b>Methods</b></h2>
Here are available methods including any optional args defaults.
<br><br>
<h3><u>Get current fee rate</u></h3>

    btxConn.get_current_fee_rate()
<li>Returns a float.
<li>Does comparison using current volume.
<li>!!!Does not automatically update if Bittrex changes their fee rates
<br><br>
<h3><u>Send a get request</u></h3>

    get_any(uriEnding, content='')
<li>Returns a parsed json object
<li>uriEnding should match Bittrex's documentation, including any slashes
<br><br>
<h3><u>Place an order</u></h3>
    
    btxConn.place_order(
        marketSymbol,
        direction, 
        orderLimit='', 
        quantity='', 
        orderType='LIMIT', 
        ceiling='', 
        timeInForce='GOOD_TIL_CANCELLED', 
        clientOrderId='', 
        useAwards='FALSE', 
        content = ""
        )
<li>Defaults allow for minimal limit orders but should be useable for any supported kind of order.
<li>Returns a parsed json object
<br><br>
<h3><u>Delete an order</u></h3>

    btxConn.delete_order(uuid)

<li>Returns a parsed json object
<br><br>

<h2><b>Dependencies</b></h2>
<li>hashlib
<li>time
<li>hmac
<li>requests
<li>json