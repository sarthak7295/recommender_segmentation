



class Customer {
  constructor(name, recency,frequency,monetary,cluster) {
    this.name = name;
    this.recency = recency;
    this.frequency = frequency;
    this.monetary = monetary;
    this.cluster = cluster;
  }}


    $(".myButton").click(function () {
        var $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
        <!--var canvasObj = document.getElementById("canvas");-->


        var  rec = document.getElementById("recency").value;
        var  freq = document.getElementById("frequency").value;
        var  mon = document.getElementById("monetary").value;
        var  cluster = document.getElementById("segment").value;
        var  custId

        if(document.getElementById('new').checked) {
                custId = document.getElementById("customerIdNew").value;
        }
        else if(document.getElementById('old').checked) {

                custId = document.getElementById("customerId").value;
         }

        myCustomer = new Customer(custId, rec,freq,mon,cluster);
        console.log(myCustomer)
        var img = canvasObj.toDataURL();
        $.ajax({
            type: "POST",
            url: $SCRIPT_ROOT + "/predict/",
            data: img,
            success: function (data) {
                $('#result').text(' Predicted Output: ' + data);
            }
        });
    });

function changeTheType() {
  var x = document.getElementById("cust_new_div");
  var y = document.getElementById("cust_old_div");


  if (x.style.display === "none") {
    x.style.display = "block";
    y.style.display = "none";

  } else {
    x.style.display = "none";
    y.style.display = "block";

  }
}


document.addEventListener("DOMContentLoaded", function(){
console.log('hi foo')
//var users;
//$.ajax({
//            type: "GET",
//            url: $SCRIPT_ROOT + "/get/users",
//            data: json,
//            success: function (data) {
//                users = data;
//            }
//        });

//var select = document.getElementById("customerId");
//var options = ["1", "2", "3", "4", "5"];
//
//for(var i = 0; i < options.length; i++) {
//    var opt = options[i];
//    var el = document.createElement("option");
//    el.textContent = opt;
//    el.value = opt;
//    select.appendChild(el);
//}​


<!---->
<!---->
<!---->



    document.getElementById('old').checked = true;
   var x = document.getElementById("cust_new_div");
  var y = document.getElementById("cust_old_div");
      x.style.display = "none";
    y.style.display = "block";

});


