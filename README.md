# Guestbook_website

您好，這是我所寫的一個留言板專案

以下是關於此專案的一些介紹 :smile:

## 寫此專案所學習到的事情：

**資料庫整合和存取與練習ORM操作**

* 在models.py中思考並設計出需要的物件
* 整合mysql資料庫，將資料遷移到database中

**練習Django的MTV 網頁架構觀念與實作**

* 利用urls傳回的參數搭配Views，顯示出想要的資料和模板
* 利用MTV達到留言與評論的CRUD

**修改留言與評論和設計表單顯示**

* 思考如何設計Forms，方便使用者對留言與評論予以填寫修改
* 設計Forms與POST搭配使用後，urls的重定向使用

**註冊系統和串接第三方應用程式所提供的API**

* 利用UserCreationForm作出註冊功能並客製化
* 利用Django allauth套件，作出第三方登入驗證功能

## 待加強的部分:

* 在models.py中定義物件，除了ForeignKey外，還有ManyToManyField等其他方式需多加認識，以便往後做使用
* 對於前端 HTML、CSS、JS的知識缺乏，往後會補強這些項目

## 網站首頁畫面:

![image](https://github.com/n55567820/Guestbook_website/blob/main/djangosite/staticfiles/index.png)
