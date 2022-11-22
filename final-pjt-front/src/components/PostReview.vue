<template>
    <div class='reviewbody'>
			<div id="box" class='postfont animate__animated animate__fadeIn animate-delay-2s'>
				<img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="" style='height: 500px; margin-left:15%; border-radius: 0.5cm;'>
				<h1 class="heading" style='font-weight:600;'>{{movie.title}}</h1>
				<div class="data">
					<span class="average">평점 {{movie.vote_average}}</span>
				</div>
				<p class="texts">
					{{movie.overview}}
				</p>
				<div style='text-align: center;'>
					<button @click='showModal' class='jua btn-open-popup' style='font-size:15px; margin-top: -30px; width:80px; border-radius:0.3cm;' 
					data-bs-toggle="modal" data-bs-target="#staticBackdrop">리뷰쓰기
					</button>
				</div>
			</div>
      <!-- 모달 들어갈 내용 -->
      <div class='reviewModal jua' v-if='is_show' style='text-align:center; margin-top:10px; '>
            <div class="ReviewInlineblock" style= 'width: 400px;'>
                <input style=' width:400px;' type="text" id='username'  placeholder="댓글 제목" class='id'>
            </div>
            <div class="ReviewInlineblock">
                <input style=' width:400px;' type="text" id='content'  placeholder="댓글 내용" class='content'>      
            </div>
            <div class="ReviewInlineblock">
              <input  type="number" value="rating"  placeholder="평점">
            </div>
              <button style='font-size:15px; margin-left:30px; width:60px; height:40px; bottom:100px;' @click='postReview'>작성</button>
      </div>
    </div>

</template>

<script>
// const IMG_URL = "https://image.tmdb.org/t/p/w500"

export default {
    name: 'PostReview',
    data() {
        return {
            // movie:null,
            title:null,
            content:null,
            rating:null,
						is_show : false,
					
        }
    },
    computed: {
        movie() {
            return this.$store.state.movie_detail
        }
    },
    methods: {
        postReview() {
            if ( this.title && this.content && this.rating ) {
                const payload = {
                    title: this.title,
                    content: this.content,
                    rating: this.rating,
                    movie_id: this.movie.id,
                }
                this.$store.dispatch('postReview', payload)
            }
            else { alert('빈 칸을 채워주세요.') }
        },
				showModal(){
					console.log('show')
					this.is_show = true
				}
    },
    created() {
        const payload = {
            backTo : 'PostReview',
            movie_id: this.$route.params.movie_id,
        }
        this.$store.dispatch('getMovieDetail', payload)
    }
		
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang&display=swap');

.postfont{
	font-family: 'Gowun Batang', serif;
	font-size: 20px;
	font-weight: 600;
}

#box  {
  width: 500px;
  border-radius: 8px;
  overflow: hidden;
  margin: 50px auto;
  transition: all 0.3s cubic-bezier(0.42, 0.0, 0.58, 1.0);
	border: 5px double gray;
}

#box:hover {
  box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
  transform: translateY(-10px);
}

#box * {
  padding: 10px;
}

#box .img {
  display: block;
  object-fit: cover;
  padding: 0;
	
	
}
#box .heading {
  font-size: 28px;
	margin-top:10px;
	margin-bottom: 10px;
}

#box .data {
  display: flex;
  flex-direction: column;
  font-size: 12px;
  color: #666;
	
}

#box .data span {
  padding: 0;
	margin-top:2px;

}

#box .data .average {
  margin-bottom: 2px;
}

#box .data .average {
  font-size: 16px;
  color: #000;
  font-weight: 600;
}

#box .texts {
  font-size: 14px;
  line-height: 18px;
	margin-bottom: 5px;
}
.reviewModal{
  position: relative;
  width: 490px;
  left: 700px;
  
}
.ReviewInlineblock {
    display: flex;
    width: 200px;
    margin: 10px;
    font-size: 17px;
    
}
.reviewModal button{
  position: relative;
  top:-75px;
  left: 220px;
}
input #content{

}
</style>