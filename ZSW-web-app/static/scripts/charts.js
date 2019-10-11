chartRanges = {"temperature" : ["17-19", "20-22", "23-25"],
    "light": ["350-450", "450-550", "550-650"],
    "humidity":["0-20", "20-40", "40-60", "60-80", "80-100"]}

chartData = {"temperature" : [5, 10, 2],
    "light": [30, 50, 20],
    "humidity":[1, 2, 5, 4, 0]}


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

    Plotly.newPlot(chart_divId, data, layout);
}

function drawAllCharts(){
    var chartTitle = "";
    for(let chartDiv of document.getElementById("chart-container").children)
    {
        chartTitle = chartDiv.id.split("-")[0];
        drawChart(chartDiv.id, chartTitle);
    }
}