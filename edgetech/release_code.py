import subprocess
from pydub import AudioSegment
import os
#46257
#50672
release_code = "474724"

tone_pairs = {
	"1":["9500.wav", "9900.wav"],
	"2":["9500.wav", "10300.wav"],
	"3":["9500.wav", "10700.wav"],
	"4":["9900.wav", "10300.wav"],
	"5":["9900.wav", "10700.wav"],
	"6":["10300.wav", "10700.wav"]
}

tone = tone_pairs[release_code[0]]

binary_command = release_code[1:]
binary_command = bin(int(binary_command, 8))[2:]
binary_command = binary_command.zfill(15)

if not binary_command.count('1')%2:
	binary_command = binary_command+"0"
else:
	binary_command = binary_command+"1"

first_bit = tone[int(binary_command[0])]

#print(first_bit)

sound1 = AudioSegment.from_file(first_bit)
for i in binary_command[1:8]:
	#print(tone[int(i)])
	sound2 = AudioSegment.from_file(tone[int(i)])
	sound1 = sound1.append(sound2, crossfade=0)

gap = AudioSegment.from_file("gap.wav")
sound1 = sound1.append(gap, crossfade=0)

for i in binary_command[8:]:
	#print(tone[int(i)])
	sound2 = AudioSegment.from_file(tone[int(i)])
	sound1 = sound1.append(sound2, crossfade=0)

sound1.export("combined.wav", format='wav')

audio_file = os.getcwd()+'/combined.wav'
return_code = subprocess.call(["afplay", audio_file])