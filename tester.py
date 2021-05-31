import requests

                                                          
if __name__ == '__main__':
                                             
    hosts_file = open('dns','r')
    no = 0                                     
    valid = "aws"
    user_agent = {
	"User-Agent" : "Browser: Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36"
    }
           
    print("\nSCRIPT BY - t.me/indisputable07")           
                    
    print(" ╔╗ ╔═╗╔╦╗╔╗ ╔═╗╦ ╦   ╔═╗")
    print(" ╠╩╗╠═╣ ║║╠╩╗║ ║╚╦╝   ╠═╣" ) 
    print(" ╚═╝╩ ╩═╩╝╚═╝╚═╝ ╩────╩ ╩=")                            
    print("\n[-] SCRIPT RUNNING...")
    for host in hosts_file:
        no += 1
        host = host.strip('\n')
        host2 = host
                                                                                                                                                                               
        host = "http://check-host.net/ip-info?host=" +host
        response = requests.get(host,headers=user_agent,verify=False)
        if(valid in response.text):                     
            print(f'[-] Checking [{no}] {host2} ->Valid Host!! Cloudfront Found In Response')
                                                                
            with open("scraped.txt","a") as mano:
                mano.write(host2+"\n")
        else:                   
            print(f'[-] Checking [{no}] {host2} ->Invalid Host!!')                                                                                            
    print("\nPOSSIBLE HOSTS HAVE BEEN WRITTEN TO scraped.txt ")
    print("\nCOMMANDS \n+ nano scraped.txt TO SEE THEM")
