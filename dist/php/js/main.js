$(document).ready(function () {
	// event listeners
	// advanced search
	$('.query>label').on('click touch', function (event) {
		$('.form-control.form-select', $(this).parent()).toggleClass('hidden');
		// reset query
		// $('input.filter-query').val(null);
	});

	$('li.option').on('click touch', function (event) {
		console.log('clicked');
		$(this).toggleClass('active');
	});
	// initiate
	var getTable = function() {
		//row group
		//https://datatables.net/extensions/rowgroup/
		var table = $('#table').DataTable({
			order: [[0, 'desc']],
			lengthMenu: [[20, 50, 100, -1], [20, 50, 100, "All"]],
			//testing start
			serverSide: true,
			ajax: {
				url: "./php/index.php",
				type: 'POST',
				data: function (d) {
					// check if any inputs have data
					var inputData = $('input.filter-query').filter(function () { return $(this).val(); }).length > 0;
					if (inputData) {
						var input = {};
						$('input.filter-query').each(function () {
							input[$(this).attr("name")] = $(this).val();
						});
						return $.extend({}, d, {
							"filter": input,
							"sortColumn": d.columns[d.order[0].column].data,
							"sortDir": d.order[0].dir
						});
					// no inputs have data
					} else {
						return $.extend({}, d, {
							"filter": null,
							"sortColumn": d.columns[d.order[0].column].data,
							"sortDir": d.order[0].dir
						});
					}
				}
			},
			columns: [
				{ data: "Gene", mData: "Gene", title: "Gene" },
				{ data: "Last Evaluated", title: "Last Evaluated", 
					render: function (data, type, row) {
						if (data == null) {
							return null;
						} else if(type === "sort" || type === "type"){
							return data;
						} else {
							return new moment(data).format("YYYY-MM-DD");
						}
					} 
				},
				{ data: "Last Updated", title: "Last Updated", 
					render: function (data, type, row) {
						if (data == null) {
							return null;
						} else if(type === "sort" || type === "type"){
							return data;
						} else {
							return new moment(data).format("YYYY-MM-DD");
						}
					} 
				},
				{ data: "Nucleotide Change", title: "Nucleotide Change", 
					render: function (data, type, row) {
						if (data == null) {
							return null;
						} else {
							return '<span data-toggle="tooltip" title="' + data + '">' + data + '</span>';
						}
					} 
				},
				{ data: "Protein Change", title: "Protein Change", 
					render: function (data, type, row) {
						if (data == null) {
							return null;
						} else {
							return '<span data-toggle="tooltip" title="' + data + '">' + data + '</span>';
						}
					} 
				},
				{ data: "Other Mappings", title: "Other Mappings", 
					render: function (data, type, row) {
						if (data == null) {
							return null;
						} else {
							return '<span data-toggle="tooltip" title="' + data + '">' + data + '</span>';
						}
					} 
				},
				{ data: "Alias", title: "Alias", 
					render: function (data, type, row) {
						if (data == null) {
							return null;
						} else {
							return '<span data-toggle="tooltip" title="' + data + '">' + data + '</span>';
						}
					} 
				},
				{ data: "Transcripts", title: "Transcripts", 
					render: function (data, type, row) {
						if (data == null) {
							return null;
						} else {
							return '<span data-toggle="tooltip" title="' + data + '">' + data + '</span>';
						}
					} 
				},
				{ data: "Region", title: "Region", 
					render: function (data, type, row) {
						if (data == null) {
							return null;
						} else {
							return '<span data-toggle="tooltip" title="' + data + '">' + data + '</span>';
						}
					} 
				},
				{ data: "Reported Classification", title: "Reported Classification", 
					render: function (data, type, row) {
						if (data == null) {
							return null;
						} else {
							return '<span data-toggle="tooltip" title="' + data + '">' + data + '</span>';
						}
					} 
				},
				{ data: "Inferred Classification", title: "Inferred Classification", 
					render: function (data, type, row) {
						if (data == null) {
							return null;
						} else {
							return '<span data-toggle="tooltip" title="' + data + '">' + data + '</span>';
						}
					} 
				},
				{ data: "Source", title: "Source" },
				{ data: "URL", title: "URL", className: "url",
					render: function (data, type, row) {
						if (data == null) {
							return null;
						} else {
							return '<a data-toggle="tooltip" title="' + data + '" href=' + data + '>' + data + '</a>';
						}
					}
				},
				{ data: "Submitter Comment", title: "Submitter Comment", 
					render: function (data, type, row) {
						if (data == null) {
							return null;
						} else {
							return '<span data-toggle="tooltip" title="' + data + '">' + data + '</span>';
						}
					} 
				},
				{ data: "Assembly", title: "Assembly" },
				{ data: "Chr", title: "Chr" },
				{ data: "Genomic Start", title: "Genomic Start" },
				{ data: "Genomic Stop", title: "Genomic Stop" },
				{ data: "Ref", title: "Ref", 
					render: function (data, type, row) {
						if (data == null) {
							return null;
						} else {
							return '<span data-toggle="tooltip" title="' + data + '">' + data + '</span>';
						}
					} 
				},
				{ data: "Alt", title: "Alt", 
					render: function (data, type, row) {
						if (data == null) {
							return null;
						} else {
							return '<span data-toggle="tooltip" title="' + data + '">' + data + '</span>';
						}
					} 
				},
				{ data: "Accession", title: "Accession" },
				{ data: "Reported Ref", title: "Reported Ref" },
				{ data: "Reported Alt", title: "Reported Alt" },
			],
			
			processing: false, //client-side visual of processing queue
			searching: true,
			paging: true,
			info: false,
			lengthChange: false,
			responsive: true,
			autoWidth: false,
			orderCellsTop: true,
			fixedHeader: false,
			ordering: true,
			aaSorting: [],
			exportOptions: {
				rows: ':visible'
			},
			dom: 'BHtrp', // remove searchbar
			buttons: [
				{ text: 'Export', extend: 'csv', title: new moment(new Date).toISOString() },
				{ className: "filter", text: '', action: function (e, dt, node, config) { $('tr.filter').toggleClass('active'); }}
			],
			initComplete: function (settings) {	
				// column filtering
				var filter = $('#table thead tr').clone().off();
				// add class
				filter.addClass('filter');
				// remove sort from new row
				filter.find('th').removeClass("sorting");
				// add new rowspan
				filter.find('th').attr('rowspan', "2").attr('tabindex', "1");
				// add to table
				filter.appendTo('#table thead');
				// for each column
				$('#table thead tr:eq(1) th').each(function (i) {
					var title = $(this).text();
					$(this).html('<input class="filter-query" type="text" name="' + title + '"/>');
					$('input', $(this)).on('input', function (event) {
						if (table.column(i).search() !== this.value) {
							table.column(i).search(this.value).draw();
						}
					});
				});
			}
		});
	}();
});