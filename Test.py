urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='login.microsoftonline.com', port=443): Max retries exceeded with url: /709c2643-b1a9-4415-ad0f-521cfa6ba3f5/v2.0/.well-known/openid-configuration (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:997)')))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\e175060\OneDrive - Applied Materials\AUTO ANIMATION REQUESTS\Dataverse_rest_v002.py", line 55, in <module>
    auth_token = pu.ms_authorization(config)        #Getting an authorization token
  File "C:\Users\e175060\OneDrive - Applied Materials\AUTO ANIMATION REQUESTS\projectutils.py", line 44, in ms_authorization
    db_app = msal.ConfidentialClientApplication(
  File "C:\Users\e175060\AppData\Local\Programs\Python\Python310\lib\site-packages\msal\application.py", line 456, in __init__
    self.authority = Authority(
  File "C:\Users\e175060\AppData\Local\Programs\Python\Python310\lib\site-packages\msal\authority.py", line 100, in __init__
    openid_config = tenant_discovery(
  File "C:\Users\e175060\AppData\Local\Programs\Python\Python310\lib\site-packages\msal\authority.py", line 160, in tenant_discovery
    resp = http_client.get(tenant_discovery_endpoint, **kwargs)
  File "C:\Users\e175060\AppData\Local\Programs\Python\Python310\lib\site-packages\msal\individual_cache.py", line 269, in wrapper
    value = function(*args, **kwargs)
  File "C:\Users\e175060\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 600, in get
    return self.request("GET", url, **kwargs)
  File "C:\Users\e175060\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\e175060\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\e175060\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 563, in send
    raise SSLError(e, request=request)
requests.exceptions.SSLError: HTTPSConnectionPool(host='login.microsoftonline.com', port=443): Max retries exceeded with url: /709c2643-b1a9-4415-ad0f-521cfa6ba3f5/v2.0/.well-known/openid-configuration (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:997)')))
