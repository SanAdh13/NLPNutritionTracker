function makeRawDataTable(data){
    var tableData = '';
    data.forEach(element => { 
        // console.log("x",element)
        tableData += "<tr>";
        tableData += "<td>"+element[0]+'</td>';
        tableData += "<td>"+element[1]+'</td>';
        tableData += "<td>"+element[2]+'</td>';
        tableData += "</tr>"; 
    })
    // clear the table before adding the new data 
    // $("#userData  tr").slice(1).remove();
    $('#userData').append(tableData)
}

function makeChart(values,l) {


    // right now we have Tx9 sized array
    // want 2D array where each nutrient = 9xT size array 

    //formattedArray is a 9 x T size array with each array corresponding to one of the nutrient
    formattedArray = []
    for(var i= 0; i < 9;i++){
        formattedArray[i] = [];  
        values.forEach(val=>{
            formattedArray[i].push(val[i])
        })
    }

    console.log(formattedArray)
    
    var canvas = $('#Nutritionlinechart');

    linechart = new Chart(canvas,{
        type:'line',
        data:{
            labels: l,
            datasets: [
            {
                label : 'Nutrient0',
                data : formattedArray[0],
                borderwidth : 1,
                fill : false,
                borderColor : "red"
            },
            {
                label : 'Nutrient1',
                data : formattedArray[1],
                borderwidth : 1,
                fill : false,
                borderColor : "blue"
            },
            {
                label : 'Nutrient2',
                data : formattedArray[2],
                borderwidth : 1,
                fill : false,
                borderColor : "green"
            },
            {
                label : 'Nutrient3',
                data : formattedArray[3],
                borderwidth : 1,
                fill : false,
                borderColor : "black"
            },
            {
                label : 'Nutrient4',
                data : formattedArray[4],
                borderwidth : 1,
                fill : false,
                borderColor : "pink"
            },
            {
                label : 'Nutrient5',
                data : formattedArray[5],
                borderwidth : 1,
                fill : false,
                borderColor : "orange"
            },
            {
                label : 'Nutrient6',
                data : formattedArray[6],
                borderwidth : 1,
                fill : false,
                borderColor : "light gray"
            },
            {
                label : 'Nutrient7',
                data : formattedArray[7],
                borderwidth : 1,
                fill : false,
                borderColor : "light green"
            },
            {
                label : 'Nutrient8',
                data : formattedArray[8],
                borderwidth : 1,
                fill : false,
                borderColor : "purple"
            }
        ]
        }
    });
    

    //TODO: need to figure out the way im gonna visualise this pie chart
    
    // I can either have 9 pie charts; each chart is one of the nutirent and each section is the timeframe 
    // for above use formattedArray
    // or i can have T amount pie charts; with 9 segments, each segment is one of the datatype 
    // for this use original Array


    var canvas1 = $('#NutritionPieChart');
    piechart = new Chart(canvas1,{
        type:'pie',
        data:{
            labels: l,
            datasets: [
                
            ]
        }
    });


    //TODO above the rawdatatable 
    // have a table that shows raw nutrition data for each timeframe 
    //          |Timeframe1 | ....  | TimeframeN    |
    //nutrition1|   TN      |   TN  |       TN      |
    //nutritionn|   TN      |   TN  |       TN      |
}


function vals(v){
    // the array returned val is a collection of n Timeframes (T)  
    // each T has 3 arrays 
    // the first one is for the table
    // second and third is for the charts
        
    var nutritionData = [] // T size array, with len 9 subarray with each index reperesenting one of the nutrient
    var labels = [] //T size array with the date labels
    
    v.forEach(timeframe => {
        // console.log("nutri",timeframe[1]);
        // console.log("label",timeframe[2]);
        makeRawDataTable(timeframe[0]);
        // forTableData.push(timeframe[0]);
        nutritionData.push(timeframe[1]);
        labels.push(timeframe[2]);  

    });

    // console.log("Table",forTableData)  
    makeChart(nutritionData,labels)
}    

var linechart;
var piechart;

$(function(){
    $('input[name="dateRange"]').daterangepicker({
        locale: {
            format: 'DD/MM/YYYY '
          }
    }, function(start, end, label) {
        $.ajax({
            type:"POST",
            url:"/getDates",
            data: {from:start.format('YYYY-MM-DD'),
                    to:end.format('YYYY-MM-DD')}
        }).done(function(values){
            if(linechart != null){
                linechart.destroy()
            };
            if(piechart != null){
                piechart.destroy()
            };
            $("#userData  tr").slice(1).remove();
            vals(values)
        });
    });
});

$(function(){
    $("#dateSelection").change(function(){
        var data = $(this).val();
        // alert(data)
        $.ajax({
            type:"POST",
            url:"/getGrouped",
            data: {data: data }
        })
        .done(function(returnedVal){
            if(linechart != null){
                linechart.destroy()
            };
            if(piechart != null){
                piechart.destroy()
            };
            $("#userData  tr").slice(1).remove();
            vals(returnedVal)
        }); 
    }) 
});

