function makeRawDataTable(data){
    var tableData = '';

    data.forEach(element => {
        // console.log(element)
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

function makeChart(returnedVal) {
    //TODO: implement the chart 
    //this one will update the chart 
    $.each(returnedVal,function(i,val){

    });
}


function vals(v){
    // the array returned val is a collection of n arrays (TimeFrames)

    v.forEach(timeframe => {
        // each timeframe has 3 arrays 
        // the first one is for the table
        //second and third is for the charts
        
        forTableData = timeframe[0];
        nutritionData =  timeframe[1];
        dateForXAxis = timeframe[2]  
        
        makeRawDataTable(forTableData);

    });
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
            console.log(values)
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
            console.log(returnedVal)
            $("#userData  tr").slice(1).remove();
            vals(returnedVal)
        }); 
    }) 
});

