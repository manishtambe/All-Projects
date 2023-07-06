const express= require('express')
const mongoose= require('mongoose')
const session = require('express-session');
const flash = require('connect-flash')
const bodyParser = require('body-parser')
const { check, validationResult} = require('express-validator')
const { spawn } = require('child_process');

const app=express();
app.set('view engine', 'ejs');

const port=process.env.PORT || 5000;

app.use(express.json());
app.use(express.urlencoded());
app.use(express.static('public'));
app.use(express.urlencoded({extended: true}))
const urlencodedParser = bodyParser.urlencoded({extended: false})


app.use(session({
   secret: 'nodejs',
   cookie: {maxAge:10000},
   saveUninitialized:true,
   resave:true,
}));

app.use(flash());

app.use(function(req, res, next){
    res.locals.message = req.flash();
    next();
});

// app.use(function(req, res, next){
//  res.locals.sucess = req.flash('sucess'),
//  res.locals.err = req.flash('err')
//  next();
// });

app.get('/index.html', (req,res)=>{
    res.sendFile(__dirname+"/public/index.html");
})


mongoose.connect('mongodb://localhost:27017/System',
{
        useNewUrlParser: true,
        useUnifiedTopology: true
}
).then( () => console.log("Connection successfull...."))
.catch((err) => console.log(err));

var db = mongoose.connection;
// const userSchema=new mongoose.Schema({
//         username:String,
//         userphone:String,
//         usernewlogin:String,
//         usernewpassword:String,
//         usernewemail:String
// })

// const User=new mongoose.model("SignUp",userSchema)


app.post('/log',urlencodedParser,[
    check('user_login', 'This username must me 3+ characters long !')
        .exists()
        .isLength({ min: 3}),
    
    check('user_password', 'Invalid Password !')
        .matches(/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8,}$/, "i")
],async (req, res)=>{

    const errors = validationResult(req)
    if(!errors.isEmpty()){
        //return res.status(422).jsonp(errors.array())
        const alert = errors.array()
        console.log(alert)
        res.render('index', {
            alert
        })
    }
    else{
        global.userlogin = req.body.user_login;
        global.userpassword = req.body.user_password;

        var data = {
            "userlogin": global.userlogin,
            "userpassword": global.userpassword,
        }

        const user = await db.collection('SignUp').findOne({usernewlogin:req.body.user_login});
        if(user != null)
        {
            if(global.userpassword === user.usernewpassword)
            {
                //req.flash('success', 'Login Successful !');
                res.redirect('/dashboard.html')
            }
            else
            {
                req.flash('success', 'Password did not match...');
                res.redirect('/flash-message')
            }
        }
        else
        {
            req.flash('success', 'User not registered !');
            res.redirect('/flash-message')
        }
        

        // db.collection('login').insertOne(data, (err, collection)=>{
        //     if(err)
        //     {
        //         throw err;
        //     }
        //     //message = req.flash('user')
        //     //message1 = "Record Inserted Successfully !";
        //     req.flash('success', 'Record Inserted Successfully !');
        //     res.redirect('/flash-message')
        // });
    }
    //return res.redirect('index.html')
})

app.post('/signup',urlencodedParser,[
    check('user_name', 'This username must me 3+ characters long !')
        .exists()
        .isLength({ min: 3}),
    check('user_phone', 'Invalid Mobile No. !')
        .exists()
        .matches(/^[0-9]{10}$/),
    check('user_new_login', 'This username must me 3+ characters long !')
        .exists()
        .isLength({ min: 3}),
    check('user_new_password', 'Invalid Password !')
        .matches(/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8,}$/, "i"),
    check('user_new_email', 'Invalid Email-id !')
        .exists()
        .isEmail()
],async (req, res)=>{
    const errors = validationResult(req)
    if(!errors.isEmpty()){
        //return res.status(422).jsonp(errors.array())
        const alert = errors.array()
        res.render('index', {
            alert
        })
    }
    else
    {
        var username = req.body.user_name;
        var userphone = req.body.user_phone;
        var usernewlogin = req.body.user_new_login;
        var usernewpassword = req.body.user_new_password;
        var usernewemail = req.body.user_new_email;

        var data = {
            "username": username,
            "userphone": userphone,
            "usernewlogin": usernewlogin,
            "usernewpassword": usernewpassword,
            "usernewemail": usernewemail
        }

        const user = await db.collection('SignUp').findOne({userphone:req.body.user_phone});
        
        if(user != null)
        {
            console.log(true)
            req.flash('success', 'User Already Registered With Same Mobile No !');
            res.redirect('/flash-message')
        }
        else
        {
            const user = await db.collection('SignUp').findOne({usernewemail:req.body.user_new_email});
            if(user != null)
            {
                console.log(true)
                req.flash('success', 'User Already Registered With Same Email-id !');
                res.redirect('/flash-message')
            }
            else
            {
                const user = await db.collection('SignUp').findOne({usernewlogin:req.body.user_new_login});
                if(user != null)
                {
                    req.flash('success', 'Username already taken !');
                    res.redirect('/flash-message')
                }
                else
                {
                    db.collection('SignUp').insertOne(data,function(err, collection){
                        if (err)
                        { 
                            req.flash('success', err);
                            res.redirect('/flash-message')
                        }
                        else
                        {
                            req.flash('success',"Successfully Registered!! ");
                            res.redirect('/flash-message')
                        }
                    
                    });
                }
            }
        }
    }
})
app.get('/flash-message', (req, res)=>{
    res.render("index");
});

// const FeedBackSchema=new mongoose.Schema({
//         email_i:String,
//         mobno:String,
//         feedbackarea:String
// })

// const feed=new mongoose.model("FeedBack",FeedBackSchema)

app.post('/feed', urlencodedParser,[
    check('email_i', 'Invalid Email-id !')
        .exists()
        .isEmail(),
    
    check('mobno', 'Invalid Mobile No. !')
        .exists()
        .matches(/^[0-9]{10}$/)

    //check('feedbackarea', 'Invalid values in feedback !')
    //    .matches(/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8,}$/, "i"),

], async (req, res)=>{
    
    const errors = validationResult(req)
    if(!errors.isEmpty()){
        //console.log(errors);
        //return res.status(422).jsonp(errors.array())
        const alert = errors.array()
        console.log(alert)
        res.render('Feedback', {
            alert
        })
    }
    else
    {
        var email_i = req.body.email_i;
        var mobno = req.body.mobno;
        var feedbackarea = req.feedbackarea;

        var data = {
            "email_i": email_i,
            "mobno": req.body.mobno,
            "feedbackarea": req.body.feedbackarea
        }

        const user = await db.collection('SignUp').findOne({usernewemail:req.body.email_i});
        if(user != null)
        {
            const user = await db.collection('SignUp').findOne({ userphone:req.body.mobno});
            console.log(user)
            if(user != null)
            {
                db.collection('FeedBack').insertOne(data,function(err, collection){
                    if (err)
                    { 
                        req.flash('success', err);
                        res.redirect('/feed-message')
                    }
                    else
                    {
                        req.flash('success',"Feedback Sent Successfully !");
                        res.redirect('/feed-message')
                    }
                
                });
            }
            else
            {
                req.flash('success', 'Invalid User !');
                res.redirect('/feed-message')
            }
        }
        else
        {
            req.flash('success', 'Invalid User !');
            res.redirect('/feed-message')
        }
    }
})


app.get('/feed-message', (req, res)=>{
    res.render("Feedback");
});


app.post('/profile',async (req, res)=>{
    console.log(global.userlogin)
    const user = await db.collection('SignUp').findOne({usernewlogin:global.userlogin});
    if(user != null)
    {
        // const errors = validationResult(req)
        //return res.status(422).jsonp(errors.array())
        //const alert = user.array()
        //const alert = Object.values(user);
        //console.log(user)
        var data = [{
            Username: user.username,
            Email_id: user.usernewemail,
            Mob_No: user.userphone,
        }];
        res.render('Profile', {
            data:data
        });
    }
    else
    {
        req.flash('success', 'Unexpected Error Occured !');
        res.redirect('/flash-message')
    }
})

app.post('/dpred', async (req, res)=>{
    var Glucose = req.body.Glucose;
    var Insulin = req.body.Insulin;
    var BMI = req.body.BMI;
    var Age = req.body.Age;

    var data1 = "";

    const pythonOne = spawn('python3',['Diabetespredictor.py', Glucose, Insulin, BMI, Age]);
    pythonOne.stdout.on('data',function(data){
        data1 = data.toString();
        var result = "";
        
        data1 = data1.trim()

        if(data1 === "1")
        {
            result = "Warning : System Detected Diabetes Signs & Symptoms Please Verify It By Doing Respective Medical Tests !"
        }
        else if(data1 === "0")
        {
            result = "System Does Not Detected An Diabetes Signs & Symptoms !"
        }

        console.log(result);

        var info = [{
            GVal: Glucose,
            IVal: Insulin,
            BVal: BMI,
            AVal: Age,
            RVal: result,
        }];

        res.render('Daibetes', {
            info:info
        });
    })

    pythonOne.on('close', (code) => {
        console.log("code",code)
    })

})

app.post('/cancer', async (req, res)=>{
    var Clump = req.body.Clump;
    var UCellSize = req.body.UCellSize;
    var UCellShape = req.body.UCellShape;
    var Marginal = req.body.Marginal;
    var SingleECellSize = req.body.SingleEcellSize;
    var barenuclei = req.body.barenuclei;
    var BlandChromatin = req.body.BlandChromatin;
    var NormalNucleoli = req.body.NormalNucleoli;
    var Mitoses = req.body.Mitoses;

    var data1 = "";

    const pythonOne = spawn('python3',['breastcancer.py', Clump, UCellSize, UCellShape, Marginal, SingleECellSize, barenuclei, BlandChromatin, NormalNucleoli, Mitoses]);
    pythonOne.stdout.on('data',function(data){
        data1 = data.toString();
        var result = "";
        
        data1 = data1.trim()
        console.log(data1)
        if(data1 === "2")
        {
            result = "Warning : You have benign cancer type !"
        }
        else if(data1 === "4")
        {
            result = "Warning : You have malignant cancer type !"
        }

        console.log(result);

        var info = [{
            CVal: Clump,
            UCSVal: UCellSize,
            UCSHVal: UCellShape,
            MVal: Marginal,
            SVal: SingleECellSize,
            BAVal: barenuclei,
            BlVal: BlandChromatin,
            NVal: NormalNucleoli,
            MiVal: Mitoses,
            RVal: result,
        }];

        res.render('Cancer', {
            info:info
        });
    })

    pythonOne.on('close', (code) => {
        console.log("code",code)
    })

})

app.get('/flash-dprediction', (req, res)=>{
    res.render("Daibetes");
});

app.post('/profileup', [
    check('email_i', 'Invalid Email-id !')
        .exists()
        .isEmail(),
    
    check('mobno', 'Invalid Mobile No. !')
        .exists()
        .matches(/^[0-9]{10}$/)
], async(req, res)=>{
    // console.log(global.userlogin)
    const errors = validationResult(req)
    if(!errors.isEmpty()){
        //console.log(errors);
        //return res.status(422).jsonp(errors.array())
        const alert = errors.array()
        console.log(alert)
        res.render('profileup', {
            alert
        })
    }
    else
    {
        var user = await db.collection('SignUp').findOne({usernewemail:req.body.email_i});
        var user1 = await db.collection('SignUp').findOne({userphone:req.body.mobno});
        console.log(user);
        console.log(user1)
        if(user == null && user1 != null)
        {
           
            db.collection('SignUp').updateOne( {"usernewlogin": global.userlogin}, 
            { $set:{"usernewemail":req.body.email_i}},{upsert: true},function(err, collection){
            if (err)
            { 
                req.flash('success', err);
                res.redirect('/profile-message')
            }
            else
            {
                user = null;
                user1 = null;
                req.flash('success',"Email-Id Updated Successfully ! Duplicate Mobile No. Found");
                res.redirect('/profile-message')
            }
                
            });
            
        }
        else if(user != null && user1 == null)
        {
            db.collection('SignUp').updateOne( {"usernewlogin": global.userlogin}, 
            { $set:{"userphone":req.body.mobno}},{upsert: true},function(err, collection){
            if (err)
            { 
                req.flash('success', err);
                res.redirect('/profile-message')
            }
            else
            {
                user = null;
                user1 = null;
                req.flash('success',"Mobile No. Updated Successfully ! Duplicate Email.id Found");
                res.redirect('/profile-message')
            }
                
            });
        }
        else if(user === null && user1 === null)
        {
            db.collection('SignUp').updateOne( {"usernewlogin": global.userlogin}, 
            {$set:{"usernewemail":req.body.email_i}},{upsert: true},function(err, collection){
            if (err)
            { 
                req.flash('success', err);
                res.redirect('/profile-message')
            }
            else
            {
                db.collection('SignUp').updateOne( {"usernewlogin": global.userlogin}, 
                { $set:{"userphone":req.body.mobno}},{upsert: true},function(err, collection){
                if (err)
                { 
                    req.flash('success', err);
                    res.redirect('/profile-message')
                }
                else
                {
                    user = null;
                    user1 = null;
                    req.flash('success',"Mobile No. & Email-id Updated Successfully !");
                    res.redirect('/profile-message')
                }
                    
                });
            }
                
            });
        }
        else
        {
            user = null;
            user1 = null;
            req.flash('success', 'Duplicate Email-id & Mobile No. Found !');
            res.redirect('/profile-message')
        }

    }
});

app.get('/profile-message', (req, res)=>{
    res.render("profileup");
});


app.listen(port,()=>{
    console.log('Server started at http://localhost:${port}')
})
