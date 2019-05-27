# meta 태그 속성 알아보기

## meta 태그의 용도
<meta> 태그는 metadata 의 약자로, 다른데이터를 설명해 주는 데이터를 의미한다.

## 속성 charSet
html 파일의 인코딩을 알려준다. 인코딩을 명확하게 명시하지 않을 경우, 웹 브라우저 설정이 자동으로 인코딩을 추정해서 처리를 하는데 정확할 때도 있고, 그렇지 못하는 경우도 있다.
따라서 해당 속성은 파일을 인코딩할때 해당 문자코드로 지정하라는 정보를 전달한다.

> 인코딩 : 웹브라우저나 컴퓨터는 HTML 파일을 웹브라우저에서 표시될 수 있도록 변환 하는 처리작업을 한다.

> HTML5 문서에서는 대부분의  charset 속성의 값을 utf-8 로 지정한다.

## meta viewport 태그

애플이 아이폰, 아이패드 등 자사의 모바일 브라우저 뷰포트 크기 조절을 위해 만들어진 메타 태그로 W3C 에는 없는 표준이 아닌 태그 이지만, iOS 장치가 많이 쓰이므로 사실상 표준인 태그 이다. 다른 브라우저에서도 이 태그를 채택하고 있다.

일반적인 태그
```html
<meta name="viewport" content="width=device-width, user-scalable=no">
```

width 속성은 뷰포트의 크기를 조정한다. 특정한 숫자를 사용해 width=600라고 할 수도 있고 device-width와 같은 특정한 값을 사용할 수도 있는데, device-width는 100% 스케일에서 CSS 픽셀들로 계산된 화면의 폭을 의미한다. (뷰포트의 높이에 따라 크기와 위치가 변하는 요소들로 이루어진 페이지의 경우 상응하는 height와 device-height 값들이 유용하게 사용될 수 있다.)

initial-scale 속성은 페이지가 처음 로드될 때 줌 레벨을 조정한다. maximum-scale, minimum-scale, 그리고 user-scalable 속성들은 사용자가 얼마나 페이지를 줌-인, 줌-아우트 할 수 있는지를 조정한다.

## meta description 태그
```html
<meta name="description" content="메타 태그 테스트중 입니다.">
```
페이지에 관한 짧은 설명을 제공하는 태그로, 검색결과에 나타나는 스니펫의 일부로도 사용할 수 있다.

## meta keywords 태그
```html
<meta name="keywords" content="공부중, 메타 태그">
```
페이지가 검색엔진에 제공하는 키워드를 나타낸다.

## meta open graph 태그

링크의 미리뵉 제목, 설명, 이미지를 정한다.

<table style="width: 100%;">
    <tbody>
        <tr>
            <td style="width: 70%;">
                <b>og:url</b> : 페이지의 표준 URL (데스크탑 URL)</br>
                <b>og:title</b> : 콘텐츠 제목</br>
                <b>og:description</b> : 콘텐츠 설명. 미리보기에서 제목 아래에 표시</br>
                <b>og:site_name</b> : 웹 사이트의 이름 (주소 아님)</br>
                <b>og:image</b> : 콘텐츠를 공유 시 표시되는 이미지의 URL</br>
                <b>og:type</b> : 뉴스피드에 콘텐츠가 표시되는 방식에 영향을 준다. (기본값은 website) 각 URL은 단일 개체여야 하므로, 여러 og:type 값을 사용할 수 없다.</br>
                <b>og:locale</b> : 리소스의 언어이다. (기본값은 en_US) 다른 언어로 번역 기능을 사용할 수 있으면 og:locale:alternate도 사용할 수 있다.</br>
                <b>fb:app_id</b> : 페이스북 인사이트를 사용하기 위한 앱 아이디</br>
                <b>fb:admins</b> : 웹 사이트용 도메인 인사이트를 사용하기 위한 아이디
            </td>
            <td style="width: 30%;"><img src="./images/openGraphExample.png" style="width:100%"/></td>
        </tr>
    </tbody>
</table>