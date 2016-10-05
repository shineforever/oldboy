/**
 * Created by shine_forever on 16/10/5.
 */
alert('oldboy');

Foo('Python hah~~~')

function Foo(name){
        console.log(name);
        }

//自执行函数
/*(function(){
    console.log('自执行函数demo')
})()
*/

//传参数给自执行函数
/*
(function(name_test){
    console.log(name_test)
})('传参数给自执行函数'
)
*/

//轮询一个数组(python中叫列表)
/*
array = [1,4,5,77,88,99]
for(var i= 0;i<array.length;i++){
    console.log(array[i])
}
*/

//轮询一个字典;打印出valule的值
dic={'name':'add','age':54,'localtion':'wuhan'}
for(var item in dic){
    console.log(dic[item])   //打印value
    console.log(item)  //打印key
}