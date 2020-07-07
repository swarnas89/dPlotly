function plots(){
    var trace1 = {
        x: [1, 4, 7, 10],
        y: [1, 1, 1, 1] ,
        text: ['<b>Topic 1</b><br><i>k1</i><br><i>k2</i><br><i>k3</i><br><i>k4</i><br>', 
        '<b>Topic 2</b><br><i>k1</i><br><i>k2</i><br><i>k3</i><br><i>k4</i><br>', 
        '<b>Topic 3</b><br><i>k1</i><br><i>k2</i><br><i>k3</i><br><i>k4</i><br>',
        '<b>Topic 4</b><br><i>k1</i><br><i>k2</i><br><i>k3</i><br><i>k4:<a href="/charts">link</a></i><br>'],
        textposition: 'top center',
        mode: 'markers+text',
        marker: {
          size: [80, 80, 80, 80],
          color:['rgb(93, 164, 214)', 'rgb(255, 144, 14)',  'rgb(44, 160, 101)', 'rgb(255, 65, 54)'],
          opacity: [1, 1, 1, 1]
        }
      };
      
      var data = [trace1];
      
      var layout = {
        title: 'Topic bubbles',
        showlegend: false,
        height: 600,
        width: 600,
        xaxis: {
            showticklabels: false,
            autotick: false,
            showgrid: false,
            zeroline: false
          },
          yaxis: {
            showticklabels: false,
            autotick: false,
            showgrid: false,
            zeroline: false
          },
      };
      
      Plotly.newPlot('myDiv', data, layout);
}