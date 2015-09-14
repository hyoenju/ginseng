$(document).ready(function(){
	$('#graph_scatter').on('submit',function(e){
		e.preventDefault();
		x_value = $("#graph_x option:selected").val();
		y_value = $("#graph_y option:selected").val();
		startDate = $j("#startDate").datepicker("getDate");
		endDate = $j("#endDate").datepicker("getDate");
		var select_sensors=[]
		$("input[class=checkbox]:checked").each(function(){
			select_sensor = ($(this).val());
			select_sensors.push(select_sensor)
			})
		$.ajax({
			type     : "GET",
			cache    : false,
			url      : "/get_selector/", 
			data     : {'startDate': $j("#startDate").datepicker("getDate"),
			'endDate': $j("#endDate").datepicker("getDate")},
			success  : function(response) {

				
d3.json("/update_sensor/", function(error, data){
	
	var dataSet=[]
	if (x_value == "temperature" && y_value == "temperature"){
		data.forEach(function(d,i){
					dataSet.push([d.temperature, d.temperature]);
		});
	}else if (x_value == "temperature" && y_value == "humidity"){
		data.forEach(function(d,i){
					dataSet.push([d.temperature, d.humidity]);
		});
	}else if (x_value == "temperature" && y_value == "soil_humidity"){
		data.forEach(function(d,i){
					dataSet.push([d.temperature, d.soil_humidity]);
		});
	}else if (x_value == "temperature" && y_value == "illumination"){
		data.forEach(function(d,i){
					dataSet.push([d.temperature, d.illumination]);
		});
	}else if (x_value == "humidity" && y_value == "temperature"){
		data.forEach(function(d,i){
					dataSet.push([d.humidity, d.temperature]);
		});
	}else if (x_value == "humidity" && y_value == "humidity"){
		data.forEach(function(d,i){
					dataSet.push([d.humidity, d.humidity]);
		});
	}else if (x_value == "humidity" && y_value == "soil_humidity"){
		data.forEach(function(d,i){
					dataSet.push([d.humidity, d.soil_humidity]);
		});
	}else if (x_value == "humidity" && y_value == "illumination"){
		data.forEach(function(d,i){
					dataSet.push([d.humidity, d.illumination]);
		});
	}else if (x_value == "soil_humidity" && y_value == "temperature"){
		data.forEach(function(d,i){
					dataSet.push([d.soil_humidity, d.temperature]);
		});
	}else if (x_value == "soil_humidity" && y_value == "humidity"){
		data.forEach(function(d,i){
					dataSet.push([d.soil_humidity, d.humidity]);
		});
	}else if (x_value == "soil_humidity" && y_value == "soil_humidity"){
		data.forEach(function(d,i){
					dataSet.push([d.soil_humidity, d.soil_humidity]);
		});
	}else if (x_value == "soil_humidity" && y_value == "illumination"){
		data.forEach(function(d,i){
					dataSet.push([d.soil_humidity, d.illumination]);
		});
	}else if (x_value == "illumination" && y_value == "temperature"){
		data.forEach(function(d,i){
					dataSet.push([d.illumination, d.temperature]);
		});
	}else if (x_value == "illumination" && y_value == "humidity"){
		data.forEach(function(d,i){
					dataSet.push([d.illumination, d.humidity]);
		});
	}else if (x_value == "illumination" && y_value == "soil_humidity"){
		data.forEach(function(d,i){
					dataSet.push([d.illumination, d.soil_humidity]);
		});
	}else if(x_value == "illumination" && y_value == "illumination"){
		data.forEach(function(d,i){
					dataSet.push([d.illumination, d.illumination]);
		});
	};
	
//	switch (x_value, y_value){
//					case ("temperature", "temperature"):
//						data.forEach(function(d,i){
//							dataSet.push([d.temperature, d.temperature]);
//						});
//						break;
//					case ("temperature", "humidity"):
//						data.forEach(function(d,i){
//							dataSet.push([d.temperature, d.humidity]);
//						});
//						break;
//					case ("temperature", "soil_humidity"):
//						data.forEach(function(d,i){
//							dataSet.push([d.temperature, d.soil_humidity]);
//						});
//						break;
//					case ("temperature", "illumination"):
//						data.forEach(function(d,i){
//							dataSet.push([d.temperature, d.illumination]);
//						});
//						break;
//					case ("humidity", "temperature"):
//						data.forEach(function(d,i){
//							dataSet.push([d.humidity, d.temperature]);
//					});
//						break;
//				case ("humidity", "humidity"):
//						data.forEach(function(d,i){
//							dataSet.push([d.humidity, d.humidity]);
//						});
//						break;
//					case ("humidity", "soil_humidity"):
//						data.forEach(function(d,i){
//							dataSet.push([d.humidity, d.soil_humidity]);
//						});
//						break;
//					case ("humidity", "illumination"):
//						data.forEach(function(d,i){
//							dataSet.push([d.humidity, d.illumination]);
//						});
//						break;
//					case ("soil_humidity", "temperature"):
//						data.forEach(function(d,i){
//							dataSet.push([d.soil_humidity, d.temperature]);
//						});
//						break;
//					case ("soil_humidity", "humidity"):
//					data.forEach(function(d,i){
//							dataSet.push([d.soil_humidity, d.humidity]);
//						});
//						break;
//					case ("soil_humidity", "soil_humidity"):
//						data.forEach(function(d,i){
//							dataSet.push([d.soil_humidity, d.soil_humidity]);
//						});
//						break;
//					case ("soil_humidity", "illumination"):
//						data.forEach(function(d,i){
//							dataSet.push([d.illumination, d.illumination]);
//					});
//						break;
//					case ("illumination", "temperature"):
//						data.forEach(function(d,i){
//						dataSet.push([d.illumination, d.temperature]);
//						});
//						break;
//					case ("illumination", "humidity"):
//						data.forEach(function(d,i){
//							dataSet.push([d.illumination, d.humidity]);
//						});
//						break;
//					case ("illumination", "soil_humidity"):
//						data.forEach(function(d,i){
//						dataSet.push([d.illumination, d.soil_humidity]);
//						});
//						break;
//					case ("illumination", "illumination"):
//						data.forEach(function(d,i){
//							dataSet.push([d.illumination, d.illumination]);
//					});
//						break;
//	};

	var svgEle = document.getElementById("scatterGram");
	var svgWidth = window.getComputedStyle(svgEle, null).getPropertyValue("width");
	var svgHeight = window.getComputedStyle(svgEle, null).getPropertyValue("height");
	svgWidth = parseFloat(svgWidth);
	svgHeight = parseFloat(svgHeight);
	var offsetX = 30;
	var offsetY = 20;
	var xScale;
	var yScale;
	var yAxisHeight = svgHeight - 20;
	var xAxisWidth = svgWidth - 40;
	var svg = d3.select("#scatterGram");
	
	drawScale();
	var circleElements = svg
		.selectAll("circle")
		.data(dataSet)

	circleElements
		.enter()
		.append("circle")
		.attr("class", "mark")
		.attr("cx", svgWidth/2 + offsetX)
		.attr("cy", svgHeight/2 - offsetY)
		.attr("r", 100)
		.attr("opacity", 0)
		.transition()
		.duration(2000)
		.ease("bounce")
		.attr("cx", function(d, i){
			return xScale(d[0]) + offsetX;
		})
		.attr("cy", function(d,i){
			return yScale(d[1]);
		})
		.attr("r", 5)
		.attr("opacity", 1.0)

	function drawScale(){
		var maxX = d3.max(dataSet, function(d,i){
			return d[0];
		});
		var maxY = d3.max(dataSet, function(d,i){
			return d[1];
		});
		yScale = d3.scale.linear()
			.domain([0,maxY])
			.range([yAxisHeight,0])
				
		svg.append("g")
			.attr("class", "axis")
			.attr("transform" , "translate("+offsetX+","+(svgHeight-yAxisHeight-offsetY)+")")
			.call(
				d3.svg.axis()
					.scale(yScale)
					.orient("left")
			)
		xScale = d3.scale.linear()
			.domain([0, maxX])
			.range([0, xAxisWidth])
				
		svg.append("g")
			.attr("class", "axis")
			.attr("transform", "translate("+offsetX+","+(svgHeight-offsetY)+")")
			.call(
				d3.svg.axis()
					.scale(xScale)
					.orient("bottom")
				)
	
		var grid = svg.append("g")
		var rangeX = d3.range(10, maxX+10, 10);
		var rangeY = d3.range(10, maxY, 10);

		grid.selectAll("line.y")
			.data(rangeY)
			.enter()
			.append("line")
			.attr("class", "grid")
			.attr("x1", offsetX)
			.attr("y1", function(d,i){
				return svgHeight - yScale(d) - offsetY;
			})
			.attr("x2", xAxisWidth+offsetX)
			.attr("y2", function(d,i){
				return svgHeight - yScale(d) - offsetY;
			})
		grid.selectAll("line.x")
			.data(rangeX)
			.enter()
			.append("line")
			.attr("class","grid")
			.attr("x1", function(d,i){
				return xScale(d) + offsetX;
			})
			.attr("y1", svgHeight - offsetY)
			.attr("x2", function(d,i){
				return xScale(d) + offsetX;
			})
			.attr("y2", svgHeight - offsetY- yAxisHeight)
	}

	var tooltip = d3.select("#scatter")
	.append("div")
	.attr("id", "#tip")

	circleElements
		.on("mouseover", function(d){
			var x= parseFloat(d[0]);
			var y= parseFloat(d[1]);
			var data = d3.select(this).datum();
			var dx = parseFloat(data[0]);
			var dy = parseFloat(data[1]);
			tooltip
				.style("left", offsetX + x +"px")
				.style("top", offsetY +30 + y +"px")
				.style("visibility", "visible")
				.text(dx+","+dy)
			})
		.on("mouseout", function(){
			tooltip.style("visibility", "hidden")
		})
});

			},
			error		 : function(response) {
				alert("failed")
			}

		});
	});
});
