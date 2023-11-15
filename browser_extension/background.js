chrome.tabs.onActivated.addListener(function (activeInfo) {
    chrome.tabs.get(activeInfo.tabId, function (tab) {
        y = tab.url;
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                console.log(this.responseText);
            }
        };
        xhttp.open("POST", "http://127.0.0.1:5000/send_url");
        xhttp.send("url=" + y);

    });
});


chrome.tabs.onUpdated.addListener((tabId, change, tab) => {
    if (tab.active && change.url) {

        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                console.log(this.responseText);
            }
        };
        xhttp.open("POST", "http://127.0.0.1:5000/send_url");
        xhttp.send("url=" + change.url);

    }
});