function startPlot(){
    var lineDiv = document.getElementById('bar');
 
    var traceA = {
    x: [25, 30, 100, 40, 45, 50, 55],
    y: [40, 20, 20, 60, 40, 20, 50],
    type: 'bar'
    };
 
    var data = [traceA];
 
    var layout = {
    title:'A Bar  in Plotly',
    height: 400,
    width: 450,
    showgrid : false,
    font: {
    size: 16,
    color: 'rgb(100,150,200)'
    },
    plot_bgcolor: 'rgba(81,151,209,0.2)',
    margin: {
    pad: 10
    },
    xaxis: {
    title: 'Distance  along x-axis',
    showgrid:true,
    titlefont: {
      color: 'black',
      size: 12
    },
    rangemode: 'tozero'
    },
    yaxis: {
    title: 'Distance travelled along y-axis',
    showgrid: true,
    titlefont: {
      color: 'black',
      size: 12
    },
    rangemode: 'tozero'
  }
};
 
Plotly.plot( lineDiv, data, layout );
scatterPlot();
}
function  scatterPlot() {
  
  var trace1 = {
    x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
    y: [8, 7, 6, 5, 4, 3, 2, 1, 0],
    type: 'scatter'
  };
  var trace2 = {
    x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
    y: [0, 1, 2, 3, 4, 5, 6, 7, 8],
    type: 'scatter'
  };
  var data = [trace1, trace2];
  var layout = {
    xaxis: {
      type: 'log',
      autorange: true,
      height :400,
      width:450
    },
    yaxis: {
      type: 'log',
      autorange: true
    }
  };
  Plotly.newPlot('scatter', data, layout);
  
  
}