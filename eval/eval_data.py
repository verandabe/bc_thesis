#import sys
#sys.path.append('./enums/')
#sys.path.append('./classes/')
#sys.path.append('./tools/')
#sys.path.append('./')
#sys.path.append('./')


import os
from RephrasErIch import RephrasErIch
from Forms import Form

datadir = 'eval/data/'

def read_text_file(filename):
    form = None
    protg = None
    text = None

    with open(datadir+filename, 'r') as tf:
        info = tf.read()
        info = info.split('</>\n')
        for i in range(3):
            info[i] = info[i].split('::')[1]
        form, protg, text = info[0], info[1], info[2]

    return (form, protg, text)


def create_pairs():
    for filename in os.listdir(datadir):
        if 'rephrased_'+filename not in os.listdir(datadir+'rephrased/'):
            if os.path.isfile(datadir+filename):
                form, protg, text = read_text_file(filename)

                print('form:', form)
                print('object form:', Form[form])
                
                rerich = RephrasErIch(Form[form])
                rerich.create_protagonist(protg)
                rephrased_text = rerich.rephrase(text)
                
                with open(datadir+'rephrased/rephrased_' + filename, 'w') as rf:
                    rf.write("Metadata: from_form=" + form + ", protagonist=" + protg + '\n')
                    rf.write("Original: " + text)
                    rf.write("\n")
                    rf.write("Rephrased: " + rephrased_text)
            
