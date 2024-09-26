// 1. ajax를 데이터 가져오기

let global_studentId = "";
let studentCount = 0;
let sum = 0;
let avg = 0;
let temp = 0;
let editStudent = [];

// --------------------------------- jquery 시작 -----------------------------------------
$(function(){

  // --------------------------------- ajax 시작 -----------------------------------------
  $.ajax({
    url: "js/stuData.json",
    type: "get",
    data: "",
    dataType: "json",

    // ajax 성공
    success: function (data) {
      let firstData = "";

      // forloop 1회 -> 한 행 완성 | firstData에 html 계속 추가
      for (const item of data) {
      studentCount++;
      sum = item.kor + item.eng + item.math;
      avg = Math.round(sum / 3);
        firstData += `
      <tr id="${item.no}">
        <td>${item.no}</td>
        <td>${item.name}</td>
        <td>${item.kor}</td>
        <td>${item.eng}</td>
        <td>${item.math}</td>
        <td>${sum}</td>
        <td>${avg}</td>
        <td><button class="updateBtn">수정</button><button class="delBtn">삭제</button></td>
      </tr>
      `
      }

      // 데이터를 테이블에 입력
      $("tbody").html(firstData);
    },

    // ajax 실패
    error: function () {
      alert("ajax error");
    }
  })
  // --------------------------------- ajax 끝 -----------------------------------------


  // 삭제 버튼 이벤트
  $(document).on("click", ".delBtn", function(){
    // 삭제할 학생 번호 가져오기
    global_studentId = $(this).closest("tr").attr("id");
    if(confirm("삭제하시겠습니까?")){
      $("#"+global_studentId).remove();
    }
  }) // 삭제 버튼 이벤트 끝


  // 초기 데이터 입력 이벤트
  $(document).on("click", ".createBtn", function(){
    studentCount++; // 학생 번호 증가
    // 사용자의 입력을 배열로 저장
    let addData = "";
    let userInput = [
      studentCount, // 학생 번호
      $("#name").val(), // 사용자가 입력한 이름칸의 value를 구함
      parseInt($("#kor").val()), // 사용자가 입력한 국어점수칸의 value를 구함
      parseInt($("#eng").val()), // 사용자가 입력한 영어점수칸의 value를 구함
      parseInt($("#math").val()), // 사용자가 입력한 수학점수칸의 value를 구함
    ]

    if (userInput[1].length < 1){
      alert("이름을 입력해주세요.");
      return false;
    }

    if (isNaN(userInput[2]) || isNaN(userInput[3]) || isNaN(userInput[4])){
      alert("점수를 제대로 입력해주세요.");
      return false;
    }

    sum = userInput[2] + userInput[3] + userInput[4]; 
    avg = Math.round(sum / 3);

    addData +=
     `
      <tr id="${studentCount}">
        <td>${studentCount}</td>
        <td>${userInput[1]}</td>
        <td>${userInput[2]}</td>
        <td>${userInput[3]}</td>
        <td>${userInput[4]}</td>
        <td>${sum}</td>
        <td>${avg}</td>
        <td><button class="updateBtn">수정</button><button class="delBtn">삭제</button></td>
      </tr>
    `

    $("#tbody").prepend(addData);
    $("#name,#kor,#eng,#math").val("");
    

  }) // 초기 데이터 입력 이벤트 끝


  // 수정 버튼 이벤트 시작
  $(document).on("click", ".updateBtn", function(){
    if (temp % 2 == 1){
      alert("다른 데이터를 수정 중입니다.")
      return false;
    }
    let row = $(this).closest("tr");
    $(".createBtn").hide();
    $(".updateCompleteBtn, .updateCancelBtn").show();
    
    // 행에서 이름, 국어, 영어, 수학 데이터를 가져옴
    editStudent = [
      row.find("td:nth-child(1)").text(),
      row.find("td:nth-child(2)").text(),
      row.find("td:nth-child(3)").text(),
      row.find("td:nth-child(4)").text(),
      row.find("td:nth-child(5)").text(),
    ]

    console.log(editStudent[0]);

    // 행에서 가져온 데이터를 유저 입력창에 넣음
    $("#name").val(editStudent[1]);
    $("#kor").val(editStudent[2]);
    $("#eng").val(editStudent[3]);
    $("#math").val(editStudent[4]);

    temp++;
  }) // 수정 버튼 이벤트 끝


  // 수정완료 버튼 이벤트
  $(document).on("click", ".updateCompleteBtn", function(){
    let updateData = "";
    sum = parseInt($("#kor").val()) + parseInt($("#eng").val()) + parseInt($("#math").val());
    avg = Math.round(sum / 3); 
    updateData = `
        <td>${studentCount}</td>
        <td>${$("#name").val()}</td>
        <td>${$("#kor").val()}</td>
        <td>${$("#eng").val()}</td>
        <td>${$("#math").val()}</td>
        <td>${sum}</td>
        <td>${avg}</td>
        <td><button class="updateBtn">수정</button><button class="delBtn">삭제</button></td>
    `
    // $("").closest("tr").html(updateData);
    temp++;
  })




})

// --------------------------------- jquery 끝 -----------------------------------------


// TODO
// 수정 완료 버튼 눌렀을 때 temp++ 추가해야함.