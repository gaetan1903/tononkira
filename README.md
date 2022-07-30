# tononkira

Unofficial Module and CLI tool to get Malagasy song lyrics from https://tononkira.serasera.org

## INSTALLATION

```s
pip install tononkira
```

## USAGE

### MODULE 

```python
from tononkira import Tononkira 

tononkira = Tononkira()

print(tononkira.get("Ampy anahy")) 
``` 

### CLI TOOL

![image](https://user-images.githubusercontent.com/43904633/181905251-f08f27de-7032-4ec6-9b7a-55495b69fd06.png)


## ADVANCE USAGE 

```python
from tononkira import Tononkira 

tononkira = Tononkira()

res = tononkira.search("Ambondrona") 
print(res[:2])
``` 

> OUTPUT 

```python
[
{'title': 'Ajanony any', 'artist': 'AmbondronA', 'url': 'https://tononkira.serasera.org/hira/ambondrona/ajanony-any-1'},
{'title': 'ALEO ALOHA', 'artist': 'AmbondronA', 'url': 'https://tononkira.serasera.org/hira/ambondrona/aleo-aloha'}
]
```
_________________________________________

```python
from tononkira import Tononkira 

tononkira = Tononkira()

res = tononkira.fetch("https://tononkira.serasera.org/hira/ambondrona/aleo-aloha") 
print(res)
```` 
> OUTPUT 

```

ALEO ALOHA (Ambondrona)
----------------------

toa ts aritro iany
ny iandry anao
niezaka iany aho fa toa
...

```
