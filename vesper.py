from Brain.aiBrain import replyBrain
from Brain.qna import questionsAnswers
from Body.Listen import micExecution
from Body.speak import Speak
def MainExe():
    while True:
        query=str(micExecution())
        querylen=len(query)
        
        if querylen<3:
            reply="Sorry i didn't get you. Please say that again"

        elif "what" in query or "who" in query or "where" in query or "when" in query or "why" in query or "how" in query:
            reply=questionsAnswers(query)
        
        else:
            reply=replyBrain(query)
        Speak(reply)