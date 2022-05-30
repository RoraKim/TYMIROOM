## 0518

### 한 일

- 데이터 받아오기

### 힘든 점

- TMDB에서 배우 데이터를 받아오는 과정에서 받은 데이터를 후처리하여 그 데이터로 또다시 요청을 보내고 받아야 해서 방법을 조금 헤메고 오래 걸림

  

## 0519

### 한 일

- 데이터 받아오기
- 백앤드 모델링 거의 완성

### 힘든 점

- TMDB에서 배우 데이터를 받아오는 과정에서 받은 데이터를 후처리하여 그 데이터로 또다시 요청을 보내고 받아야 해서 방법을 조금 헤메고 오래 걸림

  ```python
  1. OneToOneField 를 사용 : 실패
  2. django-annoying 인스톨 후 AutoOneToOneField : 실패
  3. if not Profile.objects.filter(user_id = user.pk).exists():
          Profile.objects.create(user_id = user.pk)
          뷰에서 없다면 만들어주기 : 성공
  ```

  

## 0520

### 한 일

- 백 앤드 기획부분까지 완료
- 프론트 앤드 목업만 짜놓기

### 힘든 일

- 백앤드 serializer 제작중인데 프로필 페이지 요청시 유저 정보와 프로필 정보가 같이 넘어와야하는데 profile_set = UserProfileSerializer(many=True, read_only=True) 이러면 나와야 할 것 같은데 나오지 않음

  ```python
  AutoOneToOneField 필드로 아직 사용하고 있어서 _set이 먹히지 않은 것
  다시 ForeignKey로 바꾸고 성공
  ```

- 처음 보는 오류(AssertionError)에 애를 먹음

  ```python
  AssertionError: .accepted_renderer not set on Response 오류가 뜰 때
  => @api_view(['GET', 'POST']) 제대로 입력 안함
  ```

  

## 0521

### 한 일

- 프론트 앤드 작업
  - 요청 보내고 받기 테스트
  - accounts 기능
  - 안본 영화 데이터를 받아오고 영화를 클릭하면 영화 디테일 정보를 모달을 통해 받아옴
- 시리얼라이저 조금 수정(사용 할 데이터와 사용하지 않을 데이터를 실제 만들어보기 전에는 잘 모르겠음)

### 힘든 점

- CSS가 내 맘대로 작동하지 않음 화면 크기가 작아 질 때 반응형으로 어떻게 할지 고민해봐야 함
- for문 안에 모달을 넣고 그 안에 컴포넌트를 넣으니 가장 마지막으로 호출된 컴포넌트 정보만 state에 저장이 됨 -> 클릭 할 때 마다 getters 실행
- 컴포넌트 구조가 조오금 이상함,,

## 0522

### 한 일

- 프론트
  - search와 필터링
  - review 작성
  - wish, seen

### 힘든 점

- 괄호 위치 하나로 3시간을 날렸다,,,

## 0523

### 한 일

- 친구 방명록, 친구창, 리뷰별점,

### 힘든 점

- 리뷰를 새로고침을 못함

```python
v-for 돌릴 때 :key 값을 잘못 입력함(id인데 pk로 입력)
```

- 별점이 이상하게 들어감

## 0524

### 한 일

- 친구 파도타기 기능

- 어제 별점이 이상하게 들어가는 오류 해결

  ```python
  v-model을 사용하였는데 가장 처음 모달의 값에만 score가 바뀜 content는 다 바뀌면서,,
  그래서 그냥 클릭 이벤트로 스테이트에 저장해놓고 가져다 쓰는 방식으로 해결
  ```

- 내 정보 관리 수정
  - 데이터 받아오는 값을 바꾸기 위해 모델을 수정함

### 힘든 점

- 홈으로 갈 때 새로고침이 안되서 
  - 모달에서 바로 친구 홈으로가기 안됨
  - 방명록 새로고침이 안됨

```python
a태그로 바꿈
```

## 0526

### 한 일

- 페이지네이션
- 레벨링
- CSS
- 좋아요 기능
- 팔로우 기능

### 힘든 점

- CSS

- 페이지네이션 할 때 조건을 많이 넣다보니 헷갈림

  ```python
  v-model로 연결한 currentPage가 호출한 함수보다 더 느리게 바뀌어서 전 페이지로 이동함
  -> watch 사용하여 변하면 함수 호출
  ```


- 팔로우 기능에서 follow한 유저 정보를 object로 가지고 있어서 계속 사용하던 includes를 사용하지 못함(내가 팔로우한지 안한지 알 수 없음)

  ```python
  return this.followers.followings.some(function (user) {
      return user['id'] === currentUser.pk
  })
  
  콜백함수로 해결
  ```

- 처음 기획과 바뀌는점이 많아서 수정할게 많이 생기고 복잡해진다. 기획을 잘하자
- 조건분기로 페이지들을 만드니까 너무 복잡해짐, 그냥 라우터 링크를 하나 더 파는게 나을 듯

- 이미지 안에 변수를 넣을때 계속 : 만 쓴다(이걸로 되는 것도 있고 안되는 것도 있음.)

  ```python
  :src="require('../assets/movie/'+ pic + '.gif')"
  ```

- 내 영화는 vuex의 profile 에서 가져오는데 내 영화에서 인생 영화를 클릭한다면 profile이 업데이트 되면서 모달창이 사라지는 오류 발생

  ```python
  어쩔 수 없이 홈으로 새로고침하게 만듬
  window.location.href = `http://localhost:8080/home/${currentUser.username}`
  ```

  
