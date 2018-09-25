import os
import cPickle
import numpy as np
from scipy.io.wavfile import read
from speakerfeatures import extract_features
import warnings
warnings.filterwarnings("ignore")
import time

def recog_speaker():
    #path to training data
    source   = "development_set\\"   

    modelpath = "speaker_models\\"

    test_file = "development_set_test.txt"        

    file_paths = open(test_file,'r')


    gmm_files = [os.path.join(modelpath,fname) for fname in 
                os.listdir(modelpath) if fname.endswith('.gmm')]
    #print gmm_files
    models    = [cPickle.load(open(fname,'r')) for fname in gmm_files]
    #models = cPickle.load(open("speaker_models/darsh/wav/file5.wav.gmm", "r"))
    #print "models:",models
    speakers   = [fname.split("\\")[-1].split(".gmm")[0] for fname 
                in gmm_files]
    #print speakers
     
    for path in file_paths:   
        
        path = path.strip()   
        print path
        sr,audio = read(source + path)
        vector = extract_features(audio,sr)
        #print vector
        log_likelihood = np.zeros(len(models)) 
        
        for i in range(len(models)):
            gmm = models[i]         #checking with each model one by one
            #print gmm
            scores = np.array(gmm.score(vector))
            #print scores
            log_likelihood[i] = scores.sum()
        
        winner = np.argmax(log_likelihood)
        #print winner
        #print "\tDetected as - ", speakers[winner]
        time.sleep(1.0)
    return speakers[winner]