# Red Teaming 

Welcome to path red teaming or pentesting for OSINT, on this path there are script and about tips about for enumeration, OSINT and other tips 

## Tips Reverse Shell 

1. Check the operating system target 
2. Check the network or internet access on the target (internet access opened)
3. Cehck the vuln, you can check it by run the command like sleep, delay or trying to wget on your local machine 
4. Check is it a sandbox like in a container? Or directly to the operating system. If it's a container then you have to bypass
5. Check the installed software on the target 
6. Check the compiler on the target 
7. If AV is detected then you can encode into base64, url encode or try to enumerate what caused the payload to be detected such as checking functions, commands and others. 
8. Change the port listener to bigger 
9. If there is a restrictions you should to bypass
10. If you have successfully connected with target, swtich to powershell if the Windows, if Linux switch to fully tty shell 

## Soon will added (tamplate)