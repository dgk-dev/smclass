//제이쿼리 시작
let num = 0;
let num2 = 0;
$(function(){

  
  // 우측이동 버튼 이벤트
  $("#right").click(function(){
    $("#box").stop();
    num += 200;
    num2 += 720;
    $("#box").animate({
      left:num,"rotate":num2+"deg"
    },1000)
  })


  // 좌측이동 버튼 이벤트
  $("#left").click(function(){
    $("#box").stop();
    num -= 200;
    num2 -= 720;
    $("#box").animate({
      left:num,"rotate":num2+"deg"
    },1000)

    
  })

}) //제이쿼리 끝