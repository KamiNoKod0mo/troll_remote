import pygame
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def set_system_volume(volume_level):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        # O volume deve estar entre 0.0 e 1.0
        #print(volume)
        
        try:
            unmute_windows()
            volume.SetMasterVolumeLevelScalar(volume_level, None)
        except:
            pass
    
def play_audio(file_path,vol):
    pygame.init()
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        # Aguarda o final da reprodução do áudio
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
            set_system_volume(vol)
            unmute_windows()
    except:
        pass
            
def unmute_windows():
    
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMute(0, None)  # Desmuta o som'
   

