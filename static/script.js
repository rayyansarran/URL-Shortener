function copyToClipboard() {
    var shortUrl = document.getElementById("shortenedUrl").getAttribute("href");
    var fullUrl = window.location.origin + '/' + shortUrl;
    var tempInput = document.createElement("input");
    tempInput.value = fullUrl;
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand("copy");
    document.body.removeChild(tempInput);
    alert("Copied the URL: " + fullUrl);
}