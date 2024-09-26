$(function () {
  // 검색 버튼 클릭
  $("#searchBtn").click(function () {
    alert("검색버튼 클릭");

    // API URL
    let surl = "https://apis.data.go.kr/B551011/PhotoGalleryService1/gallerySearchList1?serviceKey=Us3G5PgBx5%2FGD%2Fnp%2BsSI%2Bz4jeisOBf%2FQ8m7ES0nYOsmY%2BTtiHqFm016qdg5bdr78WGJj1F1vd82dB8aCxbsjEQ%3D%3D&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json&keyword=";

    // 검색어 가져오기
    let searchWord = $("#search_txt").val();
    surl += searchWord;

    // AJAX 요청
    $.ajax({
      url: surl,
      type: "get",
      dataType: "json",
      success: function (data) {
        alert("성공");
        console.log(data);

        // API 응답에서 갤러리 아이템 정보 추출
        let g_item = data.response.body.items.item;

        // 테이블 데이터 생성
        let h_data = "";
        for (const item of g_item) {
          h_data += `
                <tr>
                <td>${item.galContentId}</td>
                <td>${item.galTitle}</td>
                <td>${item.galPhotographer}</td>
                <td>${item.galModifiedtime}</td>
                <td><img src='${item.galWebImageUrl}' width='100'></td>
                </tr>
                `;
        }

        // 생성된 HTML을 테이블 바디에 추가
        $("#tbody").html(h_data);
      },
      error: function () {
        alert("실패");
      }
    });

  });
});
