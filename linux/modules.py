import pygame,pulsectl,alsaaudio

def set_volume(volume_level):
    pulse = pulsectl.Pulse('set_volume')
    
    # Obter o nome do dispositivo de saída padrão
    default_sink_name = pulse.server_info().default_sink_name
    
    # Obter as informações do dispositivo de saída padrão
    sink_info = next(
        (sink for sink in pulse.sink_list() if sink.name == default_sink_name),
        None
    )

    if sink_info:
        # Ajustar o volume para o valor desejado (de 0.0 a 1.0)
        unmute_linux()
        pulse.volume_set_all_chans(sink_info, volume_level)
        pulse.close()
        
def play_audio(file_path,vol):
    pygame.init()
    #print(file_path)
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        # Aguarda o final da reprodução do áudio
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
            set_volume(vol)
            unmute_linux()
                                        
    except Exception as e:
        pass
    finally:
        pygame.quit()

# Chama a função para tirar o Linux do mudo

def unmute_linux():
    try:
        mixer = alsaaudio.Mixer()  # Use o mixer padrão
        mixer.setmute(0)  # Define o mudo como falso (0) para desmutar

    except Exception as e:
        pass     

