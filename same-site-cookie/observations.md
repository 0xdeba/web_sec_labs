Same-Site Strict
--> Uses Referer Header to determine if the request is make from same-site or not.

--> Client's Browser that is making the request Automatically adds Referer Header.


How browser knows if a request is same-site or not??
Using Referer Request Header

In a request, modifying referer header to the same-site can bypass but, browser does not allows to modify it programatically.
```fetch('http://127.0.0.1:3000/cookie',
            {
                headers:{
                    "Referer":"http://127.0.0.1:3000"
                }
            }
        )```

fails

Browser Forbidden Headers