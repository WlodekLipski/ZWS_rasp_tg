chartRanges = {"temperature" : ["17-19", "20-22", "23-25"],
    "light": ["350-450", "451-550", "551-650"],
    "humidity":["0-20", "21-40", "41-60", "61-80", "81-100"]}

chartData = {"temperature" : [],
    "light": [],
    "humidity":[]}


var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on('modified', function(data) {
    var newData = data['data'];
    start(newData)
});



function drawChart(chart_divId, chart_title) {
   var trace = {
        type: 'bar',
        x: chartRanges[chart_title],
        y: chartData[chart_title],
    };

    var data = [ trace ];

    chart_title = chart_title.charAt(0).toUpperCase() + chart_title.slice(1);
    var layout = {
      title: chart_title,
      font: {size: 18}
    };

    Plotly.react(chart_divId, data, layout);
}

function drawAllCharts(){
    var chartTitle = "";
    for(let chartDiv of document.getElementById("chart-container").children)
    {
        chartTitle = chartDiv.id.split("-")[0];
        drawChart(chartDiv.id, chartTitle);
    }
}

function start(data){
        initializeArrays();
        refreshData(data);
}


function initializeArrays(){
    for(let prop in chartRanges){
        chartData[prop] = new Array(chartRanges[prop].length);
        for(var rangeIndex=0; rangeIndex<chartRanges[prop].length; ++rangeIndex)
            chartData[prop][rangeIndex] = 0;
    }
}

function refreshData(data){
    var csvData = data;
    if(data.length)
        updateData(csvData);
    drawAllCharts();
}

function updateData(csvData){
    var optionIndex = 0;
    var value = 0;
    for(let option of csvData[0][0].split(";"))
    {
        if(option!="" && option!=";") {
            option = option.toLowerCase();
            for (var dataItself = 1; dataItself < csvData.length; dataItself++) {
                var csvValue = csvData[dataItself][0].split(";")[optionIndex];
                if (csvValue != "" && csvValue != ";") {
                    value = parseInt(csvValue);
                    addValueToChart(value, option.toLowerCase());
                }
            }
            optionIndex++;
        }
    }
}

function addValueToChart(value, chart_title){
    var rangeIndex = getRangeIndex(value, chart_title);
    if(rangeIndex!=-1)
        chartData[chart_title][rangeIndex] +=1;
}

function getRangeIndex(value, chart_title){
    var index = 0;

    for(let range of chartRanges[chart_title]) {
        if (isInRange(range, value))
        {
            return index;
        }
        index++;
    }
    return -1;
}

function isInRange(range, value){
    if(value>=parseInt(range.split("-")[0]) && value<=parseInt(range.split("-")[1]))
        return true;
    return false;
}

