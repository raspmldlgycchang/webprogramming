var express = require('express')
var path= require('path');
var bodyParser = require('body-parser');
var parse = require('url-parse');
var fs = require('fs')
/*파이썬 파일을 자바스크립트내에서 작성하고 실행하기*/
const {PythonShell} = require('python-shell');
const { type } = require('os');
let options={
    mode: "text",
    pythonPath: "C:\\<my_pythonPath>\\python.exe",
    scriptPath: "./public/python/",//파이썬 파일을 모아놓은 폴더
    args:["value1", "value2", "value3"],
    //args: [user_data.title, user_data.content, json_data, user_data.from_email, user_data.pw],
};
PythonShell.run("ggsing.py", options, function(err, data){
    if(err) throw err;
    console.log(data);
    //console.log('Success!');
});

var app = express();
app.locals.pretty=true;
app.use(bodyParser.urlencoded({extended:false}));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');
app.use(express.static(path.join(__dirname, './public')));
const createCsvWriter = require('csv-writer').createObjectCsvWriter;
const csvWriter = createCsvWriter({
    path:'./public/csvs/1.csv',
    header:[
        {id:'temperature', title:'TEMPERAUTRE'},
        {id:'humidity', title:'HUMIDITY'},
    ],
});
//commit:210422_커밋6이후 상황(노란펭수 5-3) ..낸제작성
const txtfilePath = './public/txt/makeCsv.txt';
var arrays = fs.readFileSync(txtfilePath).toString().split("\n");

//console.log("type(arrays[i])=>{"+typeof arrays[0]+"}");
/*커밋 8 : (17)복사본의 변경사항으로 적어놓은 커밋을 여기에 주석으로 달거나 보고서에 쓰기*/
//개행문자제거:http://bamtol.net/v5/bbs/board.php?bo_table=pp_js&wr_id=126
//https://stackoverflow.com/questions/14289035/how-do-i-replace-line-breaks
var arrays_tmp;
for(var i in arrays){
    arrays_tmp = arrays[i].replace(/\r/gm,"");
    arrays[i] = arrays_tmp;
}
/*위의 4줄(주석처리제외)만 외부 검색을 통해 그대로 입력한 부분*/
list_2_csv = []
for(var i=0;i<arrays.length;i+=2){
    var list_tmp = {
        temperature: arrays[i],humidity: arrays[i+1]
    };
    list_2_csv.push(list_tmp)
}
console.log(list_2_csv);

/* const records=[
    {placename: 'pohang', waitpeople:1},
    {placename: 'Daegu', waitpeople:2},
]; */
/* csvWriter.writeRecords(records)
    .then(()=>{
        console.log('..Done');
    }); */
csvWriter.writeRecords(list_2_csv)
    .then(()=>{
        console.log('..Done!');
    });
/* app.get('/index',function(req,res){
    base_url= 'https://www.ggsing.com/product/list.html';
    values={'cate_no':'2112'};
    params= parse(values);
    url=base_url+"?"+params;
    res.render('./index',{addr: url});
}); */
app.post('/', function(req,res){
    /*그파일에서 받는 변수의 이름은name*/
    var buttonid = req.body.cloth;
    res.render('./<버튼 몇번 눌렀는지 받아줄 파일>', {name:buttonid})
});
app.get('/test', function(req,res){
    res.render('./test.jade');
});
app.post('/index', function(req,res){
    var name=req.body.id;
    res.render('./index', {addr:name});
});
app.listen(3000, function(req,res){
    console.log('Connected to 3000 port!');
});