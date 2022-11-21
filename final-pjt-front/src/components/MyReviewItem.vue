<template>
  <div>
    {{ myReview }}
    <a href="">
      <div class="board_img">
          <img src="" alt="이미지">
      </div>
    </a>
  </div>
</template>
<!-- { "id": 19,
   "movie": { "id": 365, "like_users": [ { "id": 1, "nickname": "이원일", "profile_image": "/media/default.jpg", "grade": 0, "followings": [] } ],
   "movie_id": 338958, 
   "title": "마법에 걸린 사랑 2", 
   "original_title": "Disenchanted", 
   "overview": "결혼 15년 차가 된 지젤과 로버트. 그러나 지젤은 도시 생활에 점점 염증을 느낀다. 그들은 동화 같은 삶을 찾아 두 딸을 데리고 먼로빌 외곽의 조용한 마을로 이사하기로 하는데, 불행히도 그건 지젤이 바라던 손쉬운 해결책이 아니다. 교외 생활에는 전혀 새로운 규칙이 존재하고, 그곳 여왕벌인 말비나 먼로로 인해 지젤은 그 어느 때보다 이곳이 맞지 않는다는 걸 느낀다. 오래오래 행복한 삶을 찾기가 생각처럼 쉽지 않자 좌절에 빠진 그녀는 안달라시아 마법에 의지하게 되고, 어쩌다 마을 전체가 현실 속 동화로 바뀌게 되면서 가족 미래의 행복이 위기에 빠진다. 이제 지젤은 마법을 빨리 되돌려야 하는 시간과의 사투를 벌이며 자신과 가족의 영원한 행복을 결정하는데...", 
   "poster_path": "/9MSqVj9ulOAK5TqQFjtAMuj2dTk.jpg", 
   "backdrop_path": "/kpUre8wWSXn3D5RhrMttBZa6w1v.jpg", 
   "release_date": "2022-11-18", "popularity": 119.958, 
   "vote_average": 10, "vote_count": 1, "adult": false }, 
   "author": { "id": 1, "username": "lwi995", "email": "lwi995@naver.com", 
   "nickname": "이원일", 
   "profile_image": "/media/default.jpg", 
   "grade": 0, 
   "followings": [], 
   "followers": [ { "id": 2, "nickname": "창조주", "profile_image": "/media/default5.jpg", 
   "grade": 0, "followings": [ 1 ] } ], 
   "cnt_followings": 0, "cnt_followers": 1 }, 
   "like_users": [], 
   "comments": [], 
   "comment_count": 0, 
   "title": "ㄹㅇㄴㄹㅇㄴㄹ", 
   "content": "ㄹㅇㄴㄹㄹ", 
   "rating": 2, 
   "created_at": "2022-11-21T01:33:09.061280Z", 
   "updated_at": "2022-11-21T01:33:09.061280Z" } -->

<script>
export default {
  name: 'MyReviewItem',
  props: {
    myReview: Object,
  },
  data() {
    return {
      poster_image() { return  }
    }

  }
}

</script>

<style>

</style>