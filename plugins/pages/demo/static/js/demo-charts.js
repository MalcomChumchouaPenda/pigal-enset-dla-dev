
function createLineChart() {
    new Chart(document.querySelector('#lineChart'), {
        type: 'line',
        data: {
            labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
            datasets: [{
            label: 'Line Chart',
            data: [65, 59, 80, 81, 56, 55, 40],
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
            }]
        },
        options: {
            scales: {
            y: {
                beginAtZero: true
            }
            }
        }
    });
}


function createPieChart() {
    new Chart(document.querySelector('#pieChart'), {
        type: 'pie',
        data: {
            labels: [
            'Red',
            'Blue',
            'Yellow'
            ],
            datasets: [{
            label: 'My First Dataset',
            data: [300, 50, 100],
            backgroundColor: [
                'rgb(255, 99, 132)',
                'rgb(54, 162, 235)',
                'rgb(255, 205, 86)'
            ],
            hoverOffset: 4
            }]
        }
    });
}


function createBarChart()  {
    new Chart(document.querySelector('#barChart'), {
      type: 'bar',
      data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
          label: 'Bar Chart',
          data: [65, 59, 80, 81, 56, 55, 40],
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(255, 159, 64, 0.2)',
            'rgba(255, 205, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(201, 203, 207, 0.2)'
          ],
          borderColor: [
            'rgb(255, 99, 132)',
            'rgb(255, 159, 64)',
            'rgb(255, 205, 86)',
            'rgb(75, 192, 192)',
            'rgb(54, 162, 235)',
            'rgb(153, 102, 255)',
            'rgb(201, 203, 207)'
          ],
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
}


function createDoughnutChart() {
    new Chart(document.querySelector('#doughnutChart'), {
      type: 'doughnut',
      data: {
        labels: [
          'Red',
          'Blue',
          'Yellow'
        ],
        datasets: [{
          label: 'My First Dataset',
          data: [300, 50, 100],
          backgroundColor: [
            'rgb(255, 99, 132)',
            'rgb(54, 162, 235)',
            'rgb(255, 205, 86)'
          ],
          hoverOffset: 4
        }]
      }
    });
}


function createRadarChart() {
    new Chart(document.querySelector('#radarChart'), {
        type: 'radar',
        data: {
          labels: [
            'Eating',
            'Drinking',
            'Sleeping',
            'Designing',
            'Coding',
            'Cycling',
            'Running'
          ],
          datasets: [{
            label: 'First Dataset',
            data: [65, 59, 90, 81, 56, 55, 40],
            fill: true,
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgb(255, 99, 132)',
            pointBackgroundColor: 'rgb(255, 99, 132)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgb(255, 99, 132)'
          }, {
            label: 'Second Dataset',
            data: [28, 48, 40, 19, 96, 27, 100],
            fill: true,
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgb(54, 162, 235)',
            pointBackgroundColor: 'rgb(54, 162, 235)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgb(54, 162, 235)'
          }]
        },
        options: {
          elements: {
            line: {
              borderWidth: 3
            }
          }
        }
    });
}


function createPolarAreaChart() {
    new Chart(document.querySelector('#polarAreaChart'), {
        type: 'polarArea',
        data: {
          labels: [
            'Red',
            'Green',
            'Yellow',
            'Grey',
            'Blue'
          ],
          datasets: [{
            label: 'My First Dataset',
            data: [11, 16, 7, 3, 14],
            backgroundColor: [
              'rgb(255, 99, 132)',
              'rgb(75, 192, 192)',
              'rgb(255, 205, 86)',
              'rgb(201, 203, 207)',
              'rgb(54, 162, 235)'
            ]
          }]
        }
    });
}


function createStackedbarChart() {
    new Chart(document.querySelector('#stakedBarChart'), {
      type: 'bar',
      data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
            label: 'Dataset 1',
            data: [-75, -15, 18, 48, 74],
            backgroundColor: 'rgb(255, 99, 132)',
          },
          {
            label: 'Dataset 2',
            data: [-11, -1, 12, 62, 95],
            backgroundColor: 'rgb(75, 192, 192)',
          },
          {
            label: 'Dataset 3',
            data: [-44, -5, 22, 35, 62],
            backgroundColor: 'rgb(255, 205, 86)',
          },
        ]
      },
      options: {
        plugins: {
          title: {
            display: true,
            text: 'Chart.js Bar Chart - Stacked'
          },
        },
        responsive: true,
        scales: {
          x: {
            stacked: true,
          },
          y: {
            stacked: true
          }
        }
      }
    });
}


function createBubbleChart() {
    new Chart(document.querySelector('#bubbleChart'), {
      type: 'bubble',
      data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
            label: 'Dataset 1',
            data: [{
                x: 20,
                y: 30,
                r: 15
              },
              {
                x: 40,
                y: 10,
                r: 10
              },
              {
                x: 15,
                y: 37,
                r: 12
              },
              {
                x: 32,
                y: 42,
                r: 33
              }
            ],
            borderColor: 'rgb(255, 99, 132)',
            backgroundColor: 'rgba(255, 99, 132, 0.5)'
          },
          {
            label: 'Dataset 2',
            data: [{
                x: 40,
                y: 25,
                r: 22
              },
              {
                x: 24,
                y: 47,
                r: 11
              },
              {
                x: 65,
                y: 11,
                r: 14
              },
              {
                x: 11,
                y: 55,
                r: 8
              }
            ],
            borderColor: 'rgb(75, 192, 192)',
            backgroundColor: 'rgba(75, 192, 192, 0.5)'
          }
        ]
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            position: 'top',
          },
          title: {
            display: true,
            text: 'Chart.js Bubble Chart'
          }
        }
      }
    });
}


document.addEventListener("DOMContentLoaded", createLineChart);
document.addEventListener("DOMContentLoaded", createPieChart);
document.addEventListener("DOMContentLoaded", createBarChart);
document.addEventListener("DOMContentLoaded", createDoughnutChart);
document.addEventListener("DOMContentLoaded", createRadarChart);
document.addEventListener("DOMContentLoaded", createPolarAreaChart);
document.addEventListener("DOMContentLoaded", createStackedbarChart);
document.addEventListener("DOMContentLoaded", createBubbleChart);

