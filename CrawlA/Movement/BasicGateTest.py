#include os
#include math

output_file = 'output/mvnt'

def file_writeout(srvN, pos);
    with open(output_file, 'a') as f:
        f.write(srvN, ' to ', pos)
    return 0
        
class leg(legN):
    def __init__(legN):
        srvHY = 'srv' + legN + 'HY'
        srvHX = 'srv' + legN + 'HX'
        srvEY = 'srv' + legN + 'EY'
