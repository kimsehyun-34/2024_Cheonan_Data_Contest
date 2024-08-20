const express = require('express');

const cookieParser = require('cookie-parser');
const spawn = require('child_process').spawn;

const app = express();
app.use(express.urlencoded({ extended: true }));

app.use('/public', express.static('public'));

app.listen(8080, '0.0.0.0');

console.log('실행: http://localhost:8080/');

app.use(cookieParser());

const nunjucks = require('nunjucks')
app.set('views engine', 'html')
nunjucks.configure('public',{
    express:app,
})

app.get('/test1', function (req, res) {
    res.sendFile(__dirname + '/public/main_one.html')
});
app.get('/test2', function (req, res) {
    res.sendFile(__dirname + '/public/main_tw.html')
});
app.get('/test3', function (req, res) {
    res.sendFile(__dirname + '/public/main_tre.html')
});
app.get('/test4', function (req, res) {
    res.sendFile(__dirname + '/public/main_fr.html')
});

app.get('/', function (req, res) {
    res.sendFile(__dirname + '/public/main_one.html')
});

app.get('/map', function (req, res) {
    res.sendFile(__dirname + '/public/map.html')
});


// app.post('/', function(req,res){
//     var Cat = req.body.Cat;
//     console.log(Cat)
//     res.sendFile(__dirname + '/public/main.html')
// })

app.post('/tw', function(req, res) {
    var sex = req.body.se;
    var age = req.body.age;
    console.log(sex);
    console.log(age);

    const result = spawn('python', ['./python/chu.py', sex, age]);

    result.stdout.on('data', (data) => {
        const output = data.toString();
        const cleanedOutput = output.replace(/[\[\]']/g, '').split(', ');

        const userInfo = {
            age: age,
            sex: sex,
            chu: cleanedOutput,
            bakery: ['0'],
            sook: ['0'],
            food: ['0']
        };

        res.cookie('user_info', JSON.stringify(userInfo), { maxAge: 900000, httpOnly: true });

        result.on('close', (code) => {
            res.render('main_tw.html', {
                content: cleanedOutput,
                content0: sex,
                content1: age
            });
        });
    });

    result.stderr.on('data', (data) => {
        console.error(`Error: ${data}`);
    });
});

app.post('/tre', function(req, res) {
    let userInfo = req.cookies['user_info'];
    // 기존 쿠키의 JSON 문자열을 객체로 변환
    if (userInfo) {
        userInfo = JSON.parse(userInfo);
    } else {
        userInfo = {}; // 쿠키가 없으면 빈 객체로 시작
    }

    var cat = req.body.Cat;
    console.log(cat);

    var cat0=cat[0]
    var cat1=cat[1]
    var cat2=cat[2]

    const num_cat0 = parseInt(cat0, 10);
    const num_cat1 = parseInt(cat1, 10);
    const num_cat2 = parseInt(cat2, 10);

    const chu = userInfo.chu;

    var chuchu0=chu[num_cat0]
    var chuchu1=chu[num_cat1]
    var chuchu2=chu[num_cat2]

    var list_chu = [chuchu0,chuchu1,chuchu2]

    console.log(list_chu)


    userInfo.chu = list_chu; // 예: favoriteColor 속성 추가

    // 객체를 다시 JSON 문자열로 변환하여 쿠키에 저장
    res.cookie('user_info', JSON.stringify(userInfo), { maxAge: 900000, httpOnly: true });


    res.render('main_tre.html', {
        content: cat,
    });
});

app.post('/fr', function(req, res) {
    let userInfo = req.cookies['user_info'];
    // 기존 쿠키의 JSON 문자열을 객체로 변환
    if (userInfo) {
        userInfo = JSON.parse(userInfo);
    } else {
        userInfo = {}; // 쿠키가 없으면 빈 객체로 시작
    }

    var cat = req.body.Cat;
    console.log(cat);

    const catString = JSON.stringify(cat);

    const result = spawn('python', ['./python/br.py', catString]);

    result.stdout.on('data', (data) => {
        const output = data.toString();

        var newoutput=output.replace(/[\d\r\n]/g, '').trim();

        console.log(newoutput)

        res.cookie('user_info', JSON.stringify(userInfo), { maxAge: 900000, httpOnly: true });

        result.on('close', (code) => {
            userInfo.bakery = newoutput;

            res.cookie('user_info', JSON.stringify(userInfo), { maxAge: 900000, httpOnly: true });

            res.render('main_fr.html', {
            });
        });
    });
});

app.post('/fiv', function(req, res) {
    let userInfo = req.cookies['user_info'];

    if (userInfo) {
        userInfo = JSON.parse(userInfo);
    } else {
        userInfo = {};
    }

    var food = req.body.food;
    var num0 = req.body.num0;
    var num1 = req.body.num1;

    console.log(food);
    console.log(num0);
    console.log(num1)

    const result = spawn('python', ['./python/sook.py', num0, num1]);

    result.stdout.on('data', (data) => {
        const output = data.toString();

        console.log(output)

        res.cookie('user_info', JSON.stringify(userInfo), { maxAge: 900000, httpOnly: true });

        result.on('close', (code) => {
            userInfo.sook = output; 



            const result = spawn('python', ['./python/food.py', food]);

            result.stdout.on('data', (data) => {
                const output = data.toString();
        
                console.log(output)
        
                res.cookie('user_info', JSON.stringify(userInfo), { maxAge: 900000, httpOnly: true });
        
                result.on('close', (code) => {
                    userInfo.food = output; 
        
                    res.cookie('user_info', JSON.stringify(userInfo), { maxAge: 900000, httpOnly: true });
        
                    res.render('main_fiv.html', {
                        
                        
                    });
                });
            });
        });
    });
});



app.get('/get-cookie', (req, res) => {
    let userInfo = req.cookies['user_info'];
    if (userInfo) {
        userInfo = JSON.parse(userInfo);
        res.send(`유저 정보: ${JSON.stringify(userInfo)}`);
    } else {
        res.send('존재하지 않음');
    }
});

// 마커 정보 표시 url https://apis.map.kakao.com/web/sample/drawShape/