
<script type="text/javascript">
          var rIndex,
          table = document.getElementById("table");
          function checkEmptyInput()
              {
                  var isEmpty = false,
                      p_id = document.getElementById("p_id").value,
                      q_id = document.getElementById("q_id").value,
                      category = document.getElementById("category").value;

                  if(p_id === ""){
                      alert("First Name Connot Be Empty");
                      isEmpty = true;
                  }
                  else if(q_id === ""){
                      alert("Last Name Connot Be Empty");
                      isEmpty = true;
                  }
                  else if(category === ""){
                      alert("category Connot Be Empty");
                      isEmpty = true;
                  }
                  return isEmpty;
              }
              // add Row
            function addHtmlTableRow()
            {
                // get the table by id
                // create a new row and cells
                // get value from input text
                // set the values into row cell's
                if(!checkEmptyInput()){
                var newRow = table.insertRow(table.length),
                    cell1 = newRow.insertCell(0),
                    cell2 = newRow.insertCell(1),
                    cell3 = newRow.insertCell(2),
                    p_id = document.getElementById("p_id").value,
                    q_id = document.getElementById("q_id").value,
                    category = document.getElementById("category").value;

                cell1.innerHTML = p_id;
                cell2.innerHTML = q_id;
                cell3.innerHTML = category;
                // call the function to set the event to the new row
                selectedRowToInput();
            }
            }
            // display selected row data into input text
            function selectedRowToInput()
            {
                
                for(var i = 1; i < table.rows.length; i++)
                {
                    table.rows[i].onclick = function()
                    {
                      // get the seected row index
                      rIndex = this.rowIndex;
                      document.getElementById("p_id").value = this.cells[0].innerHTML;
                      document.getElementById("q_id").value = this.cells[1].innerHTML;
                      document.getElementById("category").value = this.cells[2].innerHTML;
                    };
                }
            }
            selectedRowToInput();


            function editHtmlTbleSelectedRow()
            {
                var p_id = document.getElementById("p_id").value,
                    q_id = document.getElementById("q_id").value,
                    category = document.getElementById("category").value;
               if(!checkEmptyInput()){
                table.rows[rIndex].cells[0].innerHTML = p_id;
                table.rows[rIndex].cells[1].innerHTML = q_id;
                table.rows[rIndex].cells[2].innerHTML = category;
              }
            }

            function removeSelectedRow()
            {
                table.deleteRow(rIndex);
                // clear input text
                document.getElementById("p_id").value = "";
                document.getElementById("q_id").value = "";
                document.getElementById("category").value = "";
            }




// check the empty input
         </script>
             