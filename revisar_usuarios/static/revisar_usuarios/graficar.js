

// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Area Chart Example  
var ejeX =[];
for (i=0;i<256;i++){
  ejeX[i]=i;
}
var senalIR=[122741,122762,122778,122776,122790,122810,122796,122807,122860,122886,122856,122747,122673,122586,122458,122318,122263,122243,122215,122150,122076,122064,122017,121991,121972,121974,122014,122055,122039,122037,122064,122056,122078,122069,122131,122209,122214,122218,122211,122216,122212,122203,122219,122278,122326,122318,122294,122321,122322,122322,122309,122322,122419,122460,122466,122456,122486,122501,122518,122493,122600,122658,122708,122705,122724,122731,122742,122734,122786,122849,122893,122906,122851,122801,122732,122615,122485,122414,122359,122316,122225,122151,122110,122059,122014,121957,121984,122040,122054,122013,122009,122021,122054,122059,122056,122099,122203,122221,122202,122233,122244,122247,122241,122261,122316,122345,122320,122307,122321,122331,122346,122330,122362,122453,122468,122498,122466,122505,122515,122530,122537,122568,122650,122680,122657,122684,122714,122723,122707,122753,122813,122862,122860,122798,122761,122684,122582,122420,122337,122283,122215,122110,122037,121977,121927,121884,121825,121834,121869,121879,121856,121840,121861,121877,121876,121883,121961,122035,122066,122066,122109,122116,122126,122093,122143,122190,122216,122256,122207,122231,122254,122255,122241,122273,122344,122422,122430,122407,122427,122464,122463,122444,122496,122577,122614,122656,122649,122675,122702,122708,122687,122752,122797,122841,122806,122721,122668,122568,122458,122302,122256,122239,122156,122088,121987,121952,121919,121863,121812,121883,121910,121891,121875,121896,121911,121929,121890,121966,122064,122119,122124,122127,122158,122171,122162,122128,122188,122245,122278,122271,122271,122297,122300,122314,122329,122373,122439,122499,122482,122503,122509,122544,122554,122558,122609,122689,122734,122757,122752,122773,122806,122796,122786,122853,122919,122916,122879,122825,122757,122632,122513,122424,122387,122340,122263,122187,122148,122111,122074,122042,122052,122094,122112,122072,122052,122071,122101,122101,122108,122196,122274,122288,122287,122323,122326,122320,122319,122330,122405,122450,122433,122441,122440,122451,122457,122438,122490,122572,122603,122628,122612,122634,122653,122634,122648,122713,122792,122829,122819,122823,122876,122876,122869,122890,122949,123009,122989,122935,122880,122789,122684,122570,122505,122473,122440,122372,122315,122287,122278,122228,122211,122212,122270,122281,122270,122258,122285,122309,122319,122306,122377,122455,122463,122450,122457,122482,122482,122465,122502,122528,122576,122600,122567,122573,122592,122601,122597,122638,122700,122759,122745,122743,122758,122781,122784,122772,122825,122878,122921,122935,122951,122979,122981,122991,122966,122996,123025,123009,122908,122781,122714,122613,122514,122425,122420,122449,122401,122346,122325,122303,122302,122258,122270,122308,122345,122352,122343,122361,122385,122387,122373,122424,122506,122535,122531,122501,122502,122511,122495,122485,122525,122591,122587,122573,122583,122619,122611,122605,122664,122723,122777,122784,122787,122801,122822,122835,122824,122860,122931,122987,122995,122979,123030,123036,123034,122992,122993,123010,122945,122852,122730,122636,122554,122473,122407,122398,122407,122382,122337,122320,122296,122272,122242,122263,122297,122336,122353,122351,122361,122402,122396,122408,122434,122510,122540,122532,122506,122518,122526,122517,122483,122531,122613,122647,122649,122637,122650,122670,122685,122650,122724,122795,122846,122856,122844,122875,122889,122871,122888,122935,123009,123038,123044,123050,123064,123055,123014,122999,122985,122919,122813,122703,122622,122541,122470,122401,122377,122415,122392,122364,122320,122308];
var senalIR2=[]
var j=0;
for (i=0;i<512;i=i+2){
  senalIR2[j]=senalIR[i];
  j++;
}
j=0;
var ejeY=[];
for (i=0;i<256;i++){
  ejeY[i]=0;
}
var ctx = document.getElementById("graficaSpO2");
var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    //labels: ["Mar 1", "Mar 2", "Mar 3", "Mar 4", "Mar 5", "Mar 6", "Mar 7", "Mar 8", "Mar 9", "Mar 10", "Mar 11", "Mar 12", "Mar 13"],
    labels: ejeX,
    datasets: [{
      label: "Pletismografia",
      lineTension: 0.3,
      backgroundColor: "rgba(2,117,216,0.2)",
      borderColor: "rgba(2,117,216,1)",
      pointRadius: 5,
      pointBackgroundColor: "rgba(2,117,216,1)",
      pointBorderColor: "rgba(255,255,255,0.8)",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(2,117,216,1)",
      pointHitRadius: 50,
      pointBorderWidth: 2,
      //data: [900, 0, 26263, 18394, 18287, 28682, 31274, 33259, 25849, 24159, 32651, 31984, 38451],
      data: ejeY,
      fill: false,
    }],
  },
  options: {
    animation: {
      duration: 0 // general animation time
  },
  hover: {
      animationDuration: 0 // duration of animations when hovering an item
  },
  responsiveAnimationDuration: 0, // animation duration after a resize
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 7
        }
      }],
      yAxes: [{
        ticks: {
          //min: 0,
          //max: 40000,
          maxTicksLimit: 5
        },
        gridLines: {
          color: "rgba(0, 0, 0, .125)",
        }
      }],
    },
    legend: {
      display: false
    }
  }
});


console.log("VISUALIZANDO");

// se realiza el llamado a la función cada 20 ms  
setInterval(miFuncion, 20);
var senalAnalizarIR=[];
function miFuncion(){ 
  
  // valores de saturación y frecuencia cardíaca
  var script_tag=document.getElementById("graficar.js");
  const requestURL = 'http://127.0.0.1:8000/APIusuario/'+script_tag.getAttribute("one")+'/?format=json';
  console.log("LEYENDO DATOS DE SERVIDOR");
  const request = new XMLHttpRequest();
  request.open('GET', requestURL);
  request.responseType = 'json';
  request.send();
  request.onload = function() {
    const RESPUESTA = request.response;
    document.getElementById("frecuencia_cardiaca").textContent=RESPUESTA['frecuenciaCardiaca'];
    document.getElementById("saturacion_oxigeno").textContent=RESPUESTA['oximetria'];
    

    myLineChart.data.datasets[0].data=RESPUESTA['pletismografia'].senal
    // actualización de grafica importando un dato a la vez del array
    /*for (i=0;i<256;i++){senalAnalizarIR[i]=senalAnalizarIR[i+1];}
    senalAnalizarIR[255]=RESPUESTA['pletismografia'].senal[j];
    j=j+1;
    for (i=0;i<256;i++){ 
    myLineChart.data.datasets[0].data[i]=senalAnalizarIR[i];  
    }*/

    myLineChart.update();

  }

}



// OBTENER EL VALOR DE SpO2 Y FC

//const requestURL = 'http://proyecto123.pythonanywhere.com/revisar/examinarusuario/1/?format=json';
/*
const requestURL = 'http://127.0.0.1:8000/APIusuario/1/?format=json';
console.log("HOLA MUNDSO");
const request = new XMLHttpRequest();
request.open('GET', requestURL);
request.responseType = 'json';
request.send();
request.onload = function() {
  const RESPUESTA = request.response;
  document.getElementById("frecuencia_cardiaca").textContent=RESPUESTA['pletismografia'].senal[100];
  document.getElementById("saturacion_oxigeno").textContent="'"+RESPUESTA['presion']+"'";

}
*/

/*
fetch("http://proyecto123.pythonanywhere.com/revisar/examinarusuario/1/?format=json")
  .then(function (response) {
    return response.json();
  })
  .then(function (myJson) {
    console.log(myJson.ip);
  })
  .catch(function (error) {
    console.log("Error: " + error);
  });
*/
/*
fetch("http://proyecto123.pythonanywhere.com/revisar/examinarusuario/1/?format=json")
  .then(function (response) {
    return response.json();
  })
  .then(function (myJson) {
    console.log(myJson.ip);
  })
  .catch(function (error) {
    console.log("Error: " + error);
  });
*/
//document.getElementById("frecuencia_cardiaca").textContent="100";
//document.getElementById("saturacion_oxigeno").textContent="90";

