"use strict"
//"use strict"と書くとstrictモードが有効になり、let a;みたいに変数宣言を行なっていない変数に値を代入するなどがエラーとして表示される

//mozillaのjavascript, html, cssのチュートリアルが有能。特に、javascriptならではの機能を学ぶなら
//https://developer.mozilla.org/ja/docs/Learn/JavaScript/Client-side_web_APIs/Introduction
//を見るべき。後、「現代のJavascriptチュートリアル」という以下のサイトが有能？

//javascriptにおける型はプリミティブ型とオブジェクト型に分けることができて、プリミティブ型とは
//数値(intとfloatの区別はない)、長整数(大きな整数を扱えるだけ、ほぼ数値と同じ使い方、多分あまり使わない)、文字列(pythonでいうstr,"hello"など)、論理値(trueとfalse)、undefined、null(前者はlet a;などと変数宣言はしたがまだ値を代入していない変数の型、後者はlet a=null;などと明示的に変数に代入でき、特定の値を示しているわけではないことを表すために使うやつ。なぜかtypeof(null)はobjectと表示されるが、深い意味はないらしい)、シンボル(インスタンス化するたびに作成済みのSymbolと異なるユニークな値を示す型。let a1=Symbol(); let a2=Symbol();などと書くと、a1===a2がfalseになる)
//の7つ。
//また、オブジェクト型とはプリミティブ型ではないもの全てで、Object、Array、Function、Dateなどがある。これらは全てobjectクラスのサブクラスである。プリミティブ型は値を一つ(数値、文字列など)しか持たないがオブジェクト型はプロパティというkey:valueという形の内容を複数持てる。

//型はtypeof演算子で取得できる(例：typeof(51)はNumber)

//jacascriptにおけるオブジェクトとは、プロパティ名(pythonでいうインスタンス変数、キーともいう)と値(プリミティブ型でもオブジェクト型でも良い)のペアが定義されたもので、jsonで書かれる。例としては、

// let user = {
//     name:"山田太郎",
//     age:27,
//     hobby:["読書","運動"],
//     getAge:function(){
//         return this.age;
//         }
// }

//みたいにpythonのdictに近い書き方で書く(pythonでいうメソッドなどは、値としてFunction型を持っていることに対応。)。そして、値の参照の仕方はpythonと同じくuser.nameみたいに書くこともできるし、pythonのdictみたいにuser["name"]ともかける。また、user.name="佐藤"みたいに別の値を代入して変更できる。また、strict modeであってもuser.address="東京"みたいに新しいプロパティに値を入れる形で新しいプロパティを作れる。また、プロパティの削除にはdelete演算子をつかって
//delete user.addressまたは
//delete user["address"]
//みたいに書く。

//また、pythonでいうhasattrに対応するのがObjectオブジェクトの.hasOwnPropertyメソッドで、上の例だとuser.hasOwnProperty("name")がtrueになる

//また、Object.keys()、Object.values()などのObjectオブジェクトのメソッドを使うことで例えばObject.keys(オブジェクト)でオブジェクトのプロパティ名の一覧を取得する(返り値はList)。また、Object.entries()でkeyとvalueが同時にListで取得できる。

//↑実際Object.entries(Object)でentriesというkeyにfunctionが入っていた

//上の例はuserというオブジェクトをオブジェクトリテラルという書き方を使って定義した例だが、Objectオブジェクトのコンストラクタを使ってオブジェクトを作ることもできる。

//↑javascriptでは、ユーザー定義、組み込みのオブジェクトのインスタンス作成にnew演算子を使う。例としては、
//let obj = new Object();
//と書くと、objとして何も値の入っていない{}というオブジェクトができる。

//pythonのclass tes;みたいな書き方と似たようなクラスの定義方法もある(これで直接Objectをkeyとvalueを頑張って入れていかないでも作れるようになる)。書き方は、
// function Person(name,age){
//     this.name=name;
//     this.age=age;
//     this.setName=function(name){this.name=name;}
// }
//みたいに、「コンストラクタ」というfunction型を定義している(pythonでいう__init__関数)。pythonでいうselfの代わりにthisという文字を使っている。これで、
// let person1=new Person("taro", 22);みたいに書くとperson1というPerson型のインスタンスができる。メソッドに関しては、上の例のようにfunction型をコンストラクタ内で定義する方法もあるが、インスタンス生成のたびにメソッドがコピーされないで済むprototypeプロパティを使った方法というのもあるらしい

//↑ただ、新しいJavaScriptではpythonに近いclassの定義の仕方が可能になって、
//class Person{
//     constructor(name,age){this.name=name;this.age=age;}
// returnName(){return this.name;}
// }
//みたいなconstructorという特別な名前のメソッドを定義してクラスを定義できる。

//よく使うwebサイトのポップアップを簡単に扱える関数として、prompt,alert,confirmというのがある。例えば以下の例：

// var res = false;
// var mes;
// while (res===false) {
//     mes = prompt("名前を入力してください", "山田太郎");
//     res = confirm("あなたは"+mes+"さんですね?");
// }
// alert("よろしく"+mes+"さん!");

//では、まずpromptによって(chromeだとすると)、「名前を入力してください」というメッセージとその下に名前入力欄(デフォルトで「山田太郎」と書いている)があり、その下に「キャンセル」と「OK」のボタンがあるポップアップが出てくる。ここで例えば「unko」と打ち込んでOKを押すと、mesという変数に"unko"という文字列が代入され、次の行のconfirmに移る。confirmによって、「あなたはunkoさんですね?」というメッセージの下に「キャンセル」と「OK」のボタンが表示されたポップアップが出てきて、OKを押すとwhile文を抜けてalertが実行され「よろしくunkoさん!」という文章が表示され、下に「OK」ボタンがあるポップアップが出てくる。confirmの返り値は、「キャンセル」を押されたらfalse、「OK」を押されたらtrueであるので、「あなたはunkoさんですね?」でキャンセルを押すともう一度名前入力のポップアップに戻る。


let elem = document.currentScript;
elem.insertAdjacentHTML("beforebegin", typeof(elem));

/* コメントはこんな感じで入れる */

//electronというクロスプラットフォームデスクトップアプリエンジン(?)を使うと、node.js(javascriptの開発環境)+HTML+CSSというweb系の技術だけでアプリケーションを作成できるらしい(しかしpythonでDjangoでアプリを作る方が有益)。
//↑このnode.jsというのはjavascriptをバックエンドでも使えるような環境ならしいが、そんなにバックエンドの言語としてJavaScriptが強いわけではないのでそんなに優先順位は高くなさそう。フロントエンドとして使えたら多分十分
//JavaScriptのElementオブジェクトのinsertAdjacentHTMLメソッド(typeofメソッドで取得できる)をつかってHTMLに要素を挿入できる。
//javascriptでは変数名の宣言にvar, let, constなどのキーワードを使う(例:let sum=10)
//constは再代入ができない(例：const c=0;からのc=1;はエラー)が、letとvarはできる
//constとletは再宣言ができない（例：let a=0;からのlet a=1;はエラー）が、varはできる
//再宣言は同じ文字が既に使われていても気づかない危険性があるのでやらない方がいい(varは使わない)
//↑また、可読性の面から可能な部分はconstで定義するべき