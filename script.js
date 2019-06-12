// Create a request variable and assign a new XMLHttpRequest object to it.
var request1 = new XMLHttpRequest()
var request2 = new XMLHttpRequest()

function request(url) {
    const req = new XMLHttpRequest();
    req.open('GET', url, false); 
    req.send(null);
    if (req.status === 200) {
        return req.responseText;
    } else {
        console.log(req.status + " : " + req.statusText);
        return -1;
    }
}

function pausecomp(millis)
{
    var date = new Date();
    var curDate = null;
    do { curDate = new Date(); }
    while(curDate-date < millis);
}


function getStats()
{
	console.log("Lancemet du script ...")
	for (var i = 1; i < 1000; i++)
	{
		getHashTx(i);
	}
}

function getHashTx(id)
{
	console.log("On recupere les hash des tx : " + id)
		
	var result = request("https://www.coinexplorer.net/api/v1/PPC/block?height="+id)	
	var txList = JSON.parse(result)
	
	pausecomp(1001)
	
	for (var i = 0; i < txList.result.tx.length; i++)
	{
		getTxInfo(txList.result.tx[i])
		pausecomp(1001)
	}
	
	
	
	
}

function getTxInfo(hash)
{
	console.log("On recupere les infos des tx : " + hash) 
	var info = request("https://www.coinexplorer.net/api/v1/PPC/transaction?txid="+hash)
	console.log(info)	
}


getStats()

