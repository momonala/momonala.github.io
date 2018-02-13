var help_site =  'https://www.biobots.io/biowiki/biobots-software-introduction-the-basics/'

$(document).ready(function() {
	// TIME SERIES LINES 
	$(chart_id).highcharts({
		chart: {'renderTo': 'chart_ID', 'type': 'line', 'height': 500},
		title: {text: 'Cell Viability'},
		xAxis: {title: {text: 'Print Iterations'}},
		yAxis: {title: {text: 'Percent'}},
		credits: {enabled: true, text: 'need help?', href: help_site},
		series: series
	});
	
	$(chart_id2).highcharts({	
		chart: {'renderTo': 'chart_ID2', 'type': 'line', 'height': 500},
		title: {text: 'Crosslinking'},
		xAxis: {title: {text: 'Print Iterations'}},
		yAxis: {title: {text: 'units'}},
		credits: {enabled: true, text: 'need help?', href: help_site},
		series: series2
	});
	
	$(chart_id3).highcharts({	
		chart: {'renderTo': 'chart_id3', 'type': 'line', 'height': 500},
		title: {text: 'Extruder Pressure'},
		xAxis: {title: {text: 'Print Iterations'}},
		yAxis: {title: {text: 'PSI'}},
		credits: {enabled: true, text: 'need help?', href: help_site},
		series: series3
	});
	
	$(chart_id4).highcharts({	
		chart: {'renderTo': 'chart_id4', 'type': 'line', 'height': 500},
		title: {text: 'Layer Resolution'},
		xAxis: {title: {text: 'Print Iterations'}},
		yAxis: {title: {text: 'units'}},
		credits: {enabled: true, text: 'need help?', href: help_site},
		series: series4
	});
	
	
	// BOXPLOTS 
		$(chart_id_box).highcharts({
		chart: {'renderTo': 'chart_ID_box', 'type': 'boxplot', 'height': 500},
		title: {text: 'Cell Viability'},
		xAxis: {title: {text: 'Print Iterations'}},
		yAxis: {title: {text: 'Percent'}},
		credits: {enabled: true, text: 'need help?', href: help_site},
		series: series
	});
	
	$(chart_id2_box).highcharts({	
		chart: {'renderTo': 'chart_ID2_box', 'type': 'boxplot', 'height': 500},
		title: {text: 'Crosslinking'},
		xAxis: {title: {text: 'Print Iterations'}},
		yAxis: {title: {text: 'units'}},
		credits: {enabled: true, text: 'need help?', href: help_site},
		series: series2
	});
	
	$(chart_id3_box).highcharts({	
		chart: {renderTo: 'chart_id3_box', type: 'boxplot', height: 500},
		title: {text: 'Extruder Pressure'},
		xAxis: {title: {text: 'Print Iterations'}},
		yAxis: {title: {text: 'PSI'}},
		credits: {enabled: true, text: 'need help?', href: help_site},
		series: series3
	});
	
	$(chart_id4_box).highcharts({	
		chart: {'renderTo': 'chart_id4_box', 'type': 'boxplot', 'height': 500},
		title: {text: 'Layer Resolution'},
		xAxis: {title: {text: 'Print Iterations'}},
		yAxis: {title: {text: 'units'}},
		credits: {enabled: true, text: 'need help?', href: help_site},
		series: series4
	});
	
});


