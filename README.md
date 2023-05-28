# 📝 ACMA (Auto Classifying Memo App)

주제별로 자동 분류되는 메모 앱

## 설명

인생 계획부터 이번 주 쇼핑 리스트까지, 정신없이 뒤죽박죽 섞여있는 내 네모 앱이 <br />자동으로 정리되었으면 하는 마음에서 시작한 프로젝트입니다. 
<br />
#### MENU
![menu](./readme/1_menu.png)
메뉴 구성은 위와 같습니다.
<br />
#### CREATE
![create](./readme/2_create.png)
Create를 통해 작성자와 텍스트만 입력하면 메모를 생성할 수 있습니다.
<br />
#### LIST
![list](./readme/3_list.png)
List에 추가될 때는 자동으로 카테고리가 분류되어 들어가는 것을 확인할 수 있습니다. <br />List 내 카테고리 탭을 클릭하면 분류된 주제별로 묶어서 볼 수 있습니다.

## 원리

- 접근 보안을 위해 secret token을 발행하여 식별자로 사용합니다.
- 한글로 된 메모를 영어 NLP 모델에 처리하기 위해 Google Translation API를 활용합니다. 
- HuggingFace에서 제공하는 transformers의 "Zero Shot Classification" pipeline을 활용합니다. 
<br />
주요 모델인 Memo 객체의 변화를 도식화하면 위와 같습니다.
![description](./readme/4_ACMA_%EC%84%A4%EB%AA%85.png)

## 기술스택

![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=bootstrap&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=React&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=FastAPI&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-yellow?style=flat-square)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=MongoDB&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=Docker&logoColor=white)