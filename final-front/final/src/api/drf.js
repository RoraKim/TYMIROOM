const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const ACTORS = 'actors/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // 유저 확인
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username에게 팔로우/취소 요청
    follow: username => HOST + ACCOUNTS + `${username}/` + 'follow/',
    // 나를 팔로우 한 친구 목록
    followers: username => HOST + ACCOUNTS + `${username}/` + 'followers/',
    // 프로필(username) 의 프로필 정보
    profile: username => HOST + ACCOUNTS + 'profile/' + `${username}/`,
    // 프로필 업데이트
    profileUpdate: () => HOST + ACCOUNTS + 'update/' + 'profile/',
    // username의 프로필에 방명록 작성
    guestbook: username => HOST + ACCOUNTS + 'profile/' + `${username}/` + 'guestbook/',
    // username의 프로필에 방명록 작성
    guestbookUpdate: (username, guestbookId) => HOST + ACCOUNTS + 'profile/' + `${username}/` + 'guestbook/' + `${guestbookId}/`,
    // 비밀번호 변경
    passwordChange: () => HOST + ACCOUNTS + 'password/' + 'change/',
    // 유저 검색
    userList: username => HOST + ACCOUNTS + 'users/' + `${username}/`
  },
  movies: {
    // 전체 영화정보 랜덤으로
    movies: () => HOST + 'movies',
    // username이 본 영화
    seenMovies: username => HOST + MOVIES + username + '/seen/list/',
    // 영화 디테일, 리뷰 작성
    movieDetail: movieId => HOST + MOVIES + `${movieId}/`,
    // 배우 디테일 
    actorDetail: actorId => HOST + MOVIES + ACTORS + `${actorId}/`,
    // 리뷰 삭제, 수정
    reviewUpdate: (movieId, reviewId) => HOST + MOVIES + `${movieId}/` + `${reviewId}/`,
    // 리뷰 좋아요, 취소
    reviewLike: (movieId, reviewId) => HOST + MOVIES + `${movieId}/` + `${reviewId}/` + 'like/',
    // 장르에 따른 영화들
    genreMovies: genreId => HOST + MOVIES + 'genres/' + `${genreId}/`,
    // 배우에 따른 영화들
    actorMovies: actorId => HOST + MOVIES + 'actors/' + `${actorId}/`,
    // 본 영화에 추가, 제거
    seenMovieUpdate: movieId => HOST + MOVIES + `${movieId}/` + 'seen/',
    // 보고싶은 영화에 추가, 제거
    wishMovieUpdate: movieId => HOST + MOVIES + `${movieId}/` + 'wish/',
    // 영화 월드컵 
    moviegames: () => HOST +  MOVIES +'moviegame/',
    // 배우 월드컵
    actorgames: () => HOST +  MOVIES +'actorgame/',
  }
}