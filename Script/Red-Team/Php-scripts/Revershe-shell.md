# TIPS 

If you have obtained a vulnerability such as RCE, file upload or something else, you can use the script below to spawn a shell or backconnect revershell. If the shell does not run see below

1. Make sure the target has internet access (internet access opened)
2. Try changing the port to a larger one such as 8080, 8888, etc. 
3. Encode your script using base64 and then decode it 
4. Encode your script using url encode 
5. Check the compiler 

## Php spawning cmd 

```Windows
https://pastebin.com/bFqVuGwv
```

## Php spawning bash 

```Linux
https://pastebin.com/QsSKm2F1
```

### Enum about the jail 

```
echo $SHELL
echo $PATH
env
export
pwd
```

*Windows Powershell Pro Tips 

- If you was gett the shell, change to powershell, you can run 

```
powershell -ep bypass 
```

Source 

- [Hacktrikcs Escaping from Jails](https://hacktricks.boitatech.com.br/linux-unix/privilege-escalation/escaping-from-limited-bash)
- [Hacktricks github escape from jails](https://github.com/HackTricks-wiki/hacktricks/blob/master/linux-hardening/useful-linux-commands/bypass-bash-restrictions.md)
- [0xffsec restricted-shells](https://0xffsec.com/handbook/shells/restricted-shells/)
- [Hacktrikcs powershell-for-pentesters](https://book.hacktricks.xyz/windows-hardening/basic-powershell-for-pentesters)