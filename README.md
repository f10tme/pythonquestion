# Python Question

Install
```
git clone https://github.com/arinweb/pythonquestion
cd pythonquestion
python index.py
```

## Config ayarları

| Name| Value |
| ----| ----- |
| jsonFileName | test.json |
| **question** | object |
| &nbsp;&nbsp;*name* | *soru* |
| &nbsp;&nbsp;*reply* | *cevap* |
| &nbsp;&nbsp;*option* | *["a","b","c","d","e"]* |
| &nbsp;&nbsp;*skip* | true |
| &nbsp;&nbsp;*totalpoint* | 100 |
| &nbsp;&nbsp;***point*** | object |
| &nbsp;&nbsp;&nbsp;&nbsp;*status* | *false* |
| &nbsp;&nbsp;&nbsp;&nbsp;*name* | *puan* |

## Table Output Json
```json
{
  "jsonFileName": "test.json",
  "question":{
    "name":"soru",
    "reply":"cevap",
    "option":["a","b","c","d","e"],
    "skip":true,
    "totalPoint": 100,
    "point":{
      "status":false,
      "name":"puan"
    }
  }
}
```

## Question Json Format
```json showLineNumbers
[
   {
    "soru":"Soru İçeriği",
    "cevap":"a",
    "a":"A Şıkkı",
    "b":"B Şıkkı",
    "c":"C Şıkkı",
    "d":"D Şıkkı",
    "e":"E Şıkkı",
    "puan":10
  }
]
```

### *jsonFileName*
Json dosyasının konumunu belirtmek için kullanılır.

### *question* **name**
Soru içerik değişken adı **soru**

### *question* **reply**
Doğru Yanıt değişken adı **cevap**

### *question* **option**
Cevap Şıkları **["a","b","c","d","e"]**
<br>ÖR: *["x","y","z"]*

### *question* **skip**
Soruyu atlama izni değer **true** ise soru atlanabilir değer **false** ise soru atlanamaz mutlaka cevaplanması gerekir.

### *question* **totalPoint**
Toplam puan **100** toplam puanı soru adedine bölünür ve kazanılan puan belirlenir.
<br>ÖR: Toplam Puan 100,Soru adedimizde 5 / 100 ÷ 5 = 20 Yani bir soru 20 puana eşit olmaktadır.

### *question* *point* **status**
Özel puan ayarlayabilirsiniz her soru için ayrı ayrı, değer **true** ise *question* *point* **name** değişkeninde belirttiğiniz değerdeki puanlar baz alınır **false** ise totalPoint işlemi uygulanır.

### *question* *point* **name**
Özel puan değişken adı **puan**
