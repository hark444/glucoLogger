function highlightValue(element, value) {
  const decimalNumber = +value;
  if (decimalNumber > 150) {
    element.classList.add("highlight");
  } else {
  console.log("commented else statement")
//    element.classList.remove("highlight");
  }
}

window.onload = function() {
  // Assuming you have the average values stored in variables
  const beforeMeal = document.getElementById("beforeMeal");
  const afterMeal = document.getElementById("afterMeal").innerHTML;
  const fasting = document.getElementById("fasting").innerHTML;

  highlightValue(beforeMeal, beforeMeal.innerHTML);
  highlightValue(afterMeal, afterMeal.innerHTML);
  highlightValue(fasting, fasting.innerHTML);
}
//
//window.onload = function() {
//google.charts.load('current', {packages: ['corechart', 'line']});
//google.charts.setOnLoadCallback(drawBackgroundColor);



function drawBackgroundColor(chartData) {
      var data = new google.visualization.DataTable();
      data.addColumn('date', 'Date');
      data.addColumn('number', 'Glucose Levels');

      data.addRows([
        chartData
      ]);

      var options = {
        hAxis: {
          title: 'Date'
        },
        vAxis: {
          title: 'Blood Glucose Levels'
        },
        backgroundColor: '#f1f8e9'
      };

      var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
      chart.draw(data, options);
    }
 }