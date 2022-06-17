### 

## preparation



#### 폴더명 : final-back



**가상환경 만들기**

- venv라는 이름의 가상환경 생성

```bash
$ python -m venv venv
```



**만든 가상환경 activate 하기** 

1. `crtl + shift + p` 의 python select interpreter를 내가 새롭게 만들어준 python 3.9.9 venv 클릭 
2. 기존 켜져있는  bash 창 종료 



또는 자동완성으로 이용

```bash
$ source venv/Scripts/activate
(venv) 
```

 

**pip 리스트 확인** 

- 아래와 같이 떴다는 것은 가상환경이 잘 생성되었다는 뜻

```bash
$ pip list

Package    Version
---------- -------
pip        21.2.4
setuptools 58.1.0
```



**requirements 대로** **설치**

```bash
$ pip install -r requirments.txt
```



**migrate**

```bash
$ python manage.py migrate
```



**서버 켜기**

```bash
$ python manage.py runserver
```



----------

--------



#### 폴더명 : final-front

**프로젝트 디렉토리 이동** 

```bash
$ cd final
```



**npm install**

```bash
$npm install
```



**run serve**

```bash
$npm run serve
```

