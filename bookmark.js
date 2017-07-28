var form = document.createElement("form");
form.setAttribute("method", "POST");
form.setAttribute("action","http://127.0.0.1:8000/htmlsave" );
form.setAttribute("accept-charset","UTF-8" );
form.setAttribute("onsubmit","document.charset='UTF-8'" );

joongo_html=document.getElementById('cafe_main').contentWindow.document.getElementById('content-area').outerHTML;
url=document.getElementById('cafe_main').contentWindow.document.getElementById('linkUrl')['href'];

var hiddenField = document.createElement("input");
hiddenField.setAttribute("type", "hidden");
hiddenField.setAttribute("name","url" );
hiddenField.setAttribute("value", url);

var HtmlField = document.createElement("input");
HtmlField.setAttribute("type", "hidden");
HtmlField.setAttribute("name","html" );
HtmlField.setAttribute("value", joongo_html);

form.appendChild(hiddenField);
form.appendChild(HtmlField);
document.body.appendChild(form);
form.submit();
