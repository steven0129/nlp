import sys
import os


class StanfordCoreNLP():
    def __init__(self, jarPath):
        self.root = jarPath
        self.tempSrcPath = 'temp'
        self.jarList = ['ejml-0.23.jar', 'javax.json.jar', 'jollyday.jar', 'joda-time.jar',
                        'protobuf.jar', 'slf4j-api.jar', 'slf4j-simple.jar', 'stanford-corenlp-3.8.0.jar', 'xom.jar']
        self.jarPath = ''
        self.buildjars()

    def buildjars(self):
        for jar in self.jarList:
            self.jarPath += self.root + jar + ';'

    def saveFile(self, path, sent):
        fp = open(path, 'wb')
        fp.write(sent.encode())
        fp.close()

    def delFile(self, path):
        os.remove(path)


class StanfordPOSTagger(StanfordCoreNLP):
    def __init__(self, jarPath, modelPath):
        StanfordCoreNLP.__init__(self, jarPath)
        self.modelPath = modelPath
        self.classfier = 'edu.stanford.nlp.tagger.maxent.MaxentTagger'
        self.delimiter = '/'
        self.__buildcmd()

    def __buildcmd(self):
        self.cmdline = 'java -cp "' + self.root + '*" ' + self.classfier + \
            ' -model "' + self.modelPath + '" -tagSeparator ' + self.delimiter
        print(self.cmdline)

    def tag(self, sent):
        self.saveFile(self.tempSrcPath, sent)
        tagtxt = os.popen(self.cmdline + ' -textFile ' +
                          self.tempSrcPath, 'r').read()
        self.delFile(self.tempSrcPath)
        return tagtxt

    def tagFile(self, inputPath, outPath):
        os.system(self.cmdline + ' -textFile ' + inputPath + ' > ' + outPath)
