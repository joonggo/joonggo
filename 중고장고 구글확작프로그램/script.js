
chrome.tabs.executeScript({
  code:'var iframe = document.createElement("iframe");var uniqueString = "CHANGE_THIS_TO_SOME_UNIQUE_STRING";document.body.appendChild(iframe);iframe.style.display = "none";iframe.contentWindow.name = uniqueString;var form = document.createElement("form");form.target = uniqueString;form.action = "http://127.0.0.1:8000/htmlsave";form.method = "POST";form.setAttribute("accept-charset","UTF-8" );form.setAttribute("onsubmit","document.charset=\'UTF-8\'" );joongo_html=document.getElementById(\'cafe_main\').contentWindow.document.getElementById(\'content-area\').outerHTML;url=document.getElementById(\'cafe_main\').contentWindow.document.getElementById(\'linkUrl\')[\'href\'];var hiddenField = document.createElement("input");hiddenField.setAttribute("type", "hidden");hiddenField.setAttribute("name","url" );hiddenField.setAttribute("value", url);var HtmlField = document.createElement("input");HtmlField.setAttribute("type", "hidden");HtmlField.setAttribute("name","html" );HtmlField.setAttribute("value", joongo_html);form.appendChild(hiddenField);form.appendChild(HtmlField);document.body.appendChild(form);form.submit();'
})









// //크롬 스토리지에 저장된 값을 가져오세요.
// chrome.storage.sync.get(function (data) {
//   // #user의 값으로 data의 값을 입력해주세요.
//   document.querySelector('#user').value = data.userWords;

//   //분석해서 그 결과를 #result에 넣어주세요.
//   matching(data.userWords);

// });

// //컨텐츠 페이지의 #user 입력된 값이 변경 되었을 '때'
// document.querySelector('#user').addEventListener('change', function () {
//   //컨텐츠 페이지에 몇개의 단어가 등장하는지 계산해주세요.
//   var user = document.querySelector('#user').value;

//   // 크롬 스토리지에 입력값을 저장한다.
//   chrome.storage.sync.set({
//     userWords: user
//   });

//   //컨텐츠 페이지를 대상으로 코드를 실행해주세요.
//   matching(user);

// });