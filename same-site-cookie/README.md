Website A --> SameSite Cookies enables --> http://127.0.0.1:3000

Website B --> CSRF --> http://192.168.70.128
>Use another host/IP for Website B, as in same-site the cookie test is not possible.

python3 -m http.server --bind 192.168.70.128 80
