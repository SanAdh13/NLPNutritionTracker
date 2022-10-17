columns = ['Water (g)','Total nitrogen (g)','Protein (g)', 'Fat (g)','Carbohydrate (g)', 'Energy (kcal)','Total sugars (g)','Alcohol (g)','fibre (g)']

function makeRawDataTable(data){
    var tableData = '';
    data.forEach(element => { 
        tableData += "<tr>";
        tableData += "<td>"+element[0]+'</td>';
        tableData += "<td>"+element[1]+'</td>';
        tableData += "<td>"+element[2]+'</td>';
        tableData += "</tr>"; 
    })
    $('#userData').append(tableData)
}

function makeChart(values,lbl) {

    
    console.log("v", values);
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
    
    var canvas = $('#Nutritionlinechart');
    linechart = new Chart(canvas,{
        type:'line',
        data:{
            labels: lbl,
            datasets: [
            {
                label : columns[0],
                data : formattedArray[0],
                borderwidth : 1,
                fill : false,
                borderColor : "red"
            },
            {
                label : columns[1],
                data : formattedArray[1],
                borderwidth : 1,
                fill : false,
                borderColor : "blue"
            },
            {
                label : columns[2],
                data : formattedArray[2],
                borderwidth : 1,
                fill : false,
                borderColor : "green"
            },
            {
                label : columns[3],
                data : formattedArray[3],
                borderwidth : 1,
                fill : false,
                borderColor : "black"
            },
            {
                label : columns[4],
                data : formattedArray[4],
                borderwidth : 1,
                fill : false,
                borderColor : "pink"
            },
            {
                label : columns[5],
                data : formattedArray[5],
                borderwidth : 1,
                fill : false,
                borderColor : "orange"
            },
            {
                label : columns[6],
                data : formattedArray[6],
                borderwidth : 1,
                fill : false,
                borderColor : "light gray"
            },
            {
                label : columns[7],
                data : formattedArray[7],
                borderwidth : 1,
                fill : false,
                borderColor : "light green"
            },
            {
                label : columns[8],
                data : formattedArray[8],
                borderwidth : 1,
                fill : false,
                borderColor : "purple"
            }
        ]
        }
    });
    
 
    var table = "<table id='nutriTable' class='table table-striped'>";
    table += "<tr><th>Date</th>"
    columns.forEach(cols => {
        table+="<th>"+cols+"</th>";
    })
    table += "</tr>";

    console.log('v', values[0].slice(1,8));
    for (let index = 0; index < lbl.length; index++) {
        table+="<tr><td>"
        table+= lbl[index]
        table+="</td>"
 
        for(var j = 0 ; j < 9 ; j++){
            table+="<td>"
            table+=Number(parseFloat(values[index][j]).toFixed(2))
            table+="</td>"
        }
        table+="</tr>"  
    }
    table+='</table>'

    $(mycharts).append(table)


}


function vals(v){
    // the array returned val is a collection of n Timeframes (T)  
    // each T has 3 arrays 
    // the first one is for the table
    // second and third is for the charts
        
    var nutritionData = [] // T size array, with len 9 subarray with each index reperesenting one of the nutrient
    var labels = [] //T size array with the date labels
    
    v.forEach(timeframe => {
        makeRawDataTable(timeframe[0]);
        nutritionData.unshift(timeframe[1]);
        labels.unshift(timeframe[2]);  

    });
    makeChart(nutritionData,labels)
}    

var linechart;
var piechart;
function cleanup(){
    // clearing the charts & tables if it already exists
    if(linechart != null){
        linechart.destroy()
    };
    if(piechart != null){
        piechart.destroy()
    }; 
    $('#nutriTable').remove()
    $("#userData  tr").slice(1).remove();
}

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

            cleanup()
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
            cleanup()
            vals(returnedVal)
        }); 
    }) 
});

