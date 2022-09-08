# ARİN WEB
# https://arinweb.xyz
import json
# Variables
jsonConfig = json.load(open("config.json"))
userReplyList = []
replyList = []
reply = ""
question = json.load(open(jsonConfig["jsonFileName"]))
totalQuestion = len(question)
questionPoint = jsonConfig["question"]["totalPoint"]/totalQuestion
point = 0
trueQuestion = 0
falseQuestion = 0
emptyQuestion = 0
questionNumber = 0

for x in question:
  questionNumber+=1
  print(" Soru "+str(questionNumber)+": "+x[jsonConfig["question"]["name"]])
  for option in jsonConfig["question"]["option"]:
    print("  "+option+") "+x[option])
  reply = x[jsonConfig["question"]["reply"]]
  replyList.append(x["cevap"])
  while True:
    replyIN = input("  Cevap Şıkkı Yaz: ")
    print("\n")
    optionCount = jsonConfig["question"]["option"].count(replyIN)
    if jsonConfig["question"]["skip"] == True:
      if optionCount > 0 or replyIN == "":
        userReplyList.append(replyIN)
        if replyIN == reply:
          if jsonConfig["question"]["point"]["status"] == True:
            questionPoint = x[jsonConfig["question"]["point"]["name"]]
          point += questionPoint
        elif replyIN == "":
          print("    Soru boş geçildi!")
          emptyQuestion+=1
        trueQuestion = point/questionPoint
        falseQuestion = totalQuestion-trueQuestion-emptyQuestion
        break
      else:
        print("    Geçersiz karakter!")
    else:
      if optionCount > 0:
        userReplyList.append(replyIN)
        if replyIN == reply:
          if jsonConfig["question"]["point"]["status"] == True:
            questionPoint = x[jsonConfig["question"]["point"]["name"]]
          point += questionPoint
        trueQuestion = point/questionPoint
        falseQuestion = totalQuestion-trueQuestion-emptyQuestion
        break
      else:
        print("    Geçersiz karakter!")
else:
  print("\nSınav Sona Erdi!")
  #Sınav Puan taranıyor
  print("  Senin Cevapların:\n   "+str(userReplyList))
  print("  Doğru Cevaplar:\n   "+str(replyList))
  if jsonConfig["question"]["point"]["status"] == False:
    print("Bir Soru Puanı: "+str(questionPoint))
  print("Puanın: "+str(point))
  print("Toplam Soru: "+str(int(totalQuestion)))
  print("  Doğru: "+str(int(trueQuestion)))
  print("  Yanlış: "+str(int(falseQuestion)))
  if jsonConfig["question"]["skip"] == True:
    print("  Boş: "+str(int(emptyQuestion)))
print("\nArin Web | https://arinweb.xyz")
print("Kodlar için: https://arinweb.xyz/github")
print("İyi Günler Dileriz :)")
