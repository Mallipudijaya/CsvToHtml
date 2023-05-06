
 $.fn.dataTable.ext.search.push(
    function( settings, data, dataIndex ) {
        var exc = $('#exc').val();
          if (exc.length > 0) {
        var vfw = data[1]; // use data for the vfw column
        var m=data[2];
        var ref = new RegExp(exc, 'gi');
 
        // VFW
        if (vfw.match(ref))
        {
            return false;
        }
      }
 
        return true;
    }
);
 
$(document).ready(function() {
    var table = $('#table').DataTable(
    );
 
    // Event listener t o the two range filtering inputs to redraw on input
    $('#exc').keyup( function() {
        table.draw();
    } );
} );

