$(document).ready( function () {
    var table = $('#table').DataTable({
          initComplete: function () {
              this.api().columns().every( function () {
                  var column = this;
                  var select = $('<select><option value=""></option></select>')
                      .appendTo( $(column.footer()).empty() )
                      .on( 'change', function () {
                          var val = $.fn.dataTable.util.escapeRegex(
                              $(this).val()
                          );
                        
                         //if Exclude checked then use serach plugin
                         if ($('.exclude').prop('checked')) {
                            //start by clearing column search
                            column
                              .search("");
                            //call ExcludeSearch
                            ExcludeSearch(val, column.index());
                         
                         //otherwise just use plain column search
                         } else {
  
                          column
                              .search( val ? '^'+val+'$' : '', true, false )
                              .draw();
                         }
                      } );
   
                  column.data().unique().sort().each( function ( d, j ) {
                      select.append( '<option value="'+d+'">'+d+'</option>' );
                  } );
              } );
          }
      } );
  
  
      function ExcludeSearch(term, column) {
        //apply search plugin
        $.fn.dataTable.ext.search.push(
          function(settings, data, dataIndex) {
              //if column data != to search term then return true to display
              if (data[column] != term) return true;
            
              //otherwise return false to filter from display
              return false;
          }   
        );
        //draw table based on search
        table.draw();
        //remove search plugin
        $.fn.dataTable.ext.search.pop();
      } 
  
  
  } );
  