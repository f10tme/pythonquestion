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

