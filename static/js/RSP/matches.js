$( document ).ready(function() {

		table_matches = $('#matches').DataTable({
      destroy: true,
      ajax:"/rsp/list_all_matches?format=datatables",
      serverSide:true,
      searching: false,
			"columnDefs": [
      {
      	// The `data` parameter refers to the data for the cell.
        // The `rows`argument is an object representing all the data for the current row.
        "render": function ( data, type, row ) {
          return "<i class='material-icons' onclick=load_table_match_detail("+data+") \
					style='cursor: pointer' data-pk='" + data + "' >details</i>";
          },
          "targets": -1  // -1 is the last column, 0 the first, 1 the second, etc.
      }],
			order: [[ 2, "asc" ]],
    });

		table_ranking = $('#ranking').DataTable({
      destroy: true,
      ajax:"/rsp/top_leaders?format=datatables",
      serverSide:true,
      searching: false,
			order: [[ 1, "asc" ]],
    });
});

function load_table_match_detail(id){
	table_match_detail = $('#match_detail').DataTable({
		destroy: true,
		ajax:"/rsp/match_detail/"+id+"/?format=datatables",
		serverSide:true,
		searching: false
	});
}
