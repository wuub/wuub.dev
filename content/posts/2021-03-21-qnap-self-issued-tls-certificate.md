title: How to setup QNAP to correctly serve TLS certificate
date: 2021-03-20 23:24
tags: qnap, https
slug: qnap-https-own-ca
description: How to make QNAP server correct TLS cesrtificate 
status: draft

# How to setup QNAP to correctly serve TLS certificate

1. Go to Control Panel -> Security -> Certificate and Private Key 
2. Clicke `Replace certificate`
3. Give your private key and site certiciate to te script.
4. If you choose the Intermediate CA or nor apparently makes no difference.
5. `openssl s_client -showcerts -connect [your-qnap-address]:443`
6. Ovserve how only one certificate is provided. This means there's no valid crtificate chain, and you'll see a broken padlck.
7. SSH to your Qnap NAS. `ssh admin@[your-qnap-address]`
8. `cd /etc/stunnel`
9. `vim stunnel.pem`
10. append the intermediate CA certificate at the end of this file. Make sure to watch your whitespaces and not pad with anythin extra.
11. Run `/etc/init.d/stunnel.sh restart`
12. You should now be serving correct TLS certificate chain to the browser. 