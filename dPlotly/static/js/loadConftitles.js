
function populateValues() {
  
  //alert("start");
  var select1 = document.getElementById("exampleFormControlSelect1");
  //alert(select1);       
  var select2 = document.getElementById("exampleFormControlSelect2");       
  var selectedValue = select1.options[select1.selectedIndex].value;
  //document.write(selectedValue);
  //selectedValue.forEach(function(element){
  //alert(selectedValue);  
  select2.innerText = null
  var arr = selectedValue.replace("[","").replace("]","").split(",");
  //document.write(arr[0]);
  for (var i=0; i < arr.length;++i){

    addOption(select2, arr[i], arr[i]);
    
    }
  
  //selectedValue.forEach(func1);
  //select2.appendChild(selectedValue);  
//}    );

}
function addOption(selectbox,text,value )

{var optn = document.createElement("OPTION");

optn.text = text;

optn.value = value;

selectbox.options.add(optn);

}
