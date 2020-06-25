// ------------------------------------------------------ TODO
//SET UP FULLSCREEN
//ADD CSS TO PAGE
// COMPLETE DESCRIPTION




//------------------------------------------------------- TESTING 

let offline = false; // disable text to test video
let menu = true;


// //SETTING WORKING FOR EXPERIMENTS
//FOR MULTPLE VIDEOS
let videoEffects = false;
let randomFrameEffect = false; // works with no effect
let playSimpleVideo = true; //actually plays random videos // currently not working, do not know why, probably come changes in for loop // FIX // PROBLEM WITH VOLUME OR SOMETHING // currently appears as default iF one video is false
let oneVideo = false; // effects wonk work when false // just 1.mp4 


// //SETTING WORKING FOR EXPERIMENTS
//FOR SINGLE VIDEO WITH RANDOM FRAME
// let videoEffects = false;
// let randomFrameEffect = true; // works with no effect
// let playSimpleVideo = false; //actually plays random videos // currently not working, do not know why, probably come changes in for loop // FIX // PROBLEM WITH VOLUME OR SOMETHING // currently appears as default iF one video is false
// let oneVideo = true; // effects wonk work when false // just 1.mp4 
/////////------------------------------------------------- CANVAS----------

let canvas;

/////////------------------------------------------------- MOBILE NET VIDEO ----------

//ML5
let myMobileNet;

/////----------------------------------------------------- TRANSLATION MODULE

var entryLang = 'es';
var exitLang = 'en';
var translatedRes = '';

var translateAPIKey = 'AIzaSyAGvEzCaMeaL_woHEsCo_w85802jZVuYnI';

let translate = true;

//----------------------------------------------------------- CAMERA --------

// https://ml5js.github.io/ml5-examples/javascript/ImageClassification_Video/ // REVIEW
//ls -ltrh /dev/video* // check cameras available in Linux

// https://github.com/ITPNYU/ICM-2015/blob/master/09_video_sound/02_capture/13_get_sources/sketch.js // get cameras available
// Seriously.js
// https://www.youtube.com/watch?v=jdKep6jo7b0&list=PLRqwX-V7Uu6aKKsDHZdDvN6oCJ2hRY_Ig&index=8

// EFFECTS PIXEL MIRROR
// https://www.youtube.com/watch?v=rNqaw8LT2ZU&list=PLRqwX-V7Uu6aKKsDHZdDvN6oCJ2hRY_Ig&index=4

//PAINTING
// https://www.youtube.com/watch?v=0V3uYA1hafk&list=PLRqwX-V7Uu6aKKsDHZdDvN6oCJ2hRY_Ig&index=6

//SCAN
// https://www.youtube.com/watch?v=YqVbuMPIRwY&list=PLRqwX-V7Uu6aKKsDHZdDvN6oCJ2hRY_Ig&index=7

let cameraVideo;

let videoON = false;
let showVideo = 0;


//----------------------------------------------------------- VIDEO ----------

//VIDEO
// https://p5js.org/reference/#/p5.MediaElement
// https://creative-coding.decontextualize.com/video/

let playing = false;

let stage = 1;
let videos = [];
let whichVideo = 0;
let amountVideos = 5;

var vScale = 1; // scale of video // check set up to adjust vscale according to type of video effect  //Adjust video size // actually increases the accuracy of the prediction model


let pixelColor;

//------------------------------------------------------------- TEXT ----------
//To merge all text files
// cat * > merged-file
let writingOutput = false;
let writer;
let linesInPage = 10; // amount of lines in page
let page = []; // text file written

let resultsReady = false;

//------------------------------------------------------------- SAVE IMAGES ----------

let saveImages = false;


//text displayed in "TERMINAL" text
let rnn;
let mbNetLabel0 = '';
let mbNetConfidence0 = ''; //i think i am not using this
let mbNetLabel1 = '';
let mbNetLabel2 = '';
let confidence = '';

//ml5 result as subtitle text
let rnnSub = '';
let regexRnnSub = '';
let initRegx = '';
let printFinalText = '';

//parameters for "terminal" text
let sourceText = ' ';
let textSpeed = 0;


//TEXTS 
let textToLoad;
let txt;
var totalSentences;
let count = 0;

let terminal = false;
var showTerminal = 0;

let subtitle = false;
let showSubtitle = 0;

// //--------------Connectors text XIX CENTURY TRAVELER
let entrance = ['I think this is a ', 'When I find a ', 'Later on, I think of this ', 'Although I don\'t believe that this is a ', 'But, if you wander through the ', 'Last time I saw a ', 'I couldn\'t believe a ', 'I feel I already saw a ', 'Just after a ', 'Before this ', 'After encountering this ', 'Also, this ', 'Later on, the ', 'Above all, this ', ];


let middle = [' ', ' ', ' ', ' ', ' ', ' ', ' ', '. ', ', ', ', but ', ', moreover, ', ', however, ', ', in short,', ', but also, ', ', in addition, ', ', nevertheless, ', ', I rather think of ', ' we can discuss about', ' I doubted my self, but ', ' was there ', ];

// let entrance = [' '];
// let middle = [' '];

// //--------------Connectors text XIX CENTURY TRAVELER

//--------------Connectors text LATIN GAMEON
// let entrance = ['Creo que esto es un ', 'A veces, cuando encuentro un ', 'Más tarde, yo pensaría que un ', 'Aunque no crea que esto es un ', 'Pero, si recorres el ', 'La última vez que ví un ', 'No podría crer que un ', 'Siento que ya he visto este ', 'Justo antes de este ', 'Antes de este ', 'Después de reconcer este ', 'También, este ', 'Más tarde, el ', 'Sobre todo, este ', ];

// let middle = [' ', ' ', ' ', ' ', ' ', ' ', ' ', '. ', ', ', '. ', ', ', ', pero ', ', sin embargo, ', ', en resumen,', ', pero también, ', ', además, ', ', me gustaría pensar que ', ' podemos discutir acerca de', ' dudaba de mi, pero ', ' estaba ahí ', ];

//--------------------------TEXT SEEDS ----------
let startingSeeds = entrance[0];
let middleSeeds = middle[0];

//----------------------------------------------------------------  SOUND ----------

// http://ability.nyu.edu/p5.js-speech/ 
// https://generative.fm/record
var myVoice = new p5.Speech(); // new P5.Speech object // OFFLINE 
let voice = 'Google UK English Male';
// let voice = 'Google español de Estados Unidos';

//List of voices
// 'Google Deutsch', 'Google US English', 'Google UK English Female', 'Google UK English Male', 'Google español', 'Google español de Estados Unidos', 'Google français', 'Google हिन्दी', 'Google Bahasa Indonesia', 'Google italiano', 'Google 日本語', 'Google 한국의', 'Google Nederlands', 'Google polski', 'Google português do Brasil', 'Google русский', 'Google 普通话（中国大陆）', 'Google 粤語（香港', 'Google 國語（臺灣'


//BACKGROUND MUSIC
let sounds = [];
let otherSong;

//------------------------------------------------------------- WEB SETTINGS ----------


p5.disableFriendlyErrors = true; // disables FES //to upgrade performance

// ------------------------------------------------------------------------------------------------------------
// ------------------------------------------------- PRE LOAD  ------------------------------------------------
// ------------------------------------------------------------------------------------------------------------


function preload() { // To add things that take time to load


    // textToLoad = loadStrings('subTexts.txt', txtLoaded);


    myMobileNet = ml5.imageClassifier('MobileNet'); // put name of model aT the end

    // VIDEOS
    if (oneVideo) {
        videos[whichVideo] = createVideo("videos/1.mp4"); //captures video from videofile
        console.log('ONE VIDEO ON');
    } else {
        console.log('MULTI VIDEO ON');

        for (i = 0; i < amountVideos; i++) {
            videos[i] = createVideo(`videos/random_narrative_videos/${i + 1}.mp4`); //captures video from videofile
        }
        console.log('x Videos: ' + videos.length);

    }

    //LOAD MODEL LSTM
    if (translate) {
        rnn = ml5.charRNN("test-lstm/model_8_latin/"); // lATIN model for GameOn --> ESTE ES EL QUE ANDA Y ES TRADUCIDO AL INGLES
    } else {
        rnn = ml5.charRNN("test-lstm/model_124/"); // XIX century traveler
        // rnn = ml5.charRNN("test-lstm/lstm-ml5-models/bolano/"); // ml5 Models
        // rnn = ml5.charRNN("test-lstm/lstm-ml5-models/gpt2-travel-lit/"); --> NO funciona, arquitectura diferente

    }

    //SOUND
    // createConvolver('background_sound/drones.wav', soundReady);

    sounds[1] = loadSound('background_sounds/drones.wav');
    sounds[2] = loadSound('background_sounds/seven.wav');
    sounds[0] = loadSound('background_sounds/pulse-modulation.wav');
    // sounds[3] = loadSound('background_sound/eyes.wav');

}

// ------------------------------------------------------------------------------------------------------------
// ------------------------------------------------- SET UP ---------------------------------------------------
// ------------------------------------------------------------------------------------------------------------

function setup() {
    noCursor();

    canvas = createCanvas(windowWidth, windowHeight);
    canvas.style('display', 'block'); // Remove scrollbars by setting the style property display: block

    canvas.parent('sketch-holder'); // Move the canvas so it’s inside our <div id="sketch-holder">.


    // background(255, 0, 200);

    // createCanvas(windowWidth, windowHeight);
    // createCanvas(1280, 720); // original

    frameRate(30);
    pixelDensity(1);

    // console.log('my Mobile: ', myMobileNet) // to test

    //-------------VIDEO 

    if (videoEffects) {
        vScale = 20; // changes size of square, before was 15
    } else {
        vScale = 1;
    }

    if (oneVideo) {
        videos[whichVideo].size(width / vScale, height / vScale);
        videos[whichVideo].hide();
    } else if (playSimpleVideo) {
        for (i = 0; i < videos.length; i++) {
            videos[i].size(width / vScale, height / vScale);
            videos[i].hide();
        }
    }


    //-------------  ML5
    // myMobileNet.classify(myVideo, callback);
    myMobileNet.classify(videos[0], gotResults);
}


// ------------------------------------------------------------------------------------------------------------
// ------------------------------------------------- DRAW -----------------------------------------------------
// ------------------------------------------------------------------------------------------------------------


function draw() {

    // colorMode(RGB, 255, 255, 255, 1);
    background(0, 50); //antes 50
    menuCommands();

    // ENABLE AUDIOCONTEXT REQUIREMENT FOR BROWSER
    // if (getAudioContext().state !== 'running') {
    //     text('click to start audio', width / 2, height / 2);
    // }

    renderVideos();

    // filter(BLUR, 3);

    // let c = get(windowWidth / 2, windowHeight / 2);
    // tint(127, 127, 127);
    // let c = get();

    // fill(c, 127);

    // noStroke();
    // rectMode(CENTER);
    // blendMode(DIFFERENCE);
    // rect(50, 50, windowWidth - 300, windowHeight - 300);

    // extraText();


    // ------------------ Display TEXT from Model
    if (resultsReady) {
        // DoTextHiperpoesia();
        // console.log(rnnSub);

        //cuadradito para acentuar subtitulos
        // fill(0, 95);
        // rect(0, windowHeight - 200, windowWidth, 180);

        DoText();
        // talk();



        if (saveImages) {

            let interval = 10;
            if (frameCount % (interval * 30) == 0 || key === 's') {
                save(canvas, month() + "/" + day() + "/" + year() + "_" + 'canvas' + "_" + frameCount + "_" + ".jpg");

            }
        }

        if (writingOutput) {
            writer = createWriter(month() + "/" + day() + "/" + year() + "_" + 'latinPage' + "_" + frameCount + "_" + ".txt"); // texto en donde escribir 


        }

    }

}

// ------------------------------------------------------------------------------------------------------------
// ------------------------------------------------- END DRAW -------------------------------------------------
// ------------------------------------------------------------------------------------------------------------

//------------------------------------------WINDOW SIZE ELEMENTS

// if (key === 's') {
//     save(canvas, month() + "/" + day() + "/" + year() + "_" + 'canvas' + "_" + frameCount + "_" + ".jpg");
// }

//Set a fullscreen button

function mousePressed() {
    if (mouseX > 0 && mouseX < 100 && mouseY > 0 && mouseY < 100) {
        let fs = fullscreen();
        fullscreen(!fs);
    }
}

// dynamically adjust the canvas to the window
function windowResized() {
    resizeCanvas(windowWidth, windowHeight);
}

// ------------------------------- MENU

function menuCommands() {
    if (keyCode == 77) { //letter m
        textSize(18);
        fill(255);
        noStroke();
        textLeading(30);
        textAlign(LEFT);
        let menu = "Menu: \n Render Video =  space bar \n Set random Video = Enter \n Black Screen-random-number = Up arrow \n Talk =s ";
        text(menu, windowWidth / 2, windowHeight / 2 + 100, 350, 400);
    }
}



// ---------------------------------------


// ------------------------------------------------------------------------------------------------------------
// ------------------------------------------------- INSTRUCTIONS ---------------------------------------------
// ------------------------------------------------------------------------------------------------------------


// GENERAL WORKING AND TESTING BRANCH 

//Instructions to run
// https://ml5js.org/reference/api-ImageClassifier/
// In terminal enter the folder in which the code is hosted
// python3 -m http.server
// python -m http.server 8000 --bind 127.0.0.1
// http://localhost:8000/  //works best with this. Does not work with Firefox

// OTHER Option to run server
// http - server
// service nginx restart

//You have to click on the screen to be able to hear the background sounds