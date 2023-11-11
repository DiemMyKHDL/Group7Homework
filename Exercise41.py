MusicalNoteName=input('Enter the musical note name: ')
Octave=int(input('Enter the octave number: '))
if MusicalNoteName=='C':
    Frequency= 261.63/ 2**(4-Octave)
elif MusicalNoteName=='D':
    Frequency= 293.66/ 2**(4-Octave)
elif MusicalNoteName=='E':
    Frequency= 329.63/ 2**(4-Octave)
elif MusicalNoteName=='F':
    Frequency= 349.23/ 2**(4-Octave)
elif MusicalNoteName=='G':
    Frequency= 392.00/ 2**(4-Octave)
elif MusicalNoteName=='A':
    Frequency= 440.00/ 2**(4-Octave)
elif MusicalNoteName=='B':
    Frequency= 493.88/ 2**(4-Octave)
print('Frequency of ',MusicalNoteName, Octave, ' is: ', round(Frequency,2),'Hz', sep='')