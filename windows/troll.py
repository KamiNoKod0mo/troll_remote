from modules import *
import argparse,socket,os
from colorama import init,Fore,Style

init(autoreset=True)
#Aapresentação

BANNER = f'''{Fore.BLUE}          _____                      _              
         |_   _|                    | |             
           | |      ___     _ __    | |__      ___  
           | |     / _ \   | '_ \   | '_ \    / _ \ 
           | |    | (_) |  | | | |  | | | |  | (_) |
           \_/     \___/   |_| |_|  |_| |_|   \___/      
                                                                           
        Madeby:KamiNoKod0mo             Version: 1.0{Style.RESET_ALL}\n'''

audios = ['indian.mp3','nossa.mp3','vai-tomar-no-seu-c#.mp3','cristiano.mp3','baphomet-xandão.mp3','eu-não-cometo-erros.mp3',
          'ai-chaves.mp3','to-tremendo-de-medo.mp3','tira-que-eu-vo-caga.mp3','luan.mp3']

audioP = ""
for i, audio in enumerate(audios):
    audioP += f'[{i}] {audio:<30}'  # Ajuste de 50 espaços para alinhar melhor

    if (i + 1) % 2 == 0 or i == len(audios) - 1:
        audioP += '\n'

def execution():
    set_system_volume(vol)
    file =os.path.join(os.path.dirname(os.path.realpath(__file__)), 'audio', audios[audio])
    play_audio(f"{file}",vol)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='How use this tool')
    parser.add_argument('-i', action="store_true", help='provide interative choice')
    parser.add_argument('-listen', action="store_true", help='provide sock for play audio remote')
    parser.add_argument('-port', action="store", help='set a listen port')
    parser.add_argument('-audio', action="store", help='Set a audio[0-9]')
    parser.add_argument('-vol', action="store", help='Set volume[0.1-1.0]')

    args = parser.parse_args()
    if not (args.i or args.listen or args.port or args.audio or args.vol):
        print("Nenhum argumento foi fornecido. Veja a mensagem de ajuda:")
        parser.print_help()
        exit()


if args.i:
    print(f'{BANNER}')
    print(f'{audioP}')
    while True:
        audio = (input(f"\n{Fore.LIGHTBLUE_EX}[*] Select the audio [default=0]: {Style.RESET_ALL}"))
        if audio == '':
            audio = '0'
        if audio.isnumeric() and int(audio) >=0 and int(audio) <=9:
            break
    while True:
        vol = (input(f"{Fore.LIGHTBLUE_EX}[*] Volume [default=0.1]: {Style.RESET_ALL}"))
        if vol == '':
            vol = '0.1'
        #print(vol)
        if vol.isalpha() and vol.isalnum():
            pass
        else:
            if float(vol) >= 0.1 and float(vol) <= 1.0:
                break
    audio = int(audio)
    vol = float(vol)
    print(f"{Fore.GREEN}[*] Executando a audio...{Style.RESET_ALL}")
    execution()
elif args.listen:
    host_name = socket.gethostname()
    host = socket.gethostbyname(host_name)
    
    mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    mysocket.bind((host,int(args.port)))
    mysocket.listen()
    # Espera por uma conexão
    conexao, endereco_cliente = mysocket.accept()
    while True:            
        #print(f"Conexão estabelecida com {endereco_cliente}")
        try:
            conexao.send(BANNER.encode('utf-8'))
            conexao.send('\n'.encode('utf-8'))
            conexao.send(audioP.encode('utf-8'))
            conexao.send('\n'.encode('utf-8'))
            
            while True:
                conexao.send((f"\n{Fore.LIGHTBLUE_EX}[*] Select the audio [default=0]: {Style.RESET_ALL}").encode('utf-8'))
                audio = conexao.recv(1024)
                if audio == b'':
                    pass
                else:
                    audio = audio.decode().replace('\n', '')
                    
                    #conexao.send(qa.encode('utf8'))
                    if audio == '':
                        audio = '0'
                    if audio.isnumeric() and int(audio) >=0 and int(audio) <=9:
                        break
            while True:
                conexao.send((f"{Fore.LIGHTBLUE_EX}[*] Volume [default=0.1]: {Style.RESET_ALL}").encode('utf-8'))
                vol = conexao.recv(1024)
                if vol == b'':
                    pass
                else:
                    vol = vol.decode().replace('\n', '')
                    
                    if vol == '':
                        vol = '0.1'
                    #print(vol)
                    if vol.isalpha() and vol.isalnum():
                        pass
                    else:
                        if float(vol) >= 0.1 and float(vol) <= 1.0:
                            break
        except:
            pass
        
        if audio != b'' and vol !=b'':
        #print(audio)
            audio = int(audio)
            vol = float(vol)
            conexao.send((f"{Fore.GREEN}[*] Executando a audio...{Style.RESET_ALL}\n").encode('utf-8'))
            execution()
        else:
            conexao.close()
            conexao, endereco_cliente = mysocket.accept()
        #mysocket.close()
    #print(float(vol))
else:
    audio = int(args.audio)
    vol = float(args.vol)
    print((f"{Fore.GREEN}[*] Executando a audio...{Style.RESET_ALL}"))
    execution()



