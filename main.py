from http.client import HTTPSConnection 

from sys import stderr

from json import dumps

from time import sleep



# if it doesn't work, try downloading the missing files with the 'npm install' command

# if it doesn't work, try downloading the missing files with the 'npm install' command

# if it doesn't work, try downloading the missing files with the 'npm install' command

# if it doesn't work, try downloading the missing files with the 'npm install' command

 

header_data = { 

	"content-type": "application/json", 

	"user-agent": "discordapp.com", 

	"authorization": "OTgxOTA2Njc5MDQ0MTI4ODQw.GXPx7g.Oc0kcAiD1QdvdTKqJ1Zl4q830c6h_NxLShe0PY",

	"host": "discordapp.com", 

	"referer": "https://discord.gg/8TMwJZMX" # it is irrelevant

} 

 

def get_connection(): 

	return HTTPSConnection("discordapp.com", 443) 

 

def send_message(conn, channel_id, message_data): 

    try: 

        conn.request("POST", f"/api/v6/channels/{channel_id}/messages", message_data, header_data) 

        resp = conn.getresponse() 

         

        if 199 < resp.status < 300: 

            print("Complete!")

            pass 

 

        else: 

            stderr.write(f"HTTP received {resp.status}: {resp.reason}\n") 

            pass 

 

    except: 

        stderr.write("There was an error trying to send the message\n") 

 

def main(): 

	message_data = { 

		"content": "your advertise message",

		"tts": "false", 

	} 





	
send_message(get_connection(), "984622712347578378", dumps(message_data)



	
if __name__ == '__main__':
	while True:    
		main()      
		sleep(300)
