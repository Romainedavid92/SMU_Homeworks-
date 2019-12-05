// from data.js
var tableData = data;
// YOUR CODE HERE!
var tbody = d3.select("tbody");
tableData.forEach((sheepleReport) => {
    var row = tbody.append("tr");
    Object.values(sheepleReport).forEach((value) => {
      var cell = row.append("td");
      cell.text(value);
    });
  });
  // Select the button
var button = d3.select("#filter-btn");
button.on("click", function() {
    var inputElement = d3.select("#datetime");
    // Get the value property of the input element
    var inputValue = inputElement.property("value");
    var inputCity = d3.select("#city").property("value").toLowerCase();
    var inputState = d3.select("#state").property("value").toLowerCase();
    var inputCountry = d3.select("#country").property("value").toLowerCase();
    var inputShape = d3.select("#shape").property("value").toLowerCase();
    // alert(inputValue);
    // remove all table body rows
    d3.select("tbody").selectAll("tr").remove()
    let filteredData = tableData;
    // 5 input combos
    if (inputValue !== "" && inputCity !== "" && inputState !== "" && inputCountry !== "" && inputShape !== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.datetime === inputValue && ufoRow.city === inputCity && ufoRow.state === inputState && ufoRow.country === inputCountry && ufoRow.shape === inputShape);
    } 
    // 4 input combos
      else if (inputValue !== "" && inputCity !== "" && inputState !== "" && inputCountry !== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.datetime === inputValue && ufoRow.city === inputCity && ufoRow.state === inputState && ufoRow.country === inputCountry);
    } else if (inputValue !== "" && inputCity !== "" && inputState !== "" && inputShape !== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.datetime === inputValue && ufoRow.city === inputCity && ufoRow.state === inputState && ufoRow.shape === inputShape);
    } else if (inputValue !== "" && inputCity !== "" && inputCountry !== "" && inputShape !== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.datetime === inputValue && ufoRow.city === inputCity && ufoRow.Country === inputCountry && ufoRow.shape === inputShape);
    } else if (inputValue !== "" && inputState !== "" && inputCountry !== "" && inputShape !== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.datetime === inputValue && ufoRow.state === inputState && ufoRow.Country === inputCountry && ufoRow.shape === inputShape);
    } else if (inputCity !== "" && inputState !== "" && inputCountry !== "" && inputShape !== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.city === inputCity && ufoRow.state === inputState && ufoRow.Country === inputCountry && ufoRow.shape === inputShape);
    }
    // 3 input combos
      else if (inputValue !== "" && inputCity !== "" && inputState !== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.datetime === inputValue && ufoRow.city === inputCity && ufoRow.state === inputState);
    } else if (inputValue !== "" && inputCity !== "" && inputCountry !== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.datetime === inputValue && ufoRow.city === inputCity && ufoRow.country === inputCountry);
    } else if (inputValue !== "" && inputCity !== "" && inputShape !== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.datetime === inputValue && ufoRow.city === inputCity && ufoRow.shape === inputShape);
    } else if (inputValue !== "" && inputState !== "" && inputCountry !== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.datetime === inputValue && ufoRow.state === inputState && ufoRow.country === inputCountry);
    } else if (inputValue !== "" && inputState !== "" && inputShape!== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.datetime === inputValue && ufoRow.state === inputState && ufoRow.shape === inputShape);
    } else if (inputValue !== "" && inputCountry !== "" && inputShape!== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.datetime === inputValue && ufoRow.country === inputCountry && ufoRow.shape === inputShape);
    } else if (inputCity !== "" && inputState!== "" && inputCountry!== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.city === inputCity && ufoRow.state === inputState && ufoRow.country === inputCountry);
    } else if (inputCity !== "" && inputState!== "" && inputShape!== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.city === inputCity && ufoRow.state === inputState && ufoRow.shape === inputShape);
    } else if (inputState !== "" && inputCountry!== "" && inputShape!== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.state === inputState && ufoRow.country === inputCountry && ufoRow.shape === inputShape);
    }
    // 2 input combos
      else if (inputValue !== "" && inputCity !== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.datetime === inputValue && ufoRow.city === inputCity);
    } else if (inputValue !== "" && inputState !== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.datetime === inputValue && ufoRow.state === inputState);
    } else if (inputValue !== "" && inputCountry !== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.datetime === inputValue && ufoRow.country === inputCountry);
    } else if (inputValue !== "" && inputShape !== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.datetime === inputValue && ufoRow.shape === inputShape);
    } else if (inputCity !== "" && inputState !== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.city === inputCity && ufoRow.state === inputState);
    } else if (inputCity !== "" && inputCountry !== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.city === inputCity && ufoRow.country === inputCountry);
    } else if (inputCity !== "" && inputShape !== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.city === inputCity && ufoRow.shape === inputShape);
    } else if (inputState !== "" && inputCountry !== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.state === inputState && ufoRow.country === inputCountry);
    } else if (inputState !== "" && inputShape !== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.state === inputState && ufoRow.shape === inputShape);
    } else if (inputCountry !== "" && inputShape !== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.country === inputCountry && ufoRow.shape === inputShape);
    }
    // 1 input combos
      else if (inputValue !== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.datetime === inputValue);
    } else if (inputCity !== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.city === inputCity);
    } else if (inputState !== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.state === inputState);
    } else if (inputCountry !== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.country === inputCountry);
    } else if (inputShape !== ""){
      filteredData = tableData.filter(ufoRow => ufoRow.shape === inputShape);
    }
    // No Values Input
      else {
      alert("Please Enter a Value")
      }
    // refactored with arrow function
    filteredData.forEach((sheepleReport) => {
        var row = tbody.append("tr");
        Object.values(sheepleReport).forEach((value) => {
          var cell = row.append("td");
          cell.text(value);
        });
    });
});


  
