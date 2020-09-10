import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate

#Señal 1
frecuencia770 = SinSignal(freq=770, amp=1, offset=0)
frecuencia1209 = SinSignal(freq=1209, amp=1, offset=0)
#Señal 2
frecuencia697 = SinSignal(freq=697, amp=1, offset=0)
frecuencia1477 = SinSignal(freq=1477, amp=1, offset=0)
#Señal 3
frecuencia770_2 = SinSignal(freq=770, amp=1, offset=0)
frecuencia1209_2 = SinSignal(freq=1209, amp=1, offset=0)
#Señal 4
frecuencia941 = SinSignal(freq=941, amp=1, offset=0)
frecuencia1336 = SinSignal(freq=1336, amp=1, offset=0)

#Señal 1 W
wave_770 = frecuencia770.make_wave(duration=0.5, start=0, framerate=44100)
wave_1209 = frecuencia1209.make_wave(duration=0.5, start=0, framerate=44100)
#Señal 2 W
wave_697 = frecuencia697.make_wave(duration=0.5, start=0.5, framerate=44100)
wave_1477 = frecuencia1477.make_wave(duration=0.5, start=0.5, framerate=44100)
#Señal 3 W
wave_770_2 = frecuencia770_2.make_wave(duration=0.5, start=1.0, framerate=44100)
wave_1209_2 = frecuencia1209_2.make_wave(duration=0.5, start=1.0, framerate=44100)
#Señal 4 W
wave_941 = frecuencia941.make_wave(duration=0.5, start=1.5, framerate=44100)
wave_1336 = frecuencia1336.make_wave(duration=0.5, start=1.5, framerate=44100)

wave_sonido = (wave_770 + wave_1209) + (wave_697 + wave_1477) + (wave_770_2 + wave_1209_2) + (wave_941 + wave_1336)

wave_sonido.write("Funcionando.wav")
