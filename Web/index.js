const express = require('express');
const fs = require("fs");

const app = express();

app.use('/public', express.static('public'));

app.listen(8080, '0.0.0.0');

console.log('실행: http://localhost:8080/');

app.get('/', function (req, res) {
    res.sendFile(__dirname + '/public/main.html')
});




// 마커 정보 표시 url https://apis.map.kakao.com/web/sample/drawShape/