$urls = Get-Content ".\soda.txt"

foreach ($url in $urls) {
    start-process chrome.exe $url
}