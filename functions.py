from youtube_transcript_api import YouTubeTranscriptApi
import re
stopwords = ['a', 'about', 'above', 'across', 'after', 'afterwards' , 'again', 'against', 'all', 'almost', 'alone', 'along' , 'already', 'also', 'although', 'always', 'am', 'among' , 'amongst', 'amoungst', 'amount', 'an', 'and', 'another' , 'any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere' , 'are', 'around', 'as', 'at', 'back', 'be', 'became' , 'because', 'become', 'becomes', 'becoming', 'been' , 'before', 'beforehand', 'behind', 'being', 'below' , 'beside', 'besides', 'between', 'beyond', 'bill', 'both' , 'bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant' , 'co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de' , 'describe', 'detail', 'did', 'do', 'done', 'down', 'due' , 'during', 'each', 'eg', 'eight', 'either', 'eleven', 'else' , 'elsewhere', 'empty', 'enough', 'etc', 'even', 'ever' , 'every', 'everyone', 'everything', 'everywhere', 'except' , 'few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first' , 'five', 'for', 'former', 'formerly', 'forty', 'found' , 'four', 'from', 'front', 'full', 'further', 'get', 'give' , 'go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her' , 'here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers' , 'herself', 'him', 'himself', 'his', 'how', 'however' , 'hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed' , 'interest', 'into', 'is', 'it', 'its', 'itself', 'keep' , 'last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made' , 'many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine' , 'more', 'moreover', 'most', 'mostly', 'move', 'much' , 'must', 'my', 'myself', 'name', 'namely', 'neither', 'never' , 'nevertheless', 'next', 'nine', 'no', 'nobody', 'none' , 'noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of' , 'off', 'often', 'on','once', 'one', 'only', 'onto', 'or' , 'other', 'others', 'otherwise', 'our', 'ours', 'ourselves' , 'out', 'over', 'own', 'part', 'per', 'perhaps', 'please' , 'put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed' , 'seeming', 'seems', 'serious', 'several', 'she', 'should' , 'show', 'side', 'since', 'sincere', 'six', 'sixty', 'so' , 'some', 'somehow', 'someone', 'something', 'sometime' , 'sometimes', 'somewhere', 'still', 'such', 'system', 'take' , 'ten', 'than', 'that', 'the', 'their', 'them', 'themselves' , 'then', 'thence', 'there', 'thereafter', 'thereby' , 'therefore', 'therein', 'thereupon', 'these', 'they' , 'thick', 'thin', 'third', 'this', 'those', 'though', 'three' , 'three', 'through', 'throughout', 'thru', 'thus', 'to' , 'together', 'too', 'top', 'toward', 'towards', 'twelve' , 'twenty', 'two', 'un', 'under', 'until', 'up', 'upon' , 'us', 'very', 'via', 'was', 'we', 'well', 'were', 'what' , 'whatever', 'when', 'whence', 'whenever', 'where' , 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon' , 'wherever', 'whether', 'which', 'while', 'whither', 'who' , 'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with' , 'within', 'without', 'would', 'yet', 'you', 'your' , 'yours', 'yourself', 'yourselves']

#['a', 'about', 'above', 'across', 'after', 'afterwards'] 
#['again', 'against', 'all', 'almost', 'alone', 'along'] 
#['already', 'also', 'although', 'always', 'am', 'among'] 
#['amongst', 'amoungst', 'amount', 'an', 'and', 'another'] 
#['any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere'] 
#['are', 'around', 'as', 'at', 'back', 'be', 'became'] 
#['because', 'become', 'becomes', 'becoming', 'been'] 
#['before', 'beforehand', 'behind', 'being', 'below'] 
#['beside', 'besides', 'between', 'beyond', 'bill', 'both'] 
#['bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant'] 
#['co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de'] 
#['describe', 'detail', 'did', 'do', 'done', 'down', 'due'] 
#['during', 'each', 'eg', 'eight', 'either', 'eleven', 'else'] 
#['elsewhere', 'empty', 'enough', 'etc', 'even', 'ever'] 
#['every', 'everyone', 'everything', 'everywhere', 'except'] 
#['few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first'] 
#['five', 'for', 'former', 'formerly', 'forty', 'found'] 
#['four', 'from', 'front', 'full', 'further', 'get', 'give'] 
#['go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her'] 
#['here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers'] 
#['herself', 'him', 'himself', 'his', 'how', 'however'] 
#['hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed'] 
#['interest', 'into', 'is', 'it', 'its', 'itself', 'keep'] 
#['last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made'] 
#['many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine'] 
#['more', 'moreover', 'most', 'mostly', 'move', 'much'] 
#['must', 'my', 'myself', 'name', 'namely', 'neither', 'never'] 
#['nevertheless', 'next', 'nine', 'no', 'nobody', 'none'] 
#['noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of'] 
#['off', 'often', 'on','once', 'one', 'only', 'onto', 'or'] 
#['other', 'others', 'otherwise', 'our', 'ours', 'ourselves'] 
#['out', 'over', 'own', 'part', 'per', 'perhaps', 'please'] 
#['put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed'] 
#['seeming', 'seems', 'serious', 'several', 'she', 'should'] 
#['show', 'side', 'since', 'sincere', 'six', 'sixty', 'so'] 
#['some', 'somehow', 'someone', 'something', 'sometime'] 
#['sometimes', 'somewhere', 'still', 'such', 'system', 'take'] 
#['ten', 'than', 'that', 'the', 'their', 'them', 'themselves'] 
#['then', 'thence', 'there', 'thereafter', 'thereby'] 
#['therefore', 'therein', 'thereupon', 'these', 'they'] 
#['thick', 'thin', 'third', 'this', 'those', 'though', 'three'] 
#['three', 'through', 'throughout', 'thru', 'thus', 'to'] 
#['together', 'too', 'top', 'toward', 'towards', 'twelve'] 
#['twenty', 'two', 'un', 'under', 'until', 'up', 'upon'] 
#['us', 'very', 'via', 'was', 'we', 'well', 'were', 'what'] 
#['whatever', 'when', 'whence', 'whenever', 'where'] 
#['whereafter', 'whereas', 'whereby', 'wherein', 'whereupon'] 
#['wherever', 'whether', 'which', 'while', 'whither', 'who'] 
#['whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with'] 
#['within', 'without', 'would', 'yet', 'you', 'your'] 
#['yours', 'yourself', 'yourselves'] 

def wordListToFreqDict(wordlist): 
    wordfreq = [wordlist.count(p) for p in wordlist] 
    return dict(list(zip(wordlist,wordfreq))) 

def sortFreqDict(freqdict): 
    aux = [(freqdict[key], key) for key in freqdict] 
    aux.sort() 
    aux.reverse() 
    return aux 


def removeStopwords(wordlist, stopwords): 
    return [w for w in wordlist if w not in stopwords]

def transcriptify(video_id):
    return YouTubeTranscriptApi.get_transcript(video_id)

def scriptString(transcriptLibraries):
    tempDict = transcriptLibraries
    scriptStringVal = ""

    for i in tempDict:
        currChunk = i
        for key, value in currChunk.items() :
            if key == "text":
                scriptStringVal += value + ' '

    return scriptStringVal

def inputSafe(scriptString):
    scriptString = scriptString.lower()
    scriptString = remove_undesirables(scriptString)
    scriptString = ' '.join(word for word in scriptString.split() if word not in stopwords)
    return scriptString
    #re.sub(r'[^\w\s]', '', scriptString)

def remove_undesirables(str):
  undesirables = [",",".","?","!","'","\"","|","  ","(",")","{","}"]
  for undesirable in undesirables:
    str = str.replace(undesirable,"")
  return str

def parseData(videoID):

    transcript = inputSafe(scriptString(transcriptify(videoID)))
    wordlist = transcript.split()

    return str(sortFreqDict(wordListToFreqDict(removeStopwords(wordlist, stopwords))))