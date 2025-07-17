# Experiment 1

> Serve PQC NGINX with pre-configured example PQC cert
> and hit it with PQC curl

## Step 1: start NGINX

```bash
docker compose up nginx
```

This will start NGINX and attach it to a terminal

## Step 2: try using non-PQC curl

As a control test.
We want to know what would happen if we use client that does not support PQC
algorithm.

```console
$ curl https://localhost:4433
curl: (35) OpenSSL/3.0.13: error:0A000410:SSL routines::sslv3 alert handshake failure

$ curl -k https://localhost:4433
curl: (35) OpenSSL/3.0.13: error:0A000410:SSL routines::sslv3 alert handshake failure
```

`-k` means to not verify certificate, just use it to encrypt connection
immediately.

We can see that client does not know how to encrypt communication using PQC
algorithm presented in certificate.

## Step 3: try using PQC curl

```bash
docker compose run --rm curl
```

Curl as configured in docker compose has PQC enabled.
It will be able to get content of the page normally, which is:

```html
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

