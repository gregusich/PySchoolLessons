sec = int ( input() )
minutes = sec // 60 % 60 
chasy = sec // 3600 % 24
days = sec // ( 3600 * 24)
secs = sec % 60
print (str(chasy) + ':' + str (minutes) + ':' + str (secs) )
