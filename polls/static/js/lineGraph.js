d3.selectAll(".import_data").on("click", function(){
	graph = this.id
	data_url = "/"+graph

d3.json(data_url, function(error, data){
	var svgEle = document.getElementById("lineGraph");
	var svgWidth = window.getComputedStyle(svgEle, null).getPropertyValue("width");
	var svgHeight = window.getComputedStyle(svgEle, null).getPropertyValue("height");
	svgWidth = parseFloat(svgWidth) - 60;
	svgHeight = parseFloat(svgHeight) - 60;
	var offsetX = 30;
	var offsetY = 20;
	var scale = 2.0;
	var rangeYear = 10;
	var year = d3.extent(data, function(d){
		return d.created_at;
	});
	var startYear = year[0];
	var currentYear = 2000;
	var margin = svgWidth /(rangeYear - 1);

	
	pickupData(data);
	drawScale();

	function drawGraph(dataSet, itemName, cssClassName, type){

		var line = d3.svg.line()
		  .x(function(d, i){
				return offsetX + i * margin;
			})
		  .y(function(d, i){
				return svgHeight - (d[itemName] * scale) - offsetY;
			})
		  .interpolate(type)
		var lineElements = d3.select("#lineGraph")
		  .append("path")
		  .attr("class", "line "+cssClassName)
		  .attr("d", line(dataSet))
			.attr("id", itemName)
	}
	function drawScale(){
		var yScale = d3.scale.linear()
		  .domain([0, 100]) 
		  .range([scale*100, 0])
		d3.select("#lineGraph")
			  .append("g")
			  .attr("class", "axis")
			  .attr("transform", "translate("+offsetX+", "+((100-(scale-1)*100)+offsetY)+")")
			  .call(
					d3.svg.axis()
				  .scale(yScale)
				  .orient("left")
				)
		var xScale = d3.time.scale()
		  .domain([0,svgWidth])
		  .range([0, svgWidth]) 
		d3.select("#lineGraph")
			  .append("g")
			  .attr("class", "axis")
			  .attr("transform", "translate("+offsetX+", "+(svgHeight - offsetY)+")")
			  .call(
					d3.svg.axis()
				  .scale(xScale)
				  .orient("bottom")
				  .ticks(10)
				  .tickFormat(function(d, i){
						var fmtFunc = d3.time.format("%");
						return fmtFunc(d);
					})
				)
			  .selectAll("text")
			  .attr("transform", "rotate(90)")
			  .attr("dx", "0.7em")
			  .attr("dy", "-0.4em")	
			  .style("text-anchor", "start")
	}
	function pickupData(data){
		dataSet = [ ];	
		for(var i=0; i<data.length; i++){
			dataSet[i] = data[i];
		}
		d3.select("#lineGraph").selectAll("*").remove();
	}
	
	
//	drawGraph(dataSet,"temperature" , "temperature", "linear");
	d3.selectAll(".sensor").on("click",function(){
		var type = this.value;
		var display = this.checked? true : false;
		var name = this.id; 			
		if (display==true){
			drawGraph(dataSet, type , name , "linear");
		}
		else{
		name = "sensor_0"
			drawGraph(dataSet, type , name , "linear");
		}		
	});

});
});
